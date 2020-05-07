import sys
sys.path.append('../')
from logger.logger import Logger
from db_operations.sqlite_db import SqliteDbHandler
from datetime import datetime
import pandas as pd
import streamlit as st

class Training:
    def __init__(self,training_db_path,preprocessor_path):
        self._training_db_path = training_db_path
        self._preprocessor_path = preprocessor_path
        self._time_created = datetime.now()
        self._logger = Logger(f'training_logs_{self._time_created.date()}_{self._time_created.strftime("%H%M%S")}.log')


    def begin_training(self):
        self._logger.log('Training: Begin....')
        self._logger.log(f'Training: Attempting to get training data from {self._training_db_path}.')
        connection = self._get_data_from_db()
        st.write(connection)
        # df = pd.read_sql_query("select * from thyroid_training;", connection)
        df = pd.read_sql("select * from thyroid_training", connection)
        self._logger.log('Training data loaded successfully.')
        st.write(df)


    def _get_data_from_db(self):
        date = self._time_created.date()
        time = self._time_created.strftime("%H%M%S")
        db_handler = SqliteDbHandler(self._logger,self._training_db_path,f'training_db_{date}_{time}')
        connection = db_handler.create_db_connection(self._training_db_path)
        return connection


    def _get_saved_preprocessor(self):
        pass

    def _cluster_data(self):
        pass