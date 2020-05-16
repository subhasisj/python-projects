import sys
sys.path.append('../')
from logger.logger import Logger
import os
import shutil
from joblib import load

# createDirectoryForGoodBadRawData
# deleteExistingBadDataTrainingFolder
# moveBadFilesToArchiveBad

# TODO: """"
# 1. Create directory
# 2. Move files utility source-->destination
# 4. Delete Directory
# """

class FileUtils:
    def __init__(self,logger,base_path_for_files):
        self._logger = logger
        self._base_path_for_files = base_path_for_files

    def create(self,sub_directory_to_create,delete_before_creation=None):
        try:
            if delete_before_creation:
                self.delete_directory(sub_directory_to_create)
            path = os.path.join(self._base_path_for_files,sub_directory_to_create)
            if not os.path.isdir(path):
                os.makedirs(path)
                self._logger.log(f'New Path Created {path}')
            else:
                self._logger.log(f'Requested Path {path} already exists!')
            return path
        except OSError as ex:
            self._logger.log(f'File Error while trying to create {sub_directory_to_create} under {self._base_path_for_files}','critical')

    def move_files(self,filename, destination_directory):
        try:
            if filename != '.gitignore':
                source_file_path = os.path.join(self._base_path_for_files,filename)
                destination_file_path = os.path.join(destination_directory,filename)
                if os.path.isfile(source_file_path):
                    shutil.copy(source_file_path, destination_file_path)
                    self._logger.log(f'File {filename} successfully moved from {source_file_path} to {destination_file_path}')
                else:
                    self._logger.log(f'{filename} is not a file. Move operation failed from {source_file_path} to {destination_file_path}','warning')

        except :
            self._logger.log(f'File {filename} move from {source_file_path} to {destination_file_path} Failed','critical')
            raise OSError

    def delete_directory(self, foldername):
        try:
            path = os.path.join(self._base_path_for_files,foldername)
            if os.path.isdir(path):
                shutil.rmtree(path)
                self._logger.log(f'File path {path} successfully removed')
            else:
                self._logger.log(f'Requested Path {path} does not exist!','warning')
        except:
            self._logger.log(f'File path {path} removal unsuccessful','critical')


class ModelUtils:
    def __init__(self,logger):
        self._logger = logger
        self.path = os.path.join('.','artifacts','models')

    def load_model(self,model_name):
        try:
            model_path = os.path.join(self.path,model_name,f'{model_name}.joblib')
            self._logger.log(f'Model Loader: Loading model {model_name} from path {model_path}')
            return load(model_path)
        except Exception as e:
            self._logger.log(f'Model Loader: Unable to load model {model_name} from path {model_path}, Exception : {str(e)}')

    def get_all_models_info(self):
        
        models = []
        for _ ,_ ,file in os.walk(self.path):
            if len(file) != 0:
                models.append(file)

        return models





# test_base_path = os.path.join('.','utilities')
# test_dest_path = os.path.join('.','utilities','test_dir2')
# print(test_base_path)
# utils = FileUtils(Logger('filelog.log'),test_base_path)
# # utils.move_files('abc.txt',test_dest_path)
# # utils.create('test_dir')
# utils.delete_directory('test_dir2')