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

    def start_training(self):
        # validation
        self._logger.log('Starting training files validation')
        training_files_validation = Validate(self._logger,self._training_file_path,self._schema_path)
        validation_result = training_files_validation.validate_files()
        st.info('Validation Results:')
        st.write(validation_result)



# train = Training('.\data\Training_Batch_Files','.\data\schema\schema_training.json')
# train.start_training()