from ggplot import * 
import pandas as pd
import pandasql

def average_entries_per_hour():
    turnstile_weather = pd.read_csv('turnstile_data_master_with_weather.csv')
    turnstile_weather.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True) 

    q = '''
    select hour, avg(entriesn_hourly) as entries
    from turnstile_weather
    group by hour;
    '''
    return pandasql.sqldf(q.lower(), locals())

def plot_average_entries_per_hour():
    entries_hour = average_entries_per_hour()
    plot = ggplot(entries_hour, aes('hour', 'entries')) + \
            geom_point(color='brown') + geom_line(color='brown') + \
            ggtitle('Average Ridership by Hour') + \
            xlab('Hour') + ylab('Number of Entries') + \
            xlim(0, 23) + ylim(0)
    print(plot)

plot_average_entries_per_hour()