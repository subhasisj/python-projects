import sys
sys.path.append('../')
from utilities.utils import ModelUtils
from logger.logger import Logger
from db_operations.sqlite_db import SqliteDbHandler
import os
from joblib import dump, load
from datetime import datetime
import more_itertools
import streamlit as st



class Inference_Controller:
    def __init__(self,inference_db_path):
        self._inference_db_path = inference_db_path
        self._time_created = datetime.now()
        self._logger = Logger(f'inferencing_logs_{self._time_created.date()}_{self._time_created.strftime("%H%M%S")}.log')
        self._db_handler = SqliteDbHandler(self._logger,self._inference_db_path,'inferencing_db')
        self._model_utils = ModelUtils(self._logger)

    def _load_data(self):
        self._logger.log('Inference: Started Inferencing')
        self._logger.log('Inference: Loading data for Inferencing')
        try:    
            self._db_handler.create_db_connection()
            df = self._db_handler.get_data_from_db('thyroid_inferencing')
            return df
        except Exception as e:
            self._logger.log(f'Inference: Exception occured while Loading data for Inferencing, {str(e)}')

    def _cluster_data(self,df):

        clustering_model_name_with_extension = self._all_models[0]
        model_name_only = clustering_model_name_with_extension.split('.')[0]
        clustering_model = self._model_utils.load_model(model_name_only)
        
        clusters = clustering_model.predict(df)
        df['clusters']=clusters
        self._clusters=df['clusters'].unique()

        return df


    def run_inferencing(self):
        with st.spinner("Loading validated data from DB..."):
            df = self._load_data()

        with st.spinner("Loading models from repository..."):
            self._all_models = list(more_itertools.flatten(self._model_utils.get_all_models_info()))

        with st.spinner('Clustering data'):
            st.info('Clustered data')
            df = self._cluster_data(df)
            st.write(df)





        
      






