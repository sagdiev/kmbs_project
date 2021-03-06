import numpy as np
import pandas as pd
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from bot_generator_multi import *
from funtions_path_file_generator import *
from functions_parameters_generator import *


# START
start = timer()

# папки и файлы
path_bot = path_file_without_prefix(PATH_FOLDER_BOT, PATH_FILE_BOT, EXPERIMENT, TICKER)
os.makedirs(path_bot)

# параметры бота
point_bot = POINT_BOT_START
step_count_bot = STEP_BOT_START
total_amount_bot = TOTAL_RESERVED_BOT_START
param_dict = param_generate_base_point_total_amount(point_bot, total_amount_bot, step_count_bot)
print(param_dict)

date_list = DATE_LIST_ETALON
dfx = {}  # сборный словарь всех датафреймов
profit_i = 0

# считываем все csv кривых в один словарь датафреймов
for i in range(COUNT_EXPERIMENTS_GLOBAL):
    path_curve_i = path_file_history(PATH_FOLDER_HISTORY, TICKER_HISTORY_LIST, i)
    df_csv = pd.read_csv(path_curve_i, sep=',')
    df_csv.reset_index(drop=True, inplace=True)
    # print("Файл считан: ", path_curve_i)

    ticker_i = TICKER_HISTORY_LIST[i]

    df_bot_start = df_csv
    dfx[str(ticker_i)] = df_bot_start

len_list = len(TICKER_HISTORY_LIST)
rebalance_period = 252  # 252 если годовой (это количество дней в базах), может быть другой для экспериментов

k_list = [0] * len_list
first_step_status_list = [True] * len_list

profit_list = [0] * len_list
profit_portfolio_accumulated = 0
param_dict_list = [param_dict] * len_list
total_amount_bot_list = [total_amount_bot] * len_list
annual_profit_take_list = [0] * len_list

reinvest_year_signal = True
annual_profit_take_signal = False

for j in range(1, len(date_list)):
    date_j = date_list[j]
    print(date_j, '\n')

    if j % rebalance_period == 0:
        reinvest_year_signal = False
        annual_profit_take_signal = True
    elif j % rebalance_period < rebalance_period / 12 * 10:
        reinvest_year_signal = True
        annual_profit_take_signal = False
    else:
        reinvest_year_signal = False
        annual_profit_take_signal = False

    for i in range(COUNT_EXPERIMENTS_GLOBAL):
        ticker_i = TICKER_HISTORY_LIST[i]
        print(j, ticker_i)
        df_ticker_i = dfx[str(ticker_i)]
        param_i = param_dict_list[i]
        # print(df_ticker_i)
        k = k_list[i]

        if k in range(len(df_ticker_i)):
            # print('start', k, ticker_i)
            # print('first_step_status_list ', ticker_i, first_step_status_list[i])
            # print('date_j =', date_j)

            if date_j in df_ticker_i['Time'].tolist() and first_step_status_list[i] is True:
                # print('date_j = ', date_j, first_step_status_list[i])
                df_ticker_i = bot_generator_initiation_first_day(df_ticker_i, param_i, ticker_i, k)
                # print('initiation day: ', 'k =', k, 'j =', j)
                # print(df_ticker_i)
                profit_i = df_ticker_i['total_profit'][k]

                first_step_status_list[i] = False
                k_list[i] += 1

            elif date_j in df_ticker_i['Time'].tolist() and first_step_status_list[i] is False:
                # print('next day: ', 'k =', k, 'j =', j)

                df_ticker_i = bot_generator_next_day(df_ticker_i, param_i, k)
                profit_i = df_ticker_i['total_profit'][k]
                annual_profit_take_i = annual_profit_take_list[i]
                print('annual_profit_take_i', annual_profit_take_i)

                if reinvest_year_signal is True:

                    # ВАРИАНТ 1 Реинвестирование с понижением резервных сумм для упавших акций
                    # total_amount_bot_list[i] = total_amount_bot + profit_i
                    # ===================================================================

                    # # ВАРИАНТ 2 Реинвестирование без понижения резервных сумм для упавших акций
                                                # (рисковей для одной акции, но возможно лучше для всего портфеля)
                    if profit_i - annual_profit_take_i > 0:
                        total_amount_bot_list[i] = total_amount_bot + profit_i - annual_profit_take_i
                    else:
                        total_amount_bot_list[i] = total_amount_bot
                    # =====================================================================

                    # # ВАРИАНТ 3 Реинвестирование с понижением резервных сумм для упавших акций
                    #                             # но без повышения растущих (самая консервативная стратегия)
                    # if profit_i > 0:
                    #     total_amount_bot_list[i] = total_amount_bot
                    # else:
                    #     total_amount_bot_list[i] = total_amount_bot + profit_i
                    # # =======================================================================

                else:
                    total_amount_bot_list[i] = total_amount_bot



                param_dict_list[i] = param_generate_base_point_total_amount(
                    point_bot, total_amount_bot_list[i], step_count_bot)
                # print(param_dict_list[i])


                restart_signal = True
                df_ticker_i = bot_generator_restart_day(df_ticker_i, param_i, k, restart_signal)

                profit_i = df_ticker_i['total_profit'][k]

                k_list[i] += 1

            else:
                f = 1  # удалить
                # print('пропускаем ', date_j, ' для ', ticker_i)

            dfx[str(ticker_i)] = df_ticker_i
            # print(df_ticker_i)
            # print('profit_i ', ticker_i, ' = ', profit_i)
            # profit_list[i] = profit_i

        if annual_profit_take_signal is True:
            if profit_i - annual_profit_take_i > 0:
                annual_profit_take_list[i] = profit_i # - annual_profit_take_i

    # таймер
    duration = timer() - start
    print('Время обработки шага ', j, ' = ', duration)
    # #общая накопленная прибыль
    # print(profit_list)
    # profit_portfolio_accumulated = sum(profit_list)
    # print('ИТОГО ПРОФИТ ПОРТФЕЛЯ после шага ', j, ' = ', profit_portfolio_accumulated)

# запись в файл бота
for i in range(COUNT_EXPERIMENTS_GLOBAL):
    ticker_i = TICKER_HISTORY_LIST[i]
    df_bot_i = dfx[str(ticker_i)]

    path_bot_i = path_file(path_bot, i + 1)
    df_bot_i.to_csv(path_bot_i, sep=',', index=False,)
    print('Файл ', ticker_i, ' создан: ', path_bot_i, '\n')

# таймер
duration = timer() - start
print('Время обработки всего алгоритма = ', duration)
