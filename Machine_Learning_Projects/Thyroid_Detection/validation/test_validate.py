class test_validate(object):
    def __init__(self,logger):
        self._logger = logger

    def write(self):
        self._logger.log('Writing from test_validate')