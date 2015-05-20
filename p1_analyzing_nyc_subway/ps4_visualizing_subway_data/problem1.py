from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    plot = ggplot(turnstile_weather, aes('Hour', 'EXITSn_hourly', color = 'DATEn')) + geom_point() + geom_line()
    return plot

