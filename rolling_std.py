import numpy as np
import pandas as pd
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from path_file_generator import *
from parameters_generator import *


def rolling_std(df_def):
    # расчет скользящего среднего приведенного к годовому c окном WINDOW_ROLLING_STD
    # ВНИМАНИЕ! первый период временно обогощается средними данными периода - в идеале надо наполнять историческими данными прошлых периодов

    # rolling_std_cacl = df_def['Open'].pct_change().rolling(WINDOW_ROLLING_STD).std(ddof=0) * 252 ** 0.5
    rolling_std_cacl = df_def['Open'].pct_change().rolling(WINDOW_ROLLING_STD).std(ddof=0)
    rolling_std_mean = np.mean(rolling_std_cacl)

    for i in range(WINDOW_ROLLING_STD):  # первый период обогощаем средними данными периода
        rolling_std_cacl[i] = rolling_std_mean

    return rolling_std_cacl


window_size = WINDOW_ROLLING_STD

point = 1
amount_first = 1000
step_count = 3
total_reserved = 10000

# param_dict = param_generate_base_point_amount_first(point, amount_first, step_count)
param_dict = param_generate_base_point_total_amount(point, total_reserved, step_count)

procent = param_dict.get('procent')
amounts_S = param_dict.get('amounts_S')
r = param_dict.get('r')
r_fin = param_dict.get('r_fin')
procent_loss = param_dict.get('procent_loss')

print(param_dict)

rolling_std_all = []

for i in range(1):
# for i in range(COUNT_EXPERIMENTS_GLOBAL):

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

    # применение бота
    # df, profit = bot_martingale(df, amounts_S, procent, r, r_fin, procent_loss)
    # print('profit = ', profit)

    print('Старт rolling')

    # rolling_std = df['Open'].pct_change().rolling(window_size).std(ddof=0) * 252 ** 0.5

    df['Std_Rolling'] = rolling_std(df)
    rolling_std_all.append(np.mean(df['Std_Rolling']))

    # скользящее стандартное отклонение приведенное к гоовому
    # ddof=0 необходимо в этом случае, потому что нормализация стандартного отклонения
    # осуществляется по len(Ser)-ddof, и что ddof умолчанию ddof 1 в пандах.

    print('rolling_std = ', df['Std_Rolling'])
    print('average_rolling_std = ', np.mean(df['Std_Rolling']))

print('rolling_std_all = ', sorted(rolling_std_all))
print('average_rolling_std_all = ', np.mean(rolling_std_all))
