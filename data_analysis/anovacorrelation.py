import pandas as pd
import numpy as np
import sklearn.feature_selection as sk

btc_dji_df = pd.read_csv('../data/btc_dji.csv')

price_btc = np.array(btc_dji_df['btc_closing_price'])
price_dji = np.array(btc_dji_df['dji_closing_price'])

price_btc = price_btc.reshape(-1, 1)
price_dji = price_dji.reshape(-1, 1)

results = sk.f_classif(price_btc, price_dji)
print(results)