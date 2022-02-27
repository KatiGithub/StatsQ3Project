import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn.feature_selection as sk

btc_dji_df = pd.read_csv('../data/btc_dji.csv')

price_dif_btc = []
price_dif_dji = []

for index, row in btc_dji_df.iterrows():
    price_dif_btc.append(row['btc_opening_price'] - row['btc_closing_price'])
    price_dif_dji.append(row['dji_opening_price'] - row['btc_closing_price'])

price_dif_btc = np.array(price_dif_btc)
price_dif_dji = np.array(price_dif_dji)

price_dif_dji = price_dif_dji.reshape(-1, 1)
price_dif_btc = price_dif_btc.reshape(-1, 1)

print(price_dif_btc)
print(price_dif_dji)

price_btc = np.array(btc_dji_df['btc_closing_price'])
price_dji = np.array(btc_dji_df['dji_closing_price'])

price_btc = price_btc.reshape(-1, 1)
price_dji = price_dji.reshape(-1, 1)

print(sk.r_regression(price_btc, price_dji))