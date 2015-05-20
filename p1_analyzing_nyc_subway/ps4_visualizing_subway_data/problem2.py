from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    plot = ggplot(turnstile_weather, aes('ENTRIESn_hourly', 'EXITSn_hourly', color='UNIT')) + geom_point(color='lightblue')
    return plot
