import sys
sys.path.append('../')
from logger.logger import Logger
from validation.validate import Validate
import streamlit as st

class Training:
    def __init__(self,training_file_path,schema_path):
        self._training_file_path = training_file_path
        self._schema_path = schema_path
        self._logger = Logger('training_logs.log')
        self
    
    def _run_validation(self):

        self._logger.log('Starting training files validation')
        training_files_validation = Validate(self._logger,self._training_file_path,self._schema_path)
        validation_result,path_to_good_files,path_to_bad_files = training_files_validation.validate_files()
        self._logger.log('Training Files Validaiton Completed.') #
        st.info('Validation Results:')
        st.write(validation_result)
        st.info('Path to Good Files:')
        st.write(path_to_good_files)
        st.info('Path to Bad Files:')
        st.write(path_to_bad_files)

        return validation_result

    def start_training(self):
        
        bar = st.progress(0)
        
        # Validation
        validation_result = self._run_validation()

        # Move files to good/bad folders after validation




        bar.progress(100)




# train = Training('.\data\Training_Batch_Files','.\data\schema\schema_training.json')
# train.start_training()