from ggplot import * 
import pandas as pd
import pandasql

def plot_average_entries_by_hour():
    turnstile_weather = pd.read_csv("turnstile_data_master_with_weather.csv")
    turnstile_weather.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True) 
    
    q = """
    select hour, avg(entriesn_hourly) as entries
    from turnstile_weather
    group by hour;
    """
    entries_hour = pandasql.sqldf(q.lower(), locals())
    
    plot = ggplot(entries_hour, aes('hour', 'entries')) + \
            geom_point(color='red') + \
            geom_line(color='green') + ggtitle("Average Ridership by Hour") + \
            xlab("Hour") + ylab("Number of Entries") + \
            xlim(0) + ylim(0)
    print(plot)
    
plot_average_entries_by_hour()