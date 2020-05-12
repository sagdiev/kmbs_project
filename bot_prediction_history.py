import numpy as np
import pandas as pd
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from path_file_generator import *
from parameters_generator import *


# START
start = timer()

# папки и файлы
path_bot = path_file_without_prefix(PATH_FOLDER_BOT, PATH_FILE_BOT, EXPERIMENT, TICKER)
# path_curve = path_file_without_prefix(path_folder_curve, path_file_curve, experiment, ticker)
# path_curve = path_file_history_without_prefix(path_folder_history, history_ticker)
os.makedirs(path_bot)

# параметры бота

point = 1
amount_first = 1000
step_count = 3

param_dict = param_generate_base_point_amount_first(point, amount_first, step_count)

# procent = param_dict.get('procent')
# amounts_S = param_dict.get('amounts_S')
# r = param_dict.get('r')
# r_fin = param_dict.get('r_fin')
# procent_loss = param_dict.get('procent_loss')

print(param_dict)


# procent = [0, 0.15, 0.20]
# amounts_S = [1000, 1000, 2000]
# r_fin = 4
# procent_loss = 3
# r = 5
#
# procent = [0, 0.02, 0.04]
# amounts_S = [1000, 1000, 2000]
# r_fin = 0.005
# procent_loss = 0.01
# r = 0.005

# print("Процент самого глубокого снижения (от стартовой цены): \n", prod(4, procent) * 100, "%\n")

# старт применения алгоритма бота
for i in range(COUNT_EXPERIMENTS_GLOBAL):

    # count_step = [0] * (len(amounts_S) + 1)
    # size_profit = [0] * (len(amounts_S) + 1)
    # count_days = [0] * (len(amounts_S) + 1)

    # считываение крывых
    path_curve_i = path_file_history(PATH_FOLDER_HISTORY, TICKER_HISTORY_LIST, i)
    df = pd.read_csv(path_curve_i, sep=',')
    # df.sort_index(ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)
    print("Файл считан: ", path_curve_i)
    print(df)

    # x = param_rebalance(param_dict, 0.37195826601590254)
    # print('param_rebalance = ', x)

    # применение бота
    # df, profit = bot_martingale(df, amounts_S, procent, r, r_fin, procent_loss)
    df, profit = bot_martingale(df, param_dict)
    print('profit = ', profit)



    # запись в файл бота
    path_bot_i = path_file(path_bot, i + 1)
    # path_bot_i = path_file(path_bot, i + 1 + 153)
    df.to_csv(path_bot_i, sep=',', index=False,)
    print("Файл создан: ", path_bot_i, "\n")

# таймер
duration = timer() - start
print('Время обработки алгоритма = ', duration)
