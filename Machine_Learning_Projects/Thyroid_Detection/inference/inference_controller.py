import sys
sys.path.append('../')
from utilities.utils import ModelUtils
from logger.logger import Logger
from db_operations.sqlite_db import SqliteDbHandler
from utilities.utils import FileUtils
import os
from joblib import dump, load
from datetime import datetime
import more_itertools
import streamlit as st
import pandas as pd
import numpy as np



class Inference_Controller:
    def __init__(self,inference_db_path,preprocessor):
        self._inference_db_path = inference_db_path
        self._time_created = datetime.now()
        self._logger = Logger(f'inferencing_logs_{self._time_created.date()}_{self._time_created.strftime("%H%M%S")}.log')
        self._db_handler = SqliteDbHandler(self._logger,self._inference_db_path,'inferencing_db')
        self._model_utils = ModelUtils(self._logger)
        self._preprocessor = preprocessor

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
    
    def _get_model_for_clusters(self):
        
        model_repository = {}
        for cluster in self._clusters:
            model_repository[cluster]=self._model_utils.find_model_for_cluster(cluster)
        
        return model_repository

    def _get_label_encoder(self):
        return self._preprocessor.label_encoder

    def _make_predictions_for_clusters(self,df):

        label_encoder = self._get_label_encoder()
        all_models = self._get_model_for_clusters()

        final_predictions = pd.DataFrame()
        for cluster in self._clusters:
            current_cluster_data = df[df['clusters']==cluster]
            current_cluster_data = current_cluster_data.drop(['clusters'],axis=1)
            model = all_models.get(cluster)
            predicted_labels = model.predict(current_cluster_data)
            predicted_labels = predicted_labels.astype(int)
            predicted_labels = label_encoder.inverse_transform(predicted_labels)
            current_cluster_data['predictions'] = predicted_labels
            final_predictions = pd.concat([final_predictions,current_cluster_data])
        
        return final_predictions



    def run_inferencing(self):
        with st.spinner("Loading validated data from DB..."):
            df = self._load_data()

        with st.spinner("Loading models from repository..."):
            # self._all_models = list(more_itertools.flatten(self._model_utils.get_all_models_info()))
            self._all_models = self._model_utils.get_all_models_info()

        with st.spinner('Clustering data'):
            df = self._cluster_data(df)

        with st.spinner('Getting Predictions..'):
            st.info('Predictions:')
            final_predictions = self._make_predictions_for_clusters(df)
            st.write(final_predictions)

        with st.spinner('Writing Predictions to file..'):
            # file_utils = FileUtils(self._logger,os.path.join('.','data'))
            # predictions_save_path = file_utils.create('final_predictions',delete_before_creation=True)
            # predictions_save_path= os.path.join(predictions_save_path,'predictions.csv')
            final_predictions.to_csv('./data/final_predictions/predictions.csv',index=False)

