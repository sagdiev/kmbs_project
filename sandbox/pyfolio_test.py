import pandas as pd
import pyfolio as pf
import numpy as np
from datetime import date, datetime, timedelta

# from base_functions import *


# load dataset
stock_rets = pd.read_csv(
     '/Users/Artem/Documents/GitHub/kmbs_project/data_bot_analytic/experiment_43_history_summary.csv', sep=',', index_col=None)
# print(stock_rets)

index_date = stock_rets['Time'].tolist()
index_date = [datetime.strptime(i, '%m/%d/%Y') for i in index_date]
# index_date = [datetime.strptime(i, '%Y-%m-%d') for i in index_date]
# print(type(index_date))
# print(index_date)

equity_line = stock_rets['total_profit'] + stock_rets['reserved_sum_investment']
# print('equity_line', equity_line)
stock_returns = equity_line.pct_change()  #.dropna()
stock_returns = stock_returns.tolist()
# print(stock_returns)



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






# date_1 = datetime.strptime('2016-01-04', '%Y-%m-%d')
# date_2 = datetime.strptime('2016-01-05', '%Y-%m-%d')
# date_3 = datetime.strptime('2016-01-06', '%Y-%m-%d')
# date_4 = datetime.strptime('2016-01-07', '%Y-%m-%d')
# date_5 = datetime.strptime('2016-01-08', '%Y-%m-%d')
# date_6 = datetime.strptime('2016-01-09', '%Y-%m-%d')
# date_7 = datetime.strptime('2016-01-10', '%Y-%m-%d')
# date_8 = datetime.strptime('2016-01-11', '%Y-%m-%d')
# date_9 = datetime.strptime('2016-01-12', '%Y-%m-%d')
# date_10 = datetime.strptime('2016-01-13', '%Y-%m-%d')
# print(type(date_5))
# index_date = [date_1, date_2, date_3, date_4, date_5, date_6, date_7, date_8, date_9, date_10]
# print(index_date)
# index_date = pd.to_datetime(index_date)
# print(type(index_date))

index_date = pd.to_datetime(index_date)
try:
    index_date = index_date.tz_localize('UTC')
except TypeError:
    index_date = index_date.tz_convert('UTC')
# print(index_date)
# print(type(index_date))
#
start_date = index_date[0]
# print(start_date)
# print(type(start_date))
# stock_returns[0] = 0
# print(stock_returns)
returns = pd.Series(stock_returns, index=index_date)
# print(returns)
returns = pd.Series(stock_returns, index=index_date)
returns.index = pd.to_datetime(index_date)
print(returns.index)
# returns.index = pd.dt.to_pydatetime(returns.index)
# print(returns.index[-1])
# print(type(returns.index))

# pf.create_returns_tear_sheet(returns, live_start_date=start_date)
pf.create_returns_tear_sheet(returns)



# dates = pd.date_range(start='2017-01-01',end='2017-12-31', freq=pd.tseries.offsets.BDay())
# data = (np.random.rand(len(dates))-0.5)/100
# df = pd.DataFrame({'dates':dates,'col':data})
# df = df.set_index('dates')
# pf.create_returns_tear_sheet(df['col'])

# Most people I talk to who are on pandas >= 1.0 install the master branch via github, since PyPi release is at April 2019
#
# (Pandas 1.0 release in Jan 2020)
#
# pip install git+https://github.com/quantopian/pyfolio.git

