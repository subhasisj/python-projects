import sys
sys.path.append('../')
from logger.logger import Logger
from validation.validate import ValidateData
from preprocessing.preprocessing import Preprocessor
from preprocessing.imbalanced_handler import ImbalancedHandler
from db_operations.sqlite_db import SqliteDbHandler
from data_reader.data_reader import GlobDataReader,DaskDataReader
from utilities.utils import FileUtils
from sqlalchemy.types import Integer


import streamlit as st
from joblib import dump, load
import os
import pandas as pd
import dask.dataframe as dd
import glob
from datetime import datetime
from pathlib import Path


class ValidationController:
    def __init__(self,file_path,schema_path,process):
        self._file_path = file_path
        self._schema_path = schema_path
        self._time_created = datetime.now()
        self._logger = Logger(f'validation_{process}_logs_{self._time_created.date()}_{self._time_created.strftime("%H%M%S")}.log')
        self._path_to_good_files = None
        self._path_to_bad_files = None
        self.process = process
    
    def _run_validation(self):

        self._logger.log('Starting files validation')
        try:
            files_validation = ValidateData(self._logger,self._file_path,self._schema_path)
            validation_result,path_to_good_files,path_to_bad_files = files_validation.validate_files()
        except:
            self._logger.log(f'No Valid Files Found in {self._file_path}')
            raise Exception('No Valid files found')
        self._logger.log('Files Validaiton Completed.') #
        st.info('Validation Results:')
        st.write(validation_result)
        st.subheader('Files moved to:')

        self._path_to_good_files = path_to_good_files
        self._path_to_bad_files = path_to_bad_files
        st.info(f'Path to Good Files: "{self._path_to_good_files}"')
        st.info(f'Path to Bad Files: "{self._path_to_bad_files}"')

        return validation_result
    
    def get_preprocessor(self):

        unnecessary_columns = ['TSH_measured','T3_measured','TT4_measured','T4U_measured','FTI_measured','TBG_measured','TBG','TSH']
        preprocessor = Preprocessor(self._logger,unnecessary_columns)
        return preprocessor

    def _preprocess_data(self):
        data_reader = GlobDataReader(self._logger,self._path_to_good_files)
        df = data_reader.read()
        preprocessor = self.get_preprocessor()
        cleaned_data = preprocessor.transform(df)
        date = self._time_created.date()
        time = self._time_created.strftime("%H%M%S")
        self._save_preprocessor(preprocessor)
        # preprocessor_save_path = f'./artifacts/preprocessing/preprocessor_{date}_{time}.joblib'
        # dump(preprocessor,preprocessor_save_path ) 
        # st.info(f'Preprocessor saved as preprocessor_{date}_{time}.joblib')
        # self._logger.log(f'Preprocessor: Preprocessor saved as {preprocessor_save_path}')

        return cleaned_data

    def _save_preprocessor(self,preprocessor):
        try:
            self._logger.log(f'Preprocessor: Attempting to save preprocessor') 
            self._path_to_artifacts = os.path.join('.','artifacts')
            fileutils = FileUtils(self._logger,self._path_to_artifacts)
            preprocessor_save_path = os.path.join(fileutils.create('preprocessing',delete_before_creation=True),'preprocessor.joblib')
            dump(preprocessor,preprocessor_save_path )
            st.info(f'Preprocessor saved as {preprocessor_save_path}')
            self._logger.log(f'Preprocessor: Preprocessor saved as {preprocessor_save_path}') 
        except Exception as e:
            self._logger.log(f'Preprocessor: Exception occured while saving preprocessor - {str(e)}') 

    def _get_parent_folder(self,full_path):
        return str(Path(full_path).parents[0])  # "path/to"


    def _save_preprocessed_data(self,data):
        date = self._time_created.date()
        time = self._time_created.strftime("%H%M%S")
        # db_path = os.path.join(self._training_file_path,'training_db')

        fileutils = FileUtils(self._logger,self._get_parent_folder(self._file_path)) 
        db_path = fileutils.create(f'{self.process}_DB')
        # db = SqliteDbHandler(self._logger,db_path,f'training_db_{date}_{time}')
        db = SqliteDbHandler(self._logger,db_path,f'{self.process}_db')
        db.create_db_connection()
        db.save_table_in_db(f'thyroid_{self.process}',data)

    def start_validation(self): 
        
        # bar = st.progress(0)
        with st.spinner('Validating files now, please wait.....'):
        # Validation
            validation_result = self._run_validation()
            st.info('Validation Completed')

        # Read Data from all files in Good Folder and run preprocessing
        with st.spinner('Preprocessing Data now, please wait....'):
            self._preprocessed_data = self._preprocess_data()
            st.write(self._preprocessed_data)
            st.info('Preprocessing Data Completed')
        
        # # Sample Unbalanced Classes
        # with st.spinner('Handling imbalanced classes, please wait....'):
        #     sampler = ImbalancedHandler(self._logger,df,'Class')
        #     df = sampler.handle()
        #     st.info('Handling Imbalanced classes completed')
        # # Save data to DB
        # with st.spinner('Saving cleaned data to DB, please wait....'):
        #     self._save_preprocessed_data(df)
        #     st.info('Data saved data to DB successfully')
        # st.balloons()



class ValidationController_training(ValidationController):
    def __init__(self,file_path,schema_path):
        super().__init__(file_path,schema_path,process='training')
        
    def start_validation(self):
        super().start_validation()
        # Sample Unbalanced Classes
        with st.spinner('Handling imbalanced classes, please wait....'):
            sampler = ImbalancedHandler(self._logger,self._preprocessed_data,'Class')
            df = sampler.handle()
            st.info('Handling Imbalanced classes completed')
        # Save data to DB
        with st.spinner('Saving cleaned data to DB, please wait....'):
            self._save_preprocessed_data(df)
            st.info('Data saved data to DB successfully')
        st.balloons()

class ValidationController_inference(ValidationController):
    def __init__(self,file_path,schema_path):
        super().__init__(file_path,schema_path,process='inferencing')
        

    def get_preprocessor(self):
        preprocessor_path = os.path.join('.','artifacts','preprocessing','preprocessor.joblib')
        return load(preprocessor_path)

    def  _save_preprocessor(self,preprocessor):
        pass


    def start_validation(self):
        super().start_validation()
        
        # Save data to DB
        with st.spinner('Saving cleaned data to DB, please wait....'):
            self._save_preprocessed_data(self._preprocessed_data)
            st.info('Data saved data to DB successfully')
        st.balloons()
        
       

    




