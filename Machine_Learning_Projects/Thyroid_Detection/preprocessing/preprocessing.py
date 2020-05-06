from sklearn.base import TransformerMixin,BaseEstimator
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import RandomOverSampler
import pandas as pd

class Preprocessor(BaseEstimator,TransformerMixin):
    def __init__(self,logger,unnecessary_columns_list):
        self._logger = logger
        self._unnecessary_columns_list = unnecessary_columns_list
        self._label_encoder = None

    def fit(self, df,y=None):
        return self 

    def transform(self,df,y=None):
        self._logger.log(f'Preprocessor: Dropping columns: {self._unnecessary_columns_list}')
        df = self._drop_unnecessary_columns(df)

        self._logger.log('Preprocessor: Replacing "?" with NaN')
        df = self._replace_invalid_values_with_null(df)

        self._logger.log('Preprocessor: Encoding Categorical columns')
        df = self._encode_categorical_variable(df)

        self._logger.log('Preprocessor: Imputing missing values')
        df = self._impute_missing_values(df)

        return df

    def _drop_unnecessary_columns(self,df):
        df = df.drop(self._unnecessary_columns_list,axis=1)
        return df
    
    def _replace_invalid_values_with_null(self,df):
        for column in df.columns:
            count = df[column][df[column] == '?'].count()
            if count != 0:
                df[column] = df[column].replace('?', np.nan)
        return df

    def _encode_categorical_variable(self,df):
        # We can map the categorical values like below:
        df['sex'] = df['sex'].map({'F': 0, 'M': 1})

        # except for 'Sex' column all the other columns with two categorical data have same value 'f' and 't'.
        # so instead of mapping indvidually, let's do a smarter work
        for column in df.columns:
            if len(df[column].unique()) == 2:
                df[column] = df[column].map({'f': 0, 't': 1})

        # this will map all the rest of the columns as we require. Now there are handful of column left with more than 2 categories.
        # we will use get_dummies with that.
        df = pd.get_dummies(df,columns=['referral_source'])

        if self._label_encoder==None:
            encoder = LabelEncoder().fit(df['Class'])
            self._label_encoder = encoder
        else:
            #Get the existing encoder that was used on training data
            encoder = self._label_encoder 

        df['Class'] = encoder.transform(df['Class'])
        return df

    def _impute_missing_values(self,df):
        # check for missing values in columns
        null_present = False
        for i in df.isna().sum():
            if i>0:
                null_present=True
                break
        
        if null_present:
            self._logger.log('Preprocessor: missing values found.')
        
            # Impute Missing values
            try:
                imputer=KNNImputer(n_neighbors=3, weights='uniform',missing_values=np.nan)
                new_array=imputer.fit_transform(df)
                df = pd.DataFrame(data=np.round(self.new_array), columns=self.data.columns)
                self._logger.log('Preprocessor: Imputed Missing Successfully.')
                return df
            except Exception as e:
                self._logger.log(f'Preprocessor: Exception occured while Iimputing Exception message: {str(e)}','critical')
                raise Exception()
    

