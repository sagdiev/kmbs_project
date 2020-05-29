import pandas as pd
import pyfolio as pf
from datetime import datetime
from datetime import date, datetime, timedelta

from base_functions import *


# load dataset
# stock_rets = pd.read_csv(
#     '/Users/Artem/Documents/GitHub/kmbs_project/sandbox/sandbox_src/for_pyfolio.csv', sep=',', index_col=None)
# print(stock_rets)

# e = [float(stock_rets.loc[i, 'Return']) for i in range(len(stock_rets))]

# print(e)
#
# for i in range(len(stock_rets)):
#     x = datetime.strptime(stock_rets['Date'][i], '%Y-%m-%d')
#     stock_rets.loc[i, 'Return'] = x
#     print(x)
#
# stock_rets['Return'] = stock_rets['Return'].dt.date

# print(stock_rets)

# df_portfolio_src = pd.read_csv(
#     '/Users/Artem/Documents/GitHub/kmbs_project/data_bot_analytic/experiment_43_history_summary.csv', sep=',')

# bmark_src = pd.read_csv(
#     '/Users/Artem/Documents/GitHub/kmbs_project/data_history/SPX.csv', sep=',')
#
# print(df_portfolio_src)
#
# df_portfolio_src.rename(columns={'Time':'Date'}, inplace=True)
# # bmark_src.rename(columns={'Time':'Date', 'Open':'Return'}, inplace=True)
#
# # print(df_portfoio_src.loc[0, 'Date'])
#
#
#
# for i in range(len(df_portfolio_src)):
#     df_portfolio_src.loc[i, 'Date'] = date_convert(df_portfolio_src.loc[i, 'Date'])  #.strftime('%Y-%m-%d')
#     # print(date_x)
#
# print(df_portfolio_src['Date'])
# # print(df_portfoio_src['Return'])
#
# df_portfolio = pd.DataFrame()
#
# df_portfolio['Date'] = df_portfolio_src['Date']
# print(df_portfolio['Date'] )
# df_portfolio['Return'] = df_portfolio_src['total_profit'] + df_portfolio_src['reserved_sum_investment']
# stock_rets = df_portfolio['Return'].pct_change()
# stock_rets = df_portfolio['Return'].dropna()
# print('stock_rets', stock_rets)
# # print(df_portfolio['Return'] )

# for i in range(len(bmark_src)):
#     bmark_src.loc[i, 'Date'] = date_convert(bmark_src.loc[i, 'Date']).strftime('%Y-%m-%d')


# # df.to_csv(f, index=False) if i == 0 else df.to_csv(f, index=False, header=0)
#    Date    Return
# 2016-01-04 -0.013979
# 2016-01-05  0.001691
# 2016-01-06 -0.012614
# 2016-01-07 -0.023992
# 2016-01-08 -0.010977



# create tear sheet
# d = pf.create_returns_tear_sheet(stock_rets)
# pf.create_full_tear_sheet(df_portfolio_src, benchmark_rets=bmark_src)



import pandas as pd
import pyfolio as pf
import numpy as np

dates = pd.date_range(start='2017-01-01',end='2017-12-31', freq=pd.tseries.offsets.BDay())
data = (np.random.rand(len(dates))-0.5)/100
df = pd.DataFrame({'dates':dates,'col':data})
df = df.set_index('dates')
pf.create_returns_tear_sheet(df['col'])

