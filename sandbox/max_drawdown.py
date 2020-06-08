import pandas as pd
# from pandas_datareader import data
import matplotlib.pyplot as pp
from datetime import date, datetime, timedelta

stock_rets = pd.read_csv(
     '/Users/Artem/Documents/GitHub/kmbs_project/data_bot_analytic/experiment_53_history_summary.csv', sep=',', index_col=None)

# stock_rets['equity_line'] = stock_rets['total_profit'] + stock_rets['reserved_sum_investment']

Roll_Max = stock_rets['equity_line'].cummax()
Daily_Drawdown = stock_rets['equity_line']/Roll_Max - 1.0
Max_Daily_Drawdown = Daily_Drawdown.cummin()

print(Max_Daily_Drawdown)

# Plot the results
Daily_Drawdown.plot()
Max_Daily_Drawdown.plot()
pp.show()