# -*- coding: utf-8 -*-

import numpy as np
import pandas
import scipy
import statsmodels.api as sm

def predictions(weather_turnstile):
    y = weather_turnstile['ENTRIESn_hourly']
    x = weather_turnstile[['rain', 'Hour', 'EXITSn_hourly']]
    x = sm.add_constant(x)
    model = sm.OLS(y, x)
    results = model.fit()
    
    return results.predict()
