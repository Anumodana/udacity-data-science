# -*- coding: utf-8 -*-

import numpy as np
import pandas
import scipy
import statsmodels.api as sm

def predictions(weather_turnstile):
    y = weather_turnstile['ENTRIESn_hourly']
    x = weather_turnstile[['Hour', 'EXITSn_hourly', 'fog', 'rain', 'thunder']]
    x = sm.add_constant(x)
    model = sm.OLS(y, x)
    model_fit = model.fit()
    prediction = model_fit.predict()
    
    return prediction
