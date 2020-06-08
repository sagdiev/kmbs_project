import numpy as np
import pandas as pd


print(np.log(10))

df = pd.read_csv(
     '/Users/Artem/Documents/GitHub/kmbs_project/data_bot/history/experiment_67_history/bot_1.csv', sep=',', index_col=None)

df['day_profit'] = df['day_profit'].fillna(0)
df['return_log'] = np.log(
    (df['day_profit'] + df['reserved_sum_investment']) / df['reserved_sum_investment'])

print(df['return_log'])
