import sqlite3
import os
import pandas as pd

class SqliteDbHandler:
    def __init__(self,logger,path=None,dbname=None):
        self._logger = logger
        self._path = path
        self._dbname = dbname
        self._connection =None
    
    def create_db_connection(self,db_path=None):
        """
        Create a DB or Get connection to existing DB
        
        """
        try:
            if db_path:
                db_name_with_path = db_path
            else:
                db_name_with_path = os.path.join(self._path,self._dbname)+'.db'

            self._logger.log(f'DB: Attempting to get database connection to {db_name_with_path}')
            conn = sqlite3.connect(db_name_with_path)
            self._connection = conn
            self._logger.log(f'DB: Opened Connection to the DB {db_name_with_path} successfully')
            # return self._connection
        except Exception as e:
            self._logger.log(f'Error while connecting to database: {db_name_with_path}, error: {e}','critical')
            raise ConnectionError

    def save_table_in_db(self,table_name,data):
        """
        TODO:
        Save the table in the database, if the records exist in the table already exists
        then replace them else create a new entry
        This makes it useful for retraining of the models as we want to train the 
        model on both old and new data
        """
        try:
            self._logger.log(f'DB :Saving table {table_name} in database {self._dbname} ')
            c = self._connection.cursor()
            data.to_sql(table_name, self._connection,if_exists="replace",index=False)
            self._logger.log(f'DB :Saving table {table_name} in database {self._dbname} completed successfully')
            self._connection.close()
        except Exception as e:
            self._logger.log(f'Error while saving table {table_name} in Database {self._dbname}, error: {e}','critical')
            self._connection.close()

    def get_data_from_db(self,table_name):
        df = pd.read_sql(f"select * from {table_name}", self._connection)
        return df







