import sys
sys.path.append('./')
from inference.inference_controller import Inference_Controller
import unittest
import os
import more_itertools
from joblib import load

class DummyLogger:
    def __init__(self):
        pass

    def log(self, log_message,level='info'):
        print(log_message)

class TestInferenceController(unittest.TestCase):

    def setUp(self):
        logger = DummyLogger()
        current_cwd = os.getcwd()
        db_path = os.path.join(current_cwd,'tests','inferencing_DB')
        preprocessor = load(os.path.join(current_cwd,'tests','preprocessor.joblib'))
        self.inference_controller = Inference_Controller(db_path,preprocessor)

    def test_run_inference(self):
        self.inference_controller.run_inferencing()

if __name__ == '__main__':
    unittest.main()

