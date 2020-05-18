import pandas as pd

d1 = {'col1': [1, 2], 'col2': [3, 4]}
df1 = pd.DataFrame(data=d1)
print(df1)

d2 = {'col1': [6, 9], 'col2': [3, 4]}
df2 = pd.DataFrame(data=d2)
print(df2)

dfx = {'df1': df1, 'df2': df2}

print(dfx)

print(dfx['df2'])
