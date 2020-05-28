import numpy as np
import pandas as pd
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from bot_generator_multi import *
from path_file_generator import *
from parameters_generator import *


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

# считываем все csv кривых в один словарь датафреймов
for i in range(COUNT_EXPERIMENTS_GLOBAL):
    path_curve_i = path_file_history(PATH_FOLDER_HISTORY, TICKER_HISTORY_LIST, i)
    df_csv = pd.read_csv(path_curve_i, sep=',')
    df_csv.reset_index(drop=True, inplace=True)
    # print("Файл считан: ", path_curve_i)

    ticker_i = TICKER_HISTORY_LIST[i]

    df_bot_start = df_csv
    dfx[str(ticker_i)] = df_bot_start

k_list = [0] * len(TICKER_HISTORY_LIST)
first_step_status_list = [True] * len(TICKER_HISTORY_LIST)
# print('len(date_list) =', len(date_list))

for j in range(1, len(date_list)):
    date_j = date_list[j]
    print(date_j)
    for i in range(COUNT_EXPERIMENTS_GLOBAL):
        ticker_i = TICKER_HISTORY_LIST[i]
        print(j, ticker_i)
        df_ticker_i = dfx[str(ticker_i)]
        # print(df_ticker_i)
        k = k_list[i]

        if k in range(len(df_ticker_i)):
            print('start', k, ticker_i)
            date_k_ticker = df_ticker_i['Time']
            if date_k_ticker == date_j:
                # print('first_step_status_list ', ticker_i, first_step_status_list[i])
                # print('date_j =', date_j)

                if date_j in df_ticker_i['Time'].tolist() and first_step_status_list[i] is True:
                    # print('date_j = ', date_j, first_step_status_list[i])
                    df_ticker_i = bot_generator_initiation_first_day(df_ticker_i, param_dict, ticker_i, k)
                    # print('initiation day: ', 'k =', k, 'j =', j)
                    # print(df_ticker_i)
                    first_step_status_list[i] = False
                    k_list[i] += 1

                elif date_j in df_ticker_i['Time'].tolist() and first_step_status_list[i] is False:
                    # print('next day: ', 'k =', k, 'j =', j)

                    df_ticker_i = bot_generator_next_day(df_ticker_i, param_dict, k)

                    restart_signal = True
                    df_ticker_i = bot_generator_restart_day(df_ticker_i, param_dict, k, restart_signal)

                    k_list[i] += 1

                else:
                    print('пропускаем ', date_j, ' для ', ticker_i)

                dfx[str(ticker_i)] = df_ticker_i

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
