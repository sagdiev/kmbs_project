import numpy as np
import pandas as pd
import scipy.stats as stats
from math import sqrt
from datetime import datetime
# import random
# import itertools
import pylab as p

from constants import *
from functions_risk import *

def caclulation_integral_indicators(df_def, column_name_of_returns):

        # Returns from the portfolio (r) and market (m)
        returns = df_def[column_name_of_returns]
        # используем логарифмические приросты для некоторых показателей
        returns_log = np.log(1 + df_def[column_name_of_returns])
        # print(returns, returns_log)

        # Expected return
        mean = np.mean(returns_log)
        mean_annual = mean * YEAR_DAYS
        print('mean_annual', mean_annual)

        std = vol(returns_log)
        std_annual = std * np.sqrt(YEAR_DAYS)
        print('std_annual', std_annual)

        skewness_day = stats.skew(returns_log, bias=False)
        print('skewness_day', skewness_day)
        kurtosis_day = stats.kurtosis(returns_log, bias=False)
        print('kurtosis_day', kurtosis_day)

        VaR_95_non_parametric = var_non_parametric(returns, 0.95)
        print('VaR_95_non_parametric', VaR_95_non_parametric)
        VaR_95_normal = var_normal(returns, 0.95)
        print('VaR_95_normal', VaR_95_normal)

        VaR_95_normal_to_10_day = VaR_95_normal * sqrt(10)
        print('VaR_95_normal_to_10_day', VaR_95_normal_to_10_day)

        CVaR_95_non_parametric = cvar_non_parametric(returns, 0.95)
        print('CVaR_95_non_parametric', CVaR_95_non_parametric)


        information_ratio_annual = mean_annual / std_annual
        print('information_ratio_annual', information_ratio_annual)
        # sharpe = sharpe_ratio(mean, returns, risk_free)

        if TRIGGER_OF_CALCULATION_INTEGRAL_INDICATORS_ON_EACH_AND_STOCK_BOT_MAX_DRAWDOWN is True:
                max_drawdown = max_dd(returns)
                print('max_drawdown', max_drawdown)
        else:
                max_drawdown = 0
                print('max_drawdown - не считаем и просто ставим 0:', max_drawdown)

        returns_log_list = returns_log.dropna().tolist()
        print('\nNormal test for given data "returns_log":\n', stats.normaltest(returns_log_list))
        pvalue_normaltest = stats.normaltest(returns_log_list)[1]


        integral_indicators_dict_def = {
                'mean_annual': mean_annual,
                'std_annual': std_annual,
                'skewness_day': skewness_day,
                'kurtosis_day': kurtosis_day,
                'information_ratio_annual': information_ratio_annual,
                # 'sharpe_ratio': sharpe,
                'max_drawdown': max_drawdown,
                'VaR_95': VaR_95_normal,
                'VaR_95_normal_to_10_day': VaR_95_normal_to_10_day,
                'VaR_95_non_parametric': VaR_95_non_parametric,
                'CVaR_95_non_parametric': CVaR_95_non_parametric,
                'pvalue_normaltest': pvalue_normaltest
        }

        return integral_indicators_dict_def
