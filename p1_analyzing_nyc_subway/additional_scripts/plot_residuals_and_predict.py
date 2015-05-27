# -*- coding: utf-8 -*-

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def predictions(weather_turnstile):
    y = weather_turnstile['ENTRIESn_hourly']

    dummy_units = pd.get_dummies(weather_turnstile['UNIT'], prefix='unit')
    x = weather_turnstile[['rain', 'Hour', 'meantempi', 'meanpressurei', 'meanwindspdi']].join(dummy_units)

    x = sm.add_constant(x)
    model = sm.OLS(y, x)
    model_fitted = model.fit()

    plot_residuals_histogram(model_fitted.res)

    predict = model_fitted.predict()
    plot(y - predict, 'Residuals')

    return predict

def plot_residuals_histogram(res):
    res.hist(bins=150, color='orange')
    plt.title('Histogram of Residuals')
    plt.xlabel('Residuals')
    plt.ylabel('Frequency')
    plt.show()

def plot(res, ylabel):
	plt.plot(res)
    plt.xlabel('Index')
    plt.ylabel(ylabel)
    plt.show()


weather_turnstile = pd.read_csv('turnstile_data_master_with_weather.csv')
predictions(weather_turnstile)