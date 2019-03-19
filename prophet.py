# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from fbprophet import Prophet
 
 
fname="E:\\StockData\\VNINDEX.csv"
data = pd.read_csv (fname)
data.columns = ['ds', 'y']
model = Prophet() #instantiate Prophet
model.fit(data); #fit the model with your dataframe
 
future_stock_data = model.make_future_dataframe(periods=252, freq = 'd')
forecast_data = model.predict(future_stock_data)
 
print ("Forecast data")
print (forecast_data[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(12))
     
model.plot(forecast_data)
model.plot_components(forecast_data)