import sys
sys.path.append('../')
from logger.logger import Logger
from db_operations.sqlite_db import SqliteDbHandler
import pandas as pd
import unittest


class TestConnection(unittest.TestCase):
    def setUp(self):
        self.sql_connection_handler = SqliteDbHandler(Logger('test.log'),'.','test')
        self.sql_connection_handler.create_db_connection()
        self.connection = self.sql_connection_handler._connection

    def test_get_connection(self):
        self.assertIsNotNone(self.sql_connection_handler._connection)

    def test_table_from_db(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            # df = pd.read_sql("select * from thyroid_training", self.connection)
            self.assertIsNotNone(tables)
            for table_name in tables:
                print(table_name[0])
            # df.head()
            df = pd.read_sql("select * from thyroid_training", self.connection)
            self.assertIsNotNone(df)
        except Exception as e:
            self.assertRaises(e)

        



if __name__ == '__main__':
    unittest.main()