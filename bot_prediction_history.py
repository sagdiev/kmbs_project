import numpy as np
import pandas as pd
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from path_file_generator import *


# START
start = timer()

# папки и файлы
path_bot = path_file_without_prefix(path_folder_bot, path_file_bot, experiment, ticker)
# path_curve = path_file_without_prefix(path_folder_curve, path_file_curve, experiment, ticker)
# path_curve = path_file_history_without_prefix(path_folder_history, history_ticker)
# os.makedirs(path_bot)

# параметры бота
# procent = [0, 0.15, 0.20]
# amounts_S = [1000, 1000, 2000]
# r_fin = 4
# procent_loss = 3
# r = 5

procent = [0, 0.02, 0.04]
amounts_S = [1000, 1000, 2000]
r_fin = 0.005
procent_loss = 0.01
r = 0.005

# print("Процент самого глубокого снижения (от стартовой цены): \n", prod(4, procent) * 100, "%\n")

# старт применения алгоритма бота
for i in range (count_experiments_global):

    count_step = [0] * (len(amounts_S) + 1)
    size_profit = [0] * (len(amounts_S) + 1)
    count_days = [0] * (len(amounts_S) + 1)

    # считываение крывых
    path_curve_i = path_file_history(path_folder_history, history_ticker, i)
    df = pd.read_csv(path_curve_i, sep=',')
    # df.sort_index(ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)
    print("Файл считан: ", path_curve_i)
    print(df)

    # применение бота
    df, profit = bot_martingale(df, amounts_S, procent, r, r_fin, procent_loss)
    print('profit = ', profit)

    # запись в файл бота
    path_bot_i = path_file(path_bot, i + 1)
    df.to_csv(path_bot_i, sep = ',', index=False,)
    print("Файл создан: ", path_bot_i, "\n")

# таймер
duration = timer() - start
print('Время обработки алгоритма = ', duration)