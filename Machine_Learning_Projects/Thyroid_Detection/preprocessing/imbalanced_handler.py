from imblearn.over_sampling import RandomOverSampler
import pandas as pd

class ImbalancedHandler:
    def __init__(self,logger,data,label_column):
        self._logger = logger
        self._data = data
        self._label_column = label_column

    def handle(self):
        rdsmple = RandomOverSampler()
        y = self._data[(self._label_column)]
        X = self._data.drop(self._label_column,axis=1)

        self._logger.log(f'Balancing Classes : Processing column {self._label_column}')
        self._logger.log(f'Balancing Classes : Value Counts before sampling for {self._label_column}: {self._data[self._label_column].value_counts()}')
        X_sampled,y_sampled  = rdsmple.fit_sample(X,y)
        df = pd.concat([X_sampled,y_sampled], axis=1)
        self._logger.log(f'Balancing Classes : Value Counts after sampling for {self._label_column}: {df[self._label_column].value_counts()}')

        return df
