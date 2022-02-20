import yfinance as yf
import pandas as pd
import time
import datetime

dji = yf.Ticker("dji")
dji_historical = dji.history(start="2017-12-31", end="2022-01-02", interval="1d")

# print(dji_historical)

df = pd.DataFrame(dji_historical)

def convertDatetoTimestamp(date_string):
    return pd.Timestamp(date_string, unit='s').timestamp()

df = df.reset_index()
# df['Date'] = pd.to_datetime(df['Date']m)
df['Date'] = df['Date'].apply(convertDatetoTimestamp)


print(df)
df.to_csv('../data/dji.csv')

