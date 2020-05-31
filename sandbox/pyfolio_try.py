import pyfolio as pf
import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta

date_1 = datetime.strptime('2016-01-04', '%Y-%m-%d')
date_2 = datetime.strptime('2016-01-05', '%Y-%m-%d')
date_3 = datetime.strptime('2016-01-06', '%Y-%m-%d')
date_4 = datetime.strptime('2016-01-07', '%Y-%m-%d')
date_5 = datetime.strptime('2016-01-08', '%Y-%m-%d')
date_6 = datetime.strptime('2016-01-09', '%Y-%m-%d')
date_7 = datetime.strptime('2016-01-10', '%Y-%m-%d')
date_8 = datetime.strptime('2016-01-11', '%Y-%m-%d')
date_9 = datetime.strptime('2016-01-12', '%Y-%m-%d')
date_10 = datetime.strptime('2016-01-13', '%Y-%m-%d')
print(type(date_5))
index_date = [date_1, date_2, date_3, date_4, date_5, date_6, date_7, date_8, date_9, date_10]
print(index_date)

returns = pd.Series([0, -0.013979, 0.001691, 0.001691, -0.023992, -0.013979, -0.013979, 0.001691, -0.012614, -0.023992], index=index_date)

print(returns)
print(type(returns.index))

pf.create_returns_tear_sheet(returns)