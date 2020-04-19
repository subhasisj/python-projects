# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:52:19 2020

@author: I323570
"""

import pickle
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd

model = tf.keras.models.load_model('time_series_model_working.h5')
loaded_data = pickle.load(open('./train_data_for_LSTM_modek.pkl', 'rb'))

scaler = MinMaxScaler()

original_data = loaded_data.Global_active_power.values
original_data = original_data.reshape((-1,1))
scaler.fit(original_data)
original_data_scaled = scaler.transform(original_data)

look_back = 60
temp_prediction_list = original_data_scaled[-look_back:]
scaled_temp = temp_prediction_list.reshape(1,1,60)

scaler.inverse_transform(model.predict(scaled_temp)[0])

def predict(num_prediction, model):
    prediction_list = original_data_scaled[-look_back:]
    
    for _ in range(num_prediction):
        x = prediction_list[-look_back:]
        x = x.reshape((1, 1, look_back))
        out = model.predict(x)[0][0]
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[look_back-1:]
        
    return prediction_list
    
def predict_dates(num_prediction):
    last_date = loaded_data.index[-1]
    prediction_dates = pd.date_range(last_date,freq='H', periods=num_prediction+1).tolist()
    return prediction_dates

num_prediction = 100
forecast = predict(num_prediction, model)
forecast_dates = predict_dates(100)

scaled_forecasts = scaler.inverse_transform(forecast.reshape(-1,1))

df_forecast_values = pd.DataFrame({'dates':forecast_dates , 'forecast_values':scaled_forecasts[0][0]})
df_forecast_values.set_index('dates')
df_forecast_values.plot()
