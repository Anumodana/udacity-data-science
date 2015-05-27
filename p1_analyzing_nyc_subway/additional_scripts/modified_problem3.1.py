import numpy as np
import pandas
import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):
    plt.figure()

    df = turnstile_weather
    df['ENTRIESn_hourly'][df['rain']==0].hist(bins=260, alpha=0.6)
    df['ENTRIESn_hourly'][df['rain']==1].hist(bins=260, alpha=0.6)
    
    plt.title('Histogram of ENTRIESn_hourly')
    plt.legend(['No rain', 'Rain'])
    plt.xlabel('ENTRIESn_hourly')
    plt.ylabel('Frequency')
    plt.axis([0, 6000, 0, 45000])
    
    return plt
