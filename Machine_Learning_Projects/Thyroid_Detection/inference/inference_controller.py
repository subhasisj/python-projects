import sys
sys.path.append('../')
from logger.logger import Logger
from db_operations.sqlite_db import SqliteDbHandler

class Inference_Controller:
    def __init__(self,inference_file_path):

