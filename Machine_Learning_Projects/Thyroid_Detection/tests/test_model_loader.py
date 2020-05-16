import sys
sys.path.append('../')
from utilities.utils import ModelUtils
import unittest
import os
import more_itertools

class DummyLogger:
    def __init__(self):
        pass

    def log(self, log_message,level='info'):
        print(log_message)


class TestModelUtils(unittest.TestCase):

    def setUp(self):
        logger = DummyLogger()
        self.model_utils = ModelUtils(logger)
        self.actual_models = os.listdir(os.path.join('.','artifacts','models'))


    def test_model_loader(self):

        actual_model_name = self.actual_models[0]
        loaded_model = self.model_utils.load_model(actual_model_name)
        self.assertEqual(actual_model_name, loaded_model.__class__.__name__)
    
    def test_get_all_models(self):
        
        all_models = self.model_utils.get_all_models_info()
        self.assertEqual(len(all_models),len(self.actual_models))

    def test_get_one_model_name(self):
        all_models = self.model_utils.get_all_models_info()
        all_models = list(more_itertools.flatten(all_models))
        model_0_name_with_extension = all_models[0]
        model_name_only = model_0_name_with_extension.split('.')[0]
        
        self.assertEqual(model_name_only,self.actual_models[0])


if __name__ == '__main__':
    unittest.main()