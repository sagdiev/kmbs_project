import pandas as pd

df = pd.read_csv('data_history/t.csv')
df.sort_index(ascending=False, inplace=True)
print(df)