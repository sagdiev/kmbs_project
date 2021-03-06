import numpy as np
import pandas as pd
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from funtions_path_file_generator import *


# START
start = timer()

# записываем данные эксперимента в журнал
with open('experiments_logbook.txt', 'w') as file:
    running_file = sys.argv[0]
    logbook_text = logbook_text_compelling(running_file)
    print(logbook_text)
    file.write(logbook_text)

# папки и файлы
path_bot = path_file_without_prefix(PATH_FOLDER_BOT, PATH_FILE_BOT, EXPERIMENT, TICKER)
path_curve = path_file_without_prefix(PATH_FOLDER_CURVE, PATH_FILE_CURVE, EXPERIMENT, TICKER)
# os.makedirs(path_bot)

procent = [0, 0.15, 0.20]
amounts_S = [1000, 1000, 2000]
r_fin = 4
procent_loss = 3
r = 5

# print("Процент самого глубокого снижения (от стартовой цены): \n", prod(4, procent) * 100, "%\n")

# старт применения алгоритма бота
for i in range(COUNT_EXPERIMENTS_GLOBAL):

    count_step = [0] * (len(amounts_S) + 1)
    size_profit = [0] * (len(amounts_S) + 1)
    count_days = [0] * (len(amounts_S) + 1)

    # считываение крывых
    path_curve_i = path_file(path_curve, i + 1)
    df = pd.read_csv(path_curve_i, sep=',')
    print("Файл считан: ", path_curve_i)

    # применение бота
    df, profit = bot_martingale(df, amounts_S, procent, r, r_fin, procent_loss)
    print('profit = ', profit)

    # запись в файл бота
    path_bot_i = path_file(path_bot, i + 1)
    df.to_csv(path_bot_i, sep=',', index=False,)
    print("Файл создан: ", path_bot_i, "\n")

# таймер
duration = timer() - start
print('Время обработки алгоритма = ', duration)
