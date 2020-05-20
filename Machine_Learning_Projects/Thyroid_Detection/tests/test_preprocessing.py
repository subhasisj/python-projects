import sys
sys.path.append('../')
from preprocessing.preprocessing import Preprocessor
import pandas as pd
import unittest
from db_operations.sqlite_db import SqliteDbHandler
import os

class DummyLogger:
    def __init__(self,logfile):
        pass

    def log(self, log_message,level='info'):
        pass


class TestPreprocessor(unittest.TestCase):
    def setUp(self):
        logger = DummyLogger('test_preprocessing.log')
        self.connection = SqliteDbHandler(logger,'.','training_db').create_db_connection()
        
        self.unnecessary_columns = ['TSH_measured','T3_measured','TT4_measured','T4U_measured','FTI_measured','TBG_measured','TBG','TSH']
        self.preprocessing = Preprocessor(logger,self.unnecessary_columns)
    
    def test_preprocessing(self):
        print(os.getcwd())
        df = pd.read_csv('./tests/InputFile.csv')
        print(df.shape)
        self.preprocessing.transform(df)



if __name__ == '__main__':
    unittest.main()