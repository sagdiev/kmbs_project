# import pyfolio

                                ################ INSTALLING PACKAGES/LIBRARIES ################
#############################################################################################################
import scipy.stats as scs
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from statsmodels.tsa.stattools import adfuller
# from statsmodels.tsa.arima_process import arma_generate_sample
# from statsmodels.tsa.arima_model import ARMA
# from statsmodels.tsa.statespace.sarimax import SARIMAX
# from numpy import cumsum
# import seaborn
# import matplotlib.mlab as mlab
# # from tabulate import tabulate
from scipy.stats import norm




                        ##################### UPLOADING DATA #####################
####################################################################################################################
# df = pd.read_csv(r'C:\Users\Maksym\Desktop\MP\stock_data\barchart/AAPL.csv', sep=',')
# df = pd.read_csv(r'C:\Users\Maksym\Desktop\MP\python\pj_1\bot_results/bot_BTCUSD_76.csv', sep=',')
df = pd.read_csv('/Users/Artem/Documents/GitHub/kmbs_project/data_bot_analytic/experiment_43_history_summary.csv', sep=',')
# /Users/Artem/Documents/GitHub/kmbs_project/data_history/SPX.csv
df.drop(df.tail(1).index,inplace=True)
# df.sort_index(ascending=False, inplace=True)
df.reset_index(drop=True, inplace=True)
# df = df['Open']
df = df['total_profit'] + df['reserved_sum_investment']
df = df.pct_change().dropna() # returns
print("dokhodnost", df)

mean = np.mean(df) #mu
std_dev = np.std(df) #std


# Determine the mean and standard deviation of the daily returns. Plot the normal curve against the daily returns
df.hist(bins=100, density=True, histtype='stepfilled', alpha=0.5)
x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 100)
plt.plot(x, scs.norm.pdf(x, mean, std_dev), "r")
plt.show()
# HISTOGRAM OF DAILY RETURNS AND ITS STANDARD DEVIATION


# 4. Calculate the VaR using point percentile function
var_90 = norm.ppf(1-0.9, mean, std_dev) # з вірогідністю (90%) 10% ми (не)"звалимось" нижче цієї суми протягом 1 дня
# var_x = norm.ppf(1-0.01, mean, std_dev) # з вірогідністю (1%) 99% ми (не)"звалимось" нижче цієї суми протягом 1 дня
var_95 = norm.ppf(1-0.95, mean, std_dev) # з вірогідністю (95%) 5% ми (не)"звалимось" нижче цієї суми протягом 1 дня
var_99 = norm.ppf(1-0.99, mean, std_dev) # з вірогідністю (99%) 1% ми (не) "звалимось" нижче цієї суми протягом 1 дня
print("Conf Level 90%, Value at Risk: ", var_90)
# print("Conf Level 1%, Value at Risk: ", var_x)
print("Conf Level 95%, Value at Risk: ", var_95)
print("Conf Level 99%, Value at Risk: ", var_99)


# Determine the mean and standard deviation of the daily returns. Plot the normal curve against the daily returns
df.hist(bins=100, density=True, histtype='stepfilled', alpha=0.5)
x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 100)
plt.plot(x, scs.norm.pdf(x, mean, std_dev), "r")
plt.show()
# HISTOGRAM OF DAILY RETURNS AND ITS STANDARD DEVIATION


# # 2. Calculate the daily returns
#
# df = df
# plt.hist(df, bins=40)
# plt.xlabel('returns')
# plt.ylabel('frequency')
# plt.grid(True)
# plt.show()
#
#
#
# # 3. Sort the returns
# # df.sort_values('returns', inplace=True, ascending=True)
#
# # 4. Calculate the VaR for 90%, 95%, and 99% confidence levels using quantile function
# var_90 = df.quantile(0.1)
# var_95 = df.quantile(0.05)
# var_99 = df.quantile(0.01)
# print("Conf Level 90%, Value at Risk: ", var_90)
# print("Conf Level 95%, Value at Risk: ", var_95)
# print("Conf Level 99%, Value at Risk: ", var_99)