import numpy as np
import pandas as pd
import scipy.stats as stats
from datetime import datetime
# import random
# import itertools

from constants import *
from functions_risk import *

def caclulation_integral_indicators(df_def, column_name_of_returns):

        # Returns from the portfolio (r) and market (m)
        returns = df_def[column_name_of_returns]
        print(returns)

        # TODO market = nrand.uniform(-1, 1, 50)
        # Risk free rate
        risk_free = RATE_BENCHMARK

        # Expected return
        mean = np.mean(returns)
        mean_annual = mean * YEAR_DAYS

        std = vol(returns)
        std_annual = std * np.sqrt(YEAR_DAYS)

        skewness_day = stats.skew(returns, bias=False)
        kurtosis_day = stats.kurtosis(returns, bias=False)


        # VaR_01 = var(returns, 0.01)
        # VaR_05 = var(returns, 0.05)
        # VaR_90 = var(returns, 0.90)
        # VaR_95_non_parametric = var_non_parametric(returns, 0.95)
        VaR_95_normal = var_normal(returns, 0.95)

        # VaR_99 = var(returns, 0.99)

        # CVaR_01 = cvar(returns, 0.01)
        # CVaR_05 = cvar(returns, 0.05)
        # CVaR_90 = cvar(returns, 0.90)
        # CVaR_95 = cvar_non_parametric(returns, 0.95)
        # CVaR_99 = cvar(returns, 0.99)

        information_ratio_annual = mean_annual / std_annual
        # sharpe = sharpe_ratio(mean, returns, risk_free)

        max_drawdown = max_dd(returns)


        # base indicators
        print("mean_annual =", mean_annual)
        print("std_annual =", std_annual)
        print("information_ratio_annual =", information_ratio_annual)
        # print("beta =", beta(returns, market))
        # print("hpm(0.0)_1 =", hpm(returns, 0.0, 1))
        # print("lpm(0.0)_1 =", lpm(returns, 0.0, 1))
        # print("VaR(0.01) =", VaR_01)
        # print("VaR(0.05) =", VaR_05)
        # print("VaR(0.90) =", VaR_90)
        print("VaR(0.95) =", VaR_95_normal)
        # print("VaR(0.99) =", VaR_99)

        # print("CVaR(0.01) =", CVaR_01)
        # print("CVaR(0.05) =", CVaR_05)
        # print("CVaR(0.90) =", CVaR_90)
        # print("CVaR(0.95) =", CVaR_95)
        # print("CVaR(0.99) =", CVaR_99)

        # print("Drawdown(5) =", dd(returns, 5))
        print("Max Drawdown =", max_drawdown)

        # Risk-adjusted return based on Volatility
        # print("Treynor Ratio =", treynor_ratio(e, returns, market, risk_free))
        # print("Sharpe Ratio =", sharpe)
        # print("Information Ratio =", information_ratio(returns, market))
        # print("Information Ratio =", information_ratio(returns, market))


        # Risk-adjusted return based on Value at Risk
        # print("Excess VaR =", excess_var(mean, returns, risk_free, 0.05))
        # print("Conditional Sharpe Ratio =", conditional_sharpe_ratio(mean, returns, risk_free, 0.05))

        # Risk-adjusted return based on Lower Partial Moments
        # print("Omega Ratio =", omega_ratio(e, returns, risk_free))
        # print("Sortino Ratio =", sortino_ratio(e, returns, risk_free))
        # print("Kappa 3 Ratio =", kappa_three_ratio(e, returns, risk_free))
        # print("Gain Loss Ratio =", gain_loss_ratio(returns))
        # print("Upside Potential Ratio =", upside_potential_ratio(returns))

        # Risk-adjusted return based on Drawdown risk
        # print("Calmar Ratio =", calmar_ratio(mean, returns, risk_free))
        # print("Sterling Ratio =", sterling_ration(mean, returns, risk_free, 5))
        # print("Burke Ratio =", burke_ratio(mean, returns, risk_free, 5))

        integral_indicators_dict_def = {
                'mean_annual': mean_annual,
                'std_annual': std_annual,
                'skewness_day': skewness_day,
                'kurtosis_day': kurtosis_day,
                'information_ratio_annual': information_ratio_annual,
                # 'sharpe_ratio': sharpe,
                'max_drawdown': max_drawdown,
                'VaR_95': VaR_95_normal,
                # 'CVaR_95': CVaR_95
        }

        return integral_indicators_dict_def


