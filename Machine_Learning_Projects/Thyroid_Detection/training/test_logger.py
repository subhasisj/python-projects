import sys
sys.path.append('../')
from logger.logger import Logger
from validation.test_validate import test_validate
class TestLogger:
    def __init__(self):
        self._logger = Logger('testfile.log')

    def write(self):
        test_val = test_validate(self._logger)
        test_val.write()


# test = TestLogger()
# test.write()