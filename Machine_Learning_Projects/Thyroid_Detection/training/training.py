import sys
sys.path.append('../')
from utilities.utils import FileUtils
from training.clustering import KmeansClustering
from training.train_models import Train_Models
from logger.logger import Logger
from db_operations.sqlite_db import SqliteDbHandler
from datetime import datetime
import pandas as pd
import os
import streamlit as st
import jsonpickle
from joblib import dump, load



class Training:
    def __init__(self,training_db_path):
        self._training_db_path = training_db_path
        self._time_created = datetime.now()
        self._logger = Logger(f'training_logs_{self._time_created.date()}_{self._time_created.strftime("%H%M%S")}.log')
        date = self._time_created.date()
        time = self._time_created.strftime("%H%M%S")
        # self._db_handler = SqliteDbHandler(self._logger,self._training_db_path,f'training_db_{date}_{time}')
        self._db_handler = SqliteDbHandler(self._logger,self._training_db_path,f'training_db')
        self._cluster_controller = None
        self._path_to_artifacts = os.path.join('.','artifacts')
        fileutils = FileUtils(self._logger,self._path_to_artifacts)
        self.model_repo_path = fileutils.create('models',delete_before_creation=True)


    def begin_training(self):

        self._logger.log('Training: Begin....')
        self._logger.log(f'Training: Attempting to get training data from {self._training_db_path}.')
        self._db_handler.create_db_connection(self._training_db_path)

        with st.spinner('Collecting training data from DB....'):
            df = self._db_handler.get_data_from_db('thyroid_training')
            st.info('Training data loaded successfully')
            self._logger.log('Training: data loaded successfully.')

        with st.spinner('Begin Clustering of data..'):
            X = df.drop('Class',axis=1)
            y = df['Class']
            clusters = self._get_clusters_from_data(X)
            st.info(f'Found {clusters} clusters in training data')

            self._logger.log(f'Training: Found {clusters} clusters in training data')
            
        with st.spinner('Assigning Clusters to Training Data:'):
            df = self._assign_clusters_to_data(X)
            df['label'] = y
            st.write({
                'Clustering Model':self._cluster_controller.cluster_model.__class__.__name__,
                'Model Save path':self._cluster_model_save_path
            })
                # st.write(df.head())
                # df.to_csv('./data/test_pycaret_classification.csv')
        with st.spinner('Getting best model for each cluster'):
            self._logger.log(f'Training: Starting Process for getting best model for clusters ')
            st.info('Saved Models Overview:')
            st.write(self._train_models_for_clusters(df))


    def _get_clusters_from_data(self,data):

        self._cluster_controller = KmeansClustering(self._logger,data)
        return self._cluster_controller.find_clusters_using_elbow_plot()

    def _assign_clusters_to_data(self,data):

        data = self._cluster_controller.assign_clusters_to_data(data)

        model_name = self._cluster_controller.cluster_model.__class__.__name__
        file_utils = FileUtils(self._logger,self.model_repo_path)
        model_path = file_utils.create(model_name)
        self._cluster_model_save_path = os.path.join(model_path,f'{model_name}.joblib')
        try:
            dump(self._cluster_controller.cluster_model,self._cluster_model_save_path )
        except Exception as e:
            self._logger.log(f'Training: Exception occured while saving {self._cluster_model_save_path}, Exception : {str(e)}')

        return data

    def _train_models_for_clusters(self,data):

        cluster_models = {}
        # Loop at each Cluster and find best model/HP combination
        for group_name, df_group in data.groupby('Cluster'):
            self._logger.log(f'Training: Finding best model for Cluster: {group_name}')
            model_trainer = Train_Models(self._logger,df_group)
            cluster_models[group_name] = model_trainer.find_best_classifier_for_data()

        
        # fileutils = FileUtils(self._logger,self._path_to_artifacts)
        # model_repo_path = fileutils.create('models',delete_before_creation=True)
        # Save Models as per the cluster 
        # 
        saved_models = [] 
        for key, value in cluster_models.items():
            
            saved_model = {}

            model = jsonpickle.decode(value)
            model_name = model.__class__.__name__+str(key)

            model_utils = FileUtils(self._logger,self.model_repo_path)
            model_path = model_utils.create(model_name)


            try:
                model_save_path = os.path.join(model_path,f'{model_name}.joblib')
                dump(model,model_save_path )

                saved_model.update(Path = model_save_path )
                saved_model.update(Cluster = key)
                saved_model.update(model = model.__class__.__name__)
                saved_models.append(saved_model)

                self._logger.log(f'Saving Model {model_name} in {model_path}')

            except Exception as e:
                self._logger.log(f'Exception occured while saving Model {model_name} in {self.model_repo_path}: {str(e)}')
        
        
        return saved_models
        



    