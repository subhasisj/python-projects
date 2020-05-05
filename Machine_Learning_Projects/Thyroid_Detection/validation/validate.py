import sys
sys.path.append('../')
from utilities.utils import FileUtils
import json
import os
import re

import pandas as pd
import streamlit as st


class Validate:

    def __init__(self,logger,path_to_files,schema_path):
        self._logger = logger
        self._path_to_files = path_to_files
        self._schema_path = schema_path


    def _load_schema(self):
        try:
            self._logger.log(f'Loading Schema from {self._schema_path}')
            with open(self._schema_path,'r') as f:
                data = json.load(f)
                f.close()
            pattern = data['SampleFileName']
            LengthOfDateStampInFile = data['LengthOfDateStampInFile']
            LengthOfTimeStampInFile = data['LengthOfTimeStampInFile']
            column_names = data['ColName']
            NumberofColumns = data['NumberofColumns']

            return pattern,LengthOfDateStampInFile,LengthOfTimeStampInFile,column_names,NumberofColumns
            
        except Exception as e:
            self._logger.log(str(e),'critical')
            raise e
    
    def _check_file_name_format(self):
        """
            The File name format has to be something like 
            hypothyroid_0211198_0102062111998.csv
        """
        regex = "['hypothyroid']+['\_'']+[\d_]+[\d]+\.csv"
        pattern,LengthOfDateStampInFile,LengthOfTimeStampInFile,column_names,NumberofColumns = self._load_schema()
        validation_result = {}
        all_files = [file for file in os.listdir(self._path_to_files)]
        self._logger.log(f'Validating file names for {len(all_files)} files')
        for file in all_files:
            if (re.match(regex, file)):
                splitAtDot = re.split('.csv', file)
                splitAtDot = (re.split('_', splitAtDot[0]))
                if len(splitAtDot[1]) == LengthOfDateStampInFile:
                    if len(splitAtDot[2]) == LengthOfTimeStampInFile:
                        validation_result[file] = 'valid'
                    else:
                        validation_result[file] = 'invalid'
                        self._logger.log(f'Validating file {file} for file name: invalid')
                else:
                    validation_result[file] = 'invalid'
                    self._logger.log(f'Validating file {file} for file name: invalid')
            else:
                validation_result[file] = 'invalid'
                self._logger.log(f'Validating file {file} for file name: invalid')
        return validation_result


    def _check_column_length(self,validation_result):
        filtered_files = [key for key, value in validation_result.items() if value == 'valid']
        pattern,LengthOfDateStampInFile,LengthOfTimeStampInFile,column_names,NumberofColumns = self._load_schema()

        for file in filtered_files:
            path_to_file = os.path.join(self._path_to_files,file)
            csv = pd.read_csv(path_to_file)
            if csv.shape[1] == NumberofColumns:
                    pass
            else:
                validation_result[file] = 'invalid'
                self._logger.log(f'Validating file {file} for column length: invalid')
        
        return validation_result

    def _check_for_columns_with_missing_values(self,validation_result):
        filtered_files = [key for key, value in validation_result.items() if value == 'valid']
        pattern,LengthOfDateStampInFile,LengthOfTimeStampInFile,column_names,NumberofColumns = self._load_schema()
        for file in filtered_files:
            path_to_file = os.path.join(self._path_to_files,file)
            csv = pd.read_csv(path_to_file)
            for column in csv.columns:
                    if (len(csv[column]) - csv[column].count()) == len(csv[column]):
                        validation_result[file] = 'invalid'
                        self._logger.log(f'Validating file {file} for missing values in Column {column}: invalid')
                        break
                    else:
                        validation_result[file] = 'valid'
        return validation_result
        
    def _segregate_good_and_bad_data(self,validation_result):
       
        fileutils = FileUtils(self._logger,self._path_to_files)
        # Delete the folders if already existing and create again
        fileutils.delete_directory('good')
        fileutils.delete_directory('bad')
        path_to_good_files = fileutils.create('good')
        path_to_bad_files = fileutils.create('bad')

        for key, value in validation_result.items():
            if value == 'invalid':
                fileutils.move_files(key,os.path.join(self._path_to_files,'bad'))
            else:
                fileutils.move_files(key,os.path.join(self._path_to_files,'good'))
        return path_to_good_files,path_to_bad_files


    def validate_files(self):
        # file name validation
        self._logger.log('Validating for file names:')
        validation_result = self._check_file_name_format()

        # Column Length Validation
        self._logger.log('Validating for Column length:')
        validation_result = self._check_column_length(validation_result)

        # Missing values validation
        self._logger.log('Validating for Missing Values:')
        validation_result = self._check_for_columns_with_missing_values(validation_result)

        # Segregate Good and Bad Data
        path_to_good_files,path_to_bad_files = self._segregate_good_and_bad_data(validation_result)

        return validation_result,path_to_good_files,path_to_bad_files
    # def _transform_data(self):
    #     # Make data ready to be inserted into database

    # def _save_data_to_database(self):
    #     # store to db
        
    # def _save_data_to_csv(self):
    #     # store to csv
    # pass
