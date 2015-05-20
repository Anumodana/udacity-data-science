import pandas
import pandasql


def num_rainy_days(filename):
    weather_data = pandas.read_csv(filename)

    q = """
    select count(*)
    from weather_data
    where rain = 1
    group by rain;
    """
    
    rainy_days = pandasql.sqldf(q.lower(), locals())
    return rainy_days
    