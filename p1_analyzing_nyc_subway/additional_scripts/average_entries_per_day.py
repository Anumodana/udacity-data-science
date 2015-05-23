from ggplot import * 
import pandas as pd
import pandasql

def average_entries_per_day():
    turnstile_weather = pd.read_csv('turnstile_data_master_with_weather.csv')
    turnstile_weather.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    turnstile_weather['day'] = pd.DatetimeIndex(turnstile_weather['daten']).weekday
    turnstile_weather['day'] = turnstile_weather['day'].map({
                                                                0: 'Monday',
                                                                1: 'Tuesday',
                                                                2: 'Wednesday',
                                                                3: 'Thursday',
                                                                4: 'Friday',
                                                                5: 'Saturday',
                                                                6: 'Sunday'
                                                            })

    q = '''
    select day, hour, avg(entriesn_hourly) as entries
    from turnstile_weather
    group by day, hour;
    '''
    return pandasql.sqldf(q.lower(), locals())

def plot_average_entries_per_day():
    avg_entries = average_entries_per_day()
    plot = ggplot(avg_entries, aes(x='hour', y='entries', color='day')) + \
            geom_point() + geom_line() + \
            ggtitle('Average Ridership by Day and Hour') + \
            xlab('Hour') + ylab('Number of Entries') + \
            xlim(0, 23) + ylim(0)
    print(plot)

plot_average_entries_per_day()