import pandas
import pandasql


def max_temp_aggregate_by_fog(filename):
    weather_data = pandas.read_csv(filename)

    q = """
    select fog, max(maxtempi)
    from weather_data
    group by fog;
    """
    
    foggy_days = pandasql.sqldf(q.lower(), locals())
    return foggy_days
