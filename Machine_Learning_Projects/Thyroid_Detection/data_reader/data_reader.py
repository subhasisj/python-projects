import dask.dataframe as dd
import os
import pandas as pd
import glob

class DaskDataReader:
    def __init__(self,logger,path_to_good_files):
        self._logger = logger
        self._path = path_to_good_files
        
    def read(self):
        df = dd.read_csv(os.path.join(self._path,'*.csv'))
        return df


class GlobDataReader:
    def __init__(self,logger,path_to_good_files):
        self._logger = logger
        self._path = path_to_good_files

    def read(self):
        all_files = glob.glob(os.path.join(self._path,'*.csv'))
        df = pd.concat([pd.read_csv(f) for f in all_files],ignore_index =True)
        return df    