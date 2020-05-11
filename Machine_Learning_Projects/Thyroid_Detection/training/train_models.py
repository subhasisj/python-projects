
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from multiprocessing import Pool
import multiprocessing as mp
from sklearn.metrics  import roc_auc_score,accuracy_score
import pandas as pd 
import sqlite3
from functools import partial
import itertools
from sklearn.model_selection import RandomizedSearchCV
from datetime import datetime
import logging
import jsonpickle


from joblib import Parallel, delayed

import numpy as np
np.random.seed = 20

class Train_Models:

    def __init__(self,logger,data):
        self._logger = logger
        self._data = data
        self._classifiers =[RandomForestClassifier(),KNeighborsClassifier()]#XGBClassifier()

    def _run_model_sequential(self):
        self._logger.log('Models: fitting Algorithms Sequentially')
        metrics_seq = pd.DataFrame()
        model_evaluator = Model_Evaluator(self._logger,self.X,self.y)
        metrics_dict = {}
        for clf in self._classifiers:
            metrics_seq = pd.concat([metrics_seq,model_evaluator.evaluate_models(clf)])
            # metrics_dict.update(model_evaluator.evaluate_models(clf))
        all_algo_metrics = metrics_seq.sort_values('score',ascending=False).reset_index(drop=True)
        return all_algo_metrics.loc[0]['algo']

    def _run_model_multiprocessing(self):
        self._logger.log('Models: fitting Algorithms in Parallel')

        try:
            self.pool = mp.Pool(mp.cpu_count())
            # all_algo_metrics = pd.concat(self.pool.map(partial(self._evaluate_models,X=X,y=y), self._classifiers))
            model_evaluator = Model_Evaluator(self._logger)
            all_algo_metrics = pd.concat(self.pool.map(partial(model_evaluator.evaluate_models,X=self.X,y=self.y), self._classifiers))
            # self.pool.join()
            self.pool.close()
            all_algo_metrics = all_algo_metrics.sort_values('score',ascending=False).reset_index(drop=True)
        except Exception as e:
            self._logger.log(f'Models: Exception occured while running in Parallel : {str(e)}','critical')
            self.pool.close()
        return all_algo_metrics.loc[0]['algo']

    def _run_model_joblib_parallel(self):

        try:
            self._logger.log('Models: fitting Algorithms using Joblib Parallel')
            model_evaluator = Model_Evaluator(self._logger,self.X,self.y)
            all_algo_metrics = pd.concat(Parallel(n_jobs=-1)(delayed(model_evaluator.evaluate_models) (clf) for clf in self._classifiers))
            # all_algo_metrics_dict = Parallel(n_jobs=1)(delayed(model_evaluator.evaluate_models) (clf) for clf in self._classifiers)
            all_algo_metrics = all_algo_metrics.sort_values('score',ascending=False).reset_index(drop=True)
            return all_algo_metrics.loc[0]['algo']
        except Exception as e:
            self._logger.log(f'Models: Exception occured while running in Joblib Parallel : {str(e)}','critical')

    def find_best_classifier_for_data(self):

        self._logger.log('Models: Intiliazing process for finding best model')
        self.X = self._data.drop('label',axis=1)
        self.y = self._data['label']

        return self._run_model_joblib_parallel()
        # return self._run_model_sequential()


        


class Model_Evaluator:

    def __init__(self,logger,X,y):
        self._logger = logger
        self._classifiers = [RandomForestClassifier(),KNeighborsClassifier()]#XGBClassifier()
        self.X =X
        self.y =y
        self.params = {
                    'XGBClassifier':{

                                    'max_depth':[3,5,7,9,12,15,25],
                                    'n_estimators': [10, 50, 100, 200],
                                    'learning_rate': [0.5, 0.1, 0.01, 0.001],
                                    'min_child_weight':[1,3,5,7]
                                    },

                    'RandomForestClassifier':{
                                    "n_estimators": [10, 50, 100, 130],
                                    "criterion": ['gini', 'entropy'],
                                    "max_depth": range(2, 4, 1),
                                    "max_features": ['auto', 'log2']
                                    },

                    'KNeighborsClassifier':{
                                    "algorithm" : ['ball_tree', 'kd_tree', 'brute'],
                                    "leaf_size" : [10,17,24,28,30,35],
                                    "n_neighbors":[4,5,8,10,11],
                                    "p":[1,2]
                                }
                }
    
    def evaluate_models(self,classifier):
        # """TODO:
    # 1. Pass classifier and X_train,y_train for Random Search 
    # 2. Get Classifer instance from 1st step and perform scoring on test set
    # 3. Return Metrics DF
    # """
        X_train,X_test,y_train,y_test = train_test_split(self.X,self.y,test_size = 0.3)
        best_parameters_for_classifier = self._get_best_params_for_classifier(classifier, X_train,y_train)
        if classifier.__class__.__name__ == 'XGBClassifier':
            best_classifier = XGBClassifier(**best_parameters_for_classifier)
        elif classifier.__class__.__name__ == 'RandomForestClassifier':
            best_classifier = RandomForestClassifier(**best_parameters_for_classifier)
        elif classifier.__class__.__name__ == 'KNeighborsClassifier':
            best_classifier = KNeighborsClassifier(**best_parameters_for_classifier)


        best_classifier.fit(X_train,y_train)
        y_pred = best_classifier.predict_proba(X_test)
        if len(y_test.unique()) == 1:
            score = accuracy_score(y_test,y_pred)
        else:
            score =  roc_auc_score(y_test, y_pred, multi_class='ovr')
        
        metric = {
            # 'algo':classifier.__class__.__name__,
            'algo':jsonpickle.encode(best_classifier),# Serialize Classifier
            'score':float(score)
            }
        self._logger.log(f'Models: Evaluating {best_classifier.__class__.__name__} -- Score: {score}')

        metrics_df = pd.DataFrame(metric,index=[0])
        return metrics_df

    def _get_best_params_for_classifier(self, classifier,X,y):
        # """TODO:
        # 1. Get classifier and X_train ,y_train 
        # 2. Fetch parameter grid from Params dict according to Classifier 
        # 3. Run Random Search CV and get best params for classifier
        # 4. Construct the classifier with these parameters and fit the training data 
        # 5. Return Classifier
        # """
        start = datetime.now()
        self._logger.log(f'Models: RandomizedSearchCV for {classifier.__class__.__name__} started at {start}')
        random_searchcv = RandomizedSearchCV(classifier,
                                             param_distributions=self.params.get(classifier.__class__.__name__),
                                             n_jobs=-1,
                                             cv=5)
        random_searchcv.fit(X,y)
        self._logger.log(f'Models: RandomizedSearchCV for {classifier.__class__.__name__} Params :{random_searchcv.best_params_} ')
        self._logger.log(f'Models: RandomizedSearchCV for {classifier.__class__.__name__} finished in {datetime.now()- start} seconds')

        return random_searchcv.best_params_









