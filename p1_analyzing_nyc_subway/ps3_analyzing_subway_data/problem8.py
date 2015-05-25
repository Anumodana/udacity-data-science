# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import scipy
import statsmodels.api as sm

def predictions(weather_turnstile):
    y = weather_turnstile['ENTRIESn_hourly']

    dummy_units = pd.get_dummies(weather_turnstile['UNIT'], prefix='unit')
    x = weather_turnstile[['rain', 'Hour', 'meantempi', 'meanpressurei', 'meanwindspdi']].join(dummy_units)

    x = sm.add_constant(x)
    model = sm.OLS(y, x)
    results = model.fit()

    return results.predict()
