import numpy as np
import pandas as pd
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from funtions_path_file_generator import *
from functions_base import *
from functions_integral_indicators import *



def bot_analytics_summary(experiment_def, prefix_experiment_def):
    start = timer()

    # папки и файлы
    path_folder_bi = folder_check(PATH_FOLDER_BI)
    path_bi = path_folder_bi + '/' + experiment_def + str(prefix_experiment_def) +'.csv'
    print(path_bi)

    # считываение файлы
    df = pd.read_csv(path_bi, sep=',')
    print("Файл считан: ", path_bi)

    df['test'] = np.log(1 + df['day_profit_unrealized_pnl'])
    print(df['test'])

    df_summary = pd.DataFrame(columns=['Time'] + COLUMNS_WEIGHT_IMPACTED)

    date_list = df['Time'].unique().tolist()
    print(date_list)

    df_summary['Time'] = date_list

    for j in range(len(date_list)):
        date_j = date_list[j]
        print('experiment ', prefix_experiment_def, ' ', date_j)
        for i in range(len(COLUMNS_FOR_SUMMARY)):
            column_i = COLUMNS_FOR_SUMMARY[i]
            df_summary.loc[j, column_i] = df.loc[df['Time'] == date_j, column_i].sum()

    # подсчет интегральных параметров Портфеля Ботов
    if TRIGGER_OF_CALCULATION_INTEGRAL_INDICATORS_ON_BOTS_PORTFOLIO is True:
        # подсчет интегральных показателей результатов работы бота
        # оперделяем Returns бота по профитам за день и учетон неализованной прибыли и убытка
        df_summary['return_bot_procent'] = (df_summary['day_profit_unrealized_pnl'] / df_summary['reserved_sum_investment']).astype(float)
        df_summary['return_bot_procent_log'] = np.log(1 + df_summary['return_bot_procent']) # логарифмические приросты
        # внутри функции также есть преобразование в логагифмические приросты там, где это необходимо:
        integral_indicators_dict_bot = caclulation_integral_indicators(df_summary, 'return_bot_procent')
        df_summary['bot_mean'] = integral_indicators_dict_bot.get('mean_annual')
        df_summary['bot_std'] = integral_indicators_dict_bot.get('std_annual')
        df_summary['bot_skew'] = integral_indicators_dict_bot.get('skewness_day')
        df_summary['bot_kurt'] = integral_indicators_dict_bot.get('kurtosis_day')
        df_summary['bot_information_ratio'] = integral_indicators_dict_bot.get('information_ratio_annual')
        # df['bot_sharpe_ratio'] = integral_indicators_dict_bot.get('sharpe_ratio')
        df_summary['bot_max_drawdown'] = integral_indicators_dict_bot.get('max_drawdown')
        df_summary['bot_VaR_95'] = integral_indicators_dict_bot.get('VaR_95')
        df_summary['bot_VaR_95_10_day'] = integral_indicators_dict_bot.get('VaR_95_normal_to_10_day')
        df_summary['bot_VaR_95_non_param'] = integral_indicators_dict_bot.get('VaR_95_non_parametric')
        df_summary['bot_CVaR_95_non_param'] = integral_indicators_dict_bot.get('CVaR_95_non_parametric')
        df_summary['bot_pvalue_normaltest'] = integral_indicators_dict_bot.get('pvalue_normaltest')

        # подсчет интегральных параметров Портфеля Акций соотвтствующих ботов
        if TRIGGER_OF_CALCULATION_INTEGRAL_INDICATORS_ON_STOCK_PORTFOLIO is True:
            # подсчет интегральных показателей результатов работы бота
            # оперделяем Returns бота по профитам за день и учетон неализованной прибыли и убытка
            df_summary['returns_stock_price'] = df_summary['returns_stock_price'].astype(float)  # нормализуем под float
            df_summary['return_stock_procent_log'] = np.log(1 + df_summary['returns_stock_price'])  # логарифмические приросты
            # внутри функции также есть преобразование в логагифмические приросты там, где это необходимо:
            integral_indicators_dict_stock = caclulation_integral_indicators(df_summary, 'returns_stock_price')
            df_summary['stock_mean'] = integral_indicators_dict_stock.get('mean_annual')
            df_summary['stock_std'] = integral_indicators_dict_stock.get('std_annual')
            df_summary['stock_skew'] = integral_indicators_dict_stock.get('skewness_day')
            df_summary['stock_kurt'] = integral_indicators_dict_stock.get('kurtosis_day')
            df_summary['stock_information_ratio'] = integral_indicators_dict_stock.get('information_ratio_annual')
            # df['bot_sharpe_ratio'] = integral_indicators_dict_bot.get('sharpe_ratio')
            df_summary['stock_max_drawdown'] = integral_indicators_dict_stock.get('max_drawdown')
            df_summary['stock_VaR_95'] = integral_indicators_dict_stock.get('VaR_95')
            df_summary['stock_VaR_95_10_day'] = integral_indicators_dict_stock.get('VaR_95_normal_to_10_day')
            df_summary['stock_VaR_95_non_param'] = integral_indicators_dict_stock.get('VaR_95_non_parametric')
            df_summary['stock_CVaR_95_non_param'] = integral_indicators_dict_stock.get('CVaR_95_non_parametric')
            df_summary['stock_pvalue_normaltest'] = integral_indicators_dict_stock.get('pvalue_normaltest')

    return df_summary


def integral_indicators_bot_sigle(df_def, df_integral_total_def, ticker_def):
    # подсчет интегральных показателей результатов работы конкретного бота на конкретной кривой

    # подсчет прибыльности бота по годам
    date_first_list, date_last_list, year_list = find_last_days_year(df_def)

    profit_year_list = []
    profit_start = 0
    profit_end = 0
    return_bot_year_list = []
    reserved_sum_investment_max = df_def['reserved_sum_investment'][0]
    sum_invested_end = 0
    sum_invested_max = max(df_def['sum_invested'])
    cost_sum_invested_end = 0
    cost_sum_invested_list = []
    temporary_down_list = []
    fee_count_start = 0
    fee_count_year = 0
    fee_count_list = []
    fee_list = []
    profit_year_corrected_list = []
    profit_year_corrected_fee_list = []

    print(reserved_sum_investment_max)
    print(sum_invested_max)

    for i in range(len(year_list)):
        year_i = year_list[i]
        date_last_i = date_last_list[i]
        fee_count_year = 0

        for j in range(len(df_def)):
            if df_def['Time'][j] == date_last_i:
                profit_end = df_def['total_profit'][j]
                sum_invested_end = df_def['sum_invested'][j]
                cost_sum_invested_end = df_def['cost_of_sum_investment'][j]
                # fee_count_end = df_def['fee_count'][j]
                # TODO переделать на sum когда переведем fee_count из суммы в кол-во
            if date_convert(df_def['Time'][j]).year == year_i:
                # print(date_convert(df_def['Time'][j]).year)
                fee_count_year = fee_count_year + df_def['fee_count'][j]
                print(fee_count_year)

        temporary_down_end = cost_sum_invested_end - sum_invested_end
        fee_end = fee_count_year * FEE

        profit_year = profit_end - profit_start
        profit_year_corrected = profit_year + temporary_down_end
        profit_year_corrected_fee = profit_year_corrected - fee_end
        profit_start = profit_end

        profit_year_list.append(profit_year)
        cost_sum_invested_list.append(cost_sum_invested_end)
        temporary_down_list.append(temporary_down_end)
        fee_count_list.append(fee_count_year)
        fee_list.append(fee_end)
        profit_year_corrected_list.append(profit_year_corrected)
        profit_year_corrected_fee_list.append(profit_year_corrected_fee)

        # sum_invested_max = max([df_def['sum_invested'][j]
        #                         for j in range(len(df_def))
        #                         if date_convert(df_def['Time'][j]).year == year_i])
        #
        # print(reserved_sum_investment_max)
        # print(sum_invested_max)

        return_bot_year_i = profit_year / reserved_sum_investment_max
        return_bot_year_list.append(return_bot_year_i)
        print('return_bot_year ', year_i, '= ', return_bot_year_i)

        # year_profit_end = [df_def['total_profit'][j] for j in range(len(df_def)) if df_def['Time'][j] == date_last_i][0]

    # подсчет
    return_bot_year_mean = np.mean(return_bot_year_list)
    return_bot_year_std = np.std(return_bot_year_list)
    information_ratio_year = return_bot_year_mean / return_bot_year_std
    sharpe_year = ( return_bot_year_mean - RATE_BENCHMARK ) / return_bot_year_std

    # # 4. Calculate the VaR using point percentile function
    # var_90 = norm.ppf(1 - 0.9, mean,
    #                   std_dev)  # з вірогідністю (90%) 10% ми (не)"звалимось" нижче цієї суми протягом 1 дня
    # # var_x = norm.ppf(1-0.01, mean, std_dev) # з вірогідністю (1%) 99% ми (не)"звалимось" нижче цієї суми протягом 1 дня
    # var_95 = norm.ppf(1 - 0.95, mean,
    #                   std_dev)  # з вірогідністю (95%) 5% ми (не)"звалимось" нижче цієї суми протягом 1 дня
    # var_99 = norm.ppf(1 - 0.99, mean,
    #                   std_dev)  # з вірогідністю (99%) 1% ми (не) "звалимось" нижче цієї суми протягом 1 дня
    # print("Conf Level 90%, Value at Risk: ", var_90)
    # # print("Conf Level 1%, Value at Risk: ", var_x)
    # print("Conf Level 95%, Value at Risk: ", var_95)
    # print("Conf Level 99%, Value at Risk: ", var_99)

    # print('return_bot_year_list = ', return_bot_year_list)
    # print('return_bot_year_mean = ', return_bot_year_mean)
    # print('return_bot_year_std = ', return_bot_year_std)
    # print('sharpe = ', sharpe)
    # print('year_profit_list = ', year_profit_list)
    # print('total_profit = ', sum(year_profit_list))

    df_integral = pd.DataFrame()
    df_integral['year'] = year_list
    df_integral['return_bot_year'] = return_bot_year_list
    df_integral['profit_year'] = profit_year_list
    df_integral['profit_year_corrected'] = profit_year_corrected_list
    df_integral['profit_year_corrected_fee'] = profit_year_corrected_fee_list
    df_integral['cost_sum_invested'] = cost_sum_invested_list
    df_integral['temporary_down'] = temporary_down_list
    df_integral['fee_count'] = fee_count_list
    df_integral['fee'] = fee_list
    df_integral['ticker'] = ticker_def

    # зпаисть интегральных показателей за весь период работы бота
    total_info_row = {'ticker': ticker_def,
                      'return_bot_year_mean': return_bot_year_mean,
                      'return_bot_year_std': return_bot_year_std,
                      'information_ratio_year': information_ratio_year,
                      'sharpe_year': sharpe_year,
                      'total_profit': sum(profit_year_list)}

    df_integral_total = df_integral_total_def.append(total_info_row, ignore_index=True)  # , ignore_index=False

    # TODO Sharpe
    # TODO Information ratio
    # TODO Maximum Dropdown
    # TODO Среднегодовая доходность + Сигма
    # TODO Total Profit

    # print(df_integral)
    # print(df_integral_total)

    return df_integral, df_integral_total
