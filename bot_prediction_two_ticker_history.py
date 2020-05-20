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
# os.makedirs(path_bot)

# параметры бота
point_bot = 1
step_count_bot = 3
total_amount_bot = 10000
param_dict = param_generate_base_point_total_amount(point_bot, total_amount_bot, step_count_bot)
print(param_dict)

date_list = DATE_LIST_ETALON
dfx = {} # сборный словарь всех датафреймов

# считываем все csv кривых в один словарь датафреймов
for i in range(COUNT_EXPERIMENTS_GLOBAL):
    path_curve_i = path_file_history(PATH_FOLDER_HISTORY, TICKER_HISTORY_LIST, i)
    df_csv = pd.read_csv(path_curve_i, sep=',')
    df_csv.reset_index(drop=True, inplace=True)
    print("Файл считан: ", path_curve_i)

    ticker_i = TICKER_HISTORY_LIST[i]

    df_bot_start = bot_generator_initiation_first_day(df_csv, param_dict)
    dfx[str(ticker_i)] = df_bot_start

    # dfx[str(ticker_i)] = df_csv

# print(dfx['AAPL']['t'])
# print(dfx['AABA_TEST'])

k_list = [0, 0]

for j in range(len(date_list)):
    date_j = date_list[j]
    # print(date_j)
    for i in range(COUNT_EXPERIMENTS_GLOBAL):
        ticker_i = TICKER_HISTORY_LIST[i]
        df_ticker_i = dfx[str(ticker_i)]
        if date_j in df_ticker_i['Time'].tolist():
            # print(k_list[i] + 1)
            k = k_list[i]
            k_list[i] += 1

            # print(ticker_i, ' ', date_j, ' соответствует ', df_ticker_i['Time'][k], ' df_ticker_i дата = ', df_ticker_i['Open'][k])

            # todo проверка: нужен ли второй вход
            bot_generator_next_day(df_ticker_i, j)

            # todo ребаланссировка параметров бота или решения входит/не входить
            bot_generator_restart_day(df_ticker_i, j)





# d1 = {'col1': [1, 2], 'col2': [3, 4]}
# df1 = pd.DataFrame(data=d1)
# print(df1)
#
# d2 = {'col1': [6, 9], 'col2': [3, 4]}
# df2 = pd.DataFrame(data=d2)
# print(df2)
#
# dfx = {'df1': df1, 'df2': df2}
#
# print(dfx)
#
# print(dfx['df2'])


# таймер
duration = timer() - start
print('Время обработки всего алгоритма = ', duration)
