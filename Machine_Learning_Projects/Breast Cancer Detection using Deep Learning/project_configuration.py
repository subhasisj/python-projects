import os

ORIGINAL_INPUT_DATASET = r'dataset\orig'
BASE_PATH_FOR_NEW_FILES = r'dataset\cleaned'

TRAIN_PATH = os.path.sep.join([BASE_PATH_FOR_NEW_FILES ,'training'])
VAL_PATH = os.path.sep.join([BASE_PATH_FOR_NEW_FILES ,'validation'])
TEST_PATH = os.path.sep.join([BASE_PATH_FOR_NEW_FILES ,'testing'])