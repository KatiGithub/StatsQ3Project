import pandas as pd
import numpy as np
import sklearn.feature_selection as sk

btc_dji_df = pd.read_csv('../data/btc_dji.csv')

price_btc = np.array(btc_dji_df['btc_closing_price'])
price_dji = np.array(btc_dji_df['dji_closing_price'])

price_btc_dji_df = pd.DataFrame({
    'btc': price_btc,
    'dji': price_dji
})

spearmanr_correlation = price_btc_dji_df.corr(method='spearman')
print(spearmanr_correlation)