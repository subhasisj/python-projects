import sys
sys.path.append('../')
from logger.logger import Logger
from training.clustering import KmeansClustering
import pandas as pd
import unittest
from db_operations.sqlite_db import SqliteDbHandler


class TestClustering(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     connection = SqliteDbHandler(Logger('test.log'),'.','test').create_db_connection()
    #     df = pd.read_sql("select * from thyroid_training", cls.connection)
    #     print(df.dtypes)
    #     cls.clustering = KmeansClustering(Logger('test.log'),df)

    def setUp(self):
        logger = Logger('test.log')
        self.connection = SqliteDbHandler(logger,'.','test').create_db_connection()
        self.df = pd.read_sql("select * from thyroid_training", self.connection)
        self.clustering = KmeansClustering(logger,self.df)


    def test_num_clusters(self):

        n_clusters = self.clustering.find_clusters_using_elbow_plot()
        print(n_clusters)
        self.assertIsNotNone(n_clusters)


if __name__ == '__main__':
    unittest.main()