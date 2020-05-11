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
    def __init__(self,training_file_path,schema_path):
        self._training_file_path = training_file_path
        self._schema_path = schema_path
        self._time_created = datetime.now()
        self._logger = Logger(f'validation_preprocessing_logs_{self._time_created.date()}_{self._time_created.strftime("%H%M%S")}.log')
        self._path_to_good_files = None
        self._path_to_bad_files = None
    
    def _run_validation(self):

        self._logger.log('Starting training files validation')
        try:
            training_files_validation = ValidateData(self._logger,self._training_file_path,self._schema_path)
            validation_result,path_to_good_files,path_to_bad_files = training_files_validation.validate_files()
        except:
            self._logger.log(f'No Valid Files Found in {self._training_file_path}')
            raise Exception('No Valid files found')
        self._logger.log('Training Files Validaiton Completed.') #
        st.info('Validation Results:')
        st.write(validation_result)
        st.subheader('Files moved to:')

        self._path_to_good_files = path_to_good_files
        self._path_to_bad_files = path_to_bad_files
        st.info(f'Path to Good Files: "{self._path_to_good_files}"')
        st.info(f'Path to Bad Files: "{self._path_to_bad_files}"')

        return validation_result

    def _preprocess_data(self):
        data_reader = GlobDataReader(self._logger,self._path_to_good_files)
        df = data_reader.read()

        # st.write(data_to_clean.count().compute())
        unnecessary_columns = ['TSH_measured','T3_measured','TT4_measured','T4U_measured','FTI_measured','TBG_measured','TBG','TSH']
        preprocessor = Preprocessor(self._logger,unnecessary_columns)
        cleaned_data = preprocessor.transform(df)
        date = self._time_created.date()
        time = self._time_created.strftime("%H%M%S")
        preprocessor_save_path = f'./artifacts/preprocessing/preprocessor_{date}_{time}.joblib'
        dump(preprocessor,preprocessor_save_path ) 
        st.info(f'Preprocessor saved as preprocessor_{date}_{time}.joblib')
        self._logger.log(f'Preprocessor: Preprocessor saved as {preprocessor_save_path}')

        return cleaned_data

    def _get_parent_folder(self,full_path):
        return str(Path(full_path).parents[0])  # "path/to"


    def _save_preprocessed_data(self,data):
        date = self._time_created.date()
        time = self._time_created.strftime("%H%M%S")
        # db_path = os.path.join(self._training_file_path,'training_db')

        fileutils = FileUtils(self._logger,self._get_parent_folder(self._training_file_path)) 
        db_path = fileutils.create('Training_DB')
        # db = SqliteDbHandler(self._logger,db_path,f'training_db_{date}_{time}')
        db = SqliteDbHandler(self._logger,db_path,'training_db')
        db.create_db_connection()
        db.save_table_in_db('thyroid_training',data)

    def start_validation(self): 
        
        # bar = st.progress(0)
        with st.spinner('Validating files now, please wait.....'):
        # Validation
            validation_result = self._run_validation()
            st.info('Validation Completed')

        # Read Data from all files in Good Folder and run preprocessing
        with st.spinner('Preprocessing Data now, please wait....'):
            df = self._preprocess_data()
            st.info('Preprocessing Data Completed')
        
        # Sample Unbalanced Classes
        with st.spinner('Handling imbalanced classes, please wait....'):
            sampler = ImbalancedHandler(self._logger,df,'Class')
            df = sampler.handle()
            st.info('Handling Imbalanced classes completed')
        # Save data to DB
        with st.spinner('Saving cleaned data to DB, please wait....'):
            self._save_preprocessed_data(df)
            st.info('Data saved data to DB successfully')
        st.balloons()


