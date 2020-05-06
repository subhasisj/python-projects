import sys
sys.path.append('../')
from logger.logger import Logger
from validation.validate import Validate
from preprocessing.preprocessing import Preprocessor
import streamlit as st
import os
import pandas as pd
import dask.dataframe as dd

class Training:
    def __init__(self,training_file_path,schema_path):
        self._training_file_path = training_file_path
        self._schema_path = schema_path
        self._logger = Logger('training_logs.log')
        self._path_to_good_files = None
        self._path_to_bad_files = None
    
    def _run_validation(self):

        self._logger.log('Starting training files validation')
        training_files_validation = Validate(self._logger,self._training_file_path,self._schema_path)
        validation_result,path_to_good_files,path_to_bad_files = training_files_validation.validate_files()
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
        all_files = [file for file in os.listdir(self._path_to_good_files)]
        data_to_clean = dd.read_csv(os.path.join(self._path_to_good_files,'*.csv'))
        # st.write(data_to_clean.count().compute())
        unnecessary_columns = ['TSH_measured','T3_measured','TT4_measured','T4U_measured','FTI_measured','TBG_measured','TBG','TSH']
        st.write(Preprocessor(self._logger,unnecessary_columns).transform(data_to_clean.compute()))

    def start_training(self):
        
        # bar = st.progress(0)
        with st.spinner('Validating files now, please wait.....'):
        # Validation
            validation_result = self._run_validation()

        # Read Data from all files in Good Folder and run preprocessing
        with st.spinner('Preprocessing Data now, please wait....'):
            self._preprocess_data()
        # Save data to DB

        # Move files to good/bad folders after validation




        # bar.progress(100)




# train = Training('.\data\Training_Batch_Files','.\data\schema\schema_training.json')
# train.start_training()