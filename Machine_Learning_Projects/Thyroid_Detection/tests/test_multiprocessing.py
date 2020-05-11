import sys
sys.path.append('../')
from training.train_models import Model_Evaluator
import time
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from multiprocessing import Pool
import multiprocessing as mp
from sklearn.metrics  import roc_auc_score,accuracy_score
import pandas as pd 
import sqlite3
from functools import partial
import numpy as np
import itertools
np.random.seed = 20



def evaluate_models2(classifier,X,y):
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3)
    classifier.fit(X_train,y_train)
    y_pred = classifier.predict_proba(X_test)
    if len(y_test.unique()) == 1:
        print(f'Classes in y_test:{len(y_test.unique())}')
        score = accuracy_score(y_test,y_pred)
    else:
        print(f'Classes in y_test:{len(y_test.unique())}')
        score =  roc_auc_score(y_test, y_pred, multi_class='ovr')
    
    metric = {
        'algo':classifier.__class__.__name__,
        'score':float(score)
        }

    print(metric)
    metrics_df = pd.DataFrame(metric,index=[0])

    return metrics_df

def run_evaluation():
    classifiers = [XGBClassifier(),RandomForestClassifier(),KNeighborsClassifier()]
    df = pd.read_csv('../data/test_pycaret_classification.csv')
    df_cluster_1 = df[df.Cluster==1]
    X = df_cluster_1.drop('label',axis=1)
    y= df_cluster_1['label']
    starttime = time.time()
    pool = mp.Pool(mp.cpu_count())

    # https://stackoverflow.com/questions/5442910/python-multiprocessing-pool-map-for-multiple-arguments
    # https://towardsdatascience.com/a-hands-on-guide-to-multiprocessing-in-python-48b59bfcc89e
    all_algo_metrics = pd.concat(pool.map(partial(evaluate_models2,X=X,y=y), classifiers))
    pool.close()
    print('That took {} seconds in Parallel'.format(time.time() - starttime))
    print(all_algo_metrics)
    print(f'best algo:{all_algo_metrics.loc[0]}')

    starttime = time.time()
    metrics_seq = pd.DataFrame()
    for clf in classifiers:
        metrics_seq = pd.concat([metrics_seq,evaluate_models2(clf, X=X, y=y)])
    print('That took {} seconds in Single Process'.format(time.time() - starttime))
    all_algo_metrics = all_algo_metrics.sort_values('score',ascending=False).reset_index(drop=True)
    
if __name__ == '__main__':
    
    # run_evaluation()
    classifiers = [XGBClassifier(),RandomForestClassifier(),KNeighborsClassifier()]
    df = pd.read_csv('../data/test_pycaret_classification.csv')
    df_cluster_1 = df[df.Cluster==1]
    X = df_cluster_1.drop('label',axis=1)
    y= df_cluster_1['label']
    starttime = time.time()
    pool = mp.Pool(mp.cpu_count())
    test_model = Model_Evaluator()
    all_algo_metrics = pd.concat(pool.map(partial(test_model._evaluate_models,X=X,y=y), classifiers))
    # pool.join()
    pool.close()