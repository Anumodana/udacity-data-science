import numpy as np
import scipy
import scipy.stats
import pandas

def mann_whitney_plus_means(turnstile_weather):
    rain = turnstile_weather[turnstile_weather['rain']==1]['ENTRIESn_hourly']
    not_rain = turnstile_weather[turnstile_weather['rain']==0]['ENTRIESn_hourly']
    with_rain_mean = np.mean(rain)
    without_rain_mean = np.mean(not_rain)
    U, p = scipy.stats.mannwhitneyu(rain, not_rain)
    
    return with_rain_mean, without_rain_mean, U, p
