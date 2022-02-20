import matplotlib.pyplot as plt
import pandas as pd

btc_df = pd.read_csv('./data/btc.csv')
dji_df = pd.read_csv('./data/dji.csv')

btc_dji_df = pd.DataFrame({
    'Date': [],
    'btc_closing_price': [],
    'btc_opening_price': [],
    'dji_closing_price': [],
    'dji_opening_price': []
})

btc_df["Date"] = btc_df["Date"].apply(lambda x: x / 1000)
# print(btc_df)
# print(dji_df)

for date in btc_df["Date"]:
    if date in dji_df["Date"]:
        index_date_dji = dji_df["Date"].index.tolist().index(date)
        index_date_btc = btc_df["Date"].index.tolist().index(date)

        btc_dji_df = pd.concat([date, 
                                btc_df["close"][index_date_btc],
                                btc_df["open"][index_date_btc],
                                dji_df["Close"][index_date_dji],
                                dji_df["Open"][index_date_dji]],
                                
                                columns=["Date", "btc_closing_price", "btc_opening_price", "dji_closing_price", "dji_opening_price"])

        

# btc_dji_df = pd.merge(btc_df, dji_df, how='outer', on=["Date"])
print(btc_dji_df)

# plt.plot(btc_df["high"], dji_df["High"])
# plt.show()