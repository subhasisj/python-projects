import sys
sys.path.append('../')
from inference.inference_controller import Inference_Controller
import unittest
import os
import more_itertools

class DummyLogger:
    def __init__(self):
        pass

    def log(self, log_message,level='info'):
        print(log_message)

class TestInferenceController(unittest.TestCase):

    def setUp(self):
        logger = DummyLogger()
        current_cwd = os.getcwd()
        db_path = os.path.join('.','data','inferencing_DB')
        self.inference_controller = Inference_Controller(db_path)

    def test_run_inference(self):
        self.inference_controller.run_inferencing()

if __name__ == '__main__':
    unittest.main()

