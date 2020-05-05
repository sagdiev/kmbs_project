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
path_folder_bi = folder_check(path_folder_bi)
path_bi = path_folder_bi + '/' + experiment +'.csv'
print(path_bi)

r = file_clear(path_bi)

# старт применения алгоритма бота

with open(path_bi, 'a') as f:

    for i in range (count_experiments_global):

        # считываение файлы
        path_bot_i = path_file(path_bot, i + 1)
        df = pd.read_csv(path_bot_i, sep=',')
        print("Файл считан: ", path_bot_i)
        print(df)

        df['curve_number'] = 'curve_' + str(i + 1)
        # df['ticker'] = ticker
        df['ticker'] = history_ticker[i]
        print(df)

        df.to_csv(f, index=False) if i == 0 else df.to_csv(f, index=False, header=0)

# таймер
duration = timer() - start
print('Время обработки алгоритма = ', duration)