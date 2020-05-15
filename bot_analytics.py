import numpy as np
import pandas as pd
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from path_file_generator import *
from base_functions import *


def integral_indicators_bot_sigle(df_def):
    # подсчет интегральных показателей результатов работы конкретного бота на конкретной кривой

    # подсчет прибыльности по годам
    date_first_list, date_last_list, year_list = find_last_days_year(df_def)

    year_profit_list = []
    year_profit_start = 0
    return_year_list = []

    for i in range(len(year_list)):
        year_i = year_list[i]
        date_last_i = date_last_list[i]
        #
        # one_day = [list(df_def[j]) for j in range(len(df_def)) if df_def['Time'][j] == date_last_i][0]
        # print(one_day)

        year_profit_end = [df_def['total_profit'][j] for j in range(len(df_def)) if df_def['Time'][j] == date_last_i][0]

        year_profit = year_profit_end - year_profit_start
        year_profit_list.append(year_profit)
        year_profit_start = year_profit_end

        reserved_sum_investment_max = max([df_def['reserved_sum_investment'][j]
                                           for j in range(len(df_def))
                                           if date_convert(df_def['Time'][j]).year == year_i])

        return_year_i = year_profit/reserved_sum_investment_max
        return_year_list.append(return_year_i)
        print('return_year = ', return_year_i)

    return_year_mean = np.mean(return_year_list)
    return_year_std = np.std(return_year_list)
    sharpe = return_year_mean/return_year_std
    print('return_year_list = ', return_year_list)
    print('return_year_mean = ', return_year_mean)
    print('return_year_std = ', return_year_std)
    print('sharpe = ', sharpe)
    print('year_profit_list = ', year_profit_list)
    print('total_profit = ', sum(year_profit_list))





    df_cacl = 1

    # TODO Sharpe
    # TODO Information ratio
    # TODO Maximum Dropdown
    # TODO Среднегодовая доходность + Сигма
    # TODO Total Profit

    return df_cacl

# START
start = timer()

# папки и файлы
path_bot = path_file_without_prefix(PATH_FOLDER_BOT, PATH_FILE_BOT, EXPERIMENT, TICKER)
path_folder_analytic = folder_check(PATH_FOLDER_BOT_ANALYTIC)
path_analytic = path_folder_analytic + '/' + EXPERIMENT +'.csv'
print(path_analytic)

r = file_clear(path_analytic)

# старт применения алгоритма бота

with open(path_analytic, 'a') as f:

    for i in range (COUNT_EXPERIMENTS_GLOBAL):

        # считываение файлы
        path_bot_i = path_file(path_bot, i + 1)
        df = pd.read_csv(path_bot_i, sep=',')
        print("Файл считан: ", path_bot_i)
        print(df)

        df['curve_number'] = 'curve_' + str(i + 1)
        # df['ticker'] = ticker
        df['ticker'] = TICKER_HISTORY_LIST[i]
        # for j in range(len(list(df['Ticker']))):
        #     print(df['Ticker'][j])
        #     df['Ticker'][j] = date_convert(df['Ticker'][j])
        #
        # print(df)

        # df.to_csv(f, index=False) if i == 0 else df.to_csv(f, index=False, header=0)

        integral_indicators_bot_sigle(df)

# таймер
duration = timer() - start
print('Время обработки алгоритма = ', duration)