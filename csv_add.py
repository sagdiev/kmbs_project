import pandas, sys
import pandas as pd

df1 = pd.read_csv("/Users/Artem/Documents/GitHub/kmbs_project/data_bi/experiment_62_history.csv")
df2 = pd.read_csv("/Users/Artem/Documents/GitHub/kmbs_project/data_bi/experiment_62.2_history.csv")

out = df1.append(df2)
print(out)

with open('/Users/Artem/Documents/GitHub/kmbs_project/data_bi/experiment_62_ALL_history.csv', 'w', encoding='utf-8') as f:
    out.to_csv(f, index=False)