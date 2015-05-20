import pandas

def get_hourly_exits(df):
    df['EXITSn_hourly'] = (df.EXITSn - df.EXITSn.shift(1)).fillna(0)
    return df
