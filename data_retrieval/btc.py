from calendar import calendar
import ccxt
import pandas as pd
import datetime as dt

pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 1000)

exchange_binance = ccxt.binance()
interval = '1d'
since='2018-01-01T00:00:00Z'
market_symbol = 'BTC/USDT'

header = ['timestamp', 'open', 'high', 'low', 'close', 'volume']

periodRetrieval =  exchange_binance.parse8601(since)
print(periodRetrieval)

data = []

current_time = dt.datetime.timestamp(dt.datetime.now()) * 1000
previous_periodRetrieval = periodRetrieval
if exchange_binance.has['fetchOHLCV']:
    while(periodRetrieval < current_time):
        current_data = exchange_binance.fetchOHLCV(market_symbol, interval, periodRetrieval, 1000)

        periodRetrieval = current_data[-1][0]
        
        if previous_periodRetrieval == periodRetrieval:
            data.pop()
            break

        try:
            data.index(0)
        except ValueError:
            data.extend(current_data)

        previous_periodRetrieval = periodRetrieval

df = pd.DataFrame(data, columns=header)
df = df.rename(columns={'timestamp': 'Date'})
df.to_csv('../data/btc.csv')