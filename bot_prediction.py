import numpy as np
import os
import matplotlib.pyplot as plt
import stochastic.continuous
import stochastic.diffusion
from constants import *
from bot_generator import *
from path_file_generator import *


import pandas as pd
import math as m
import numpy as np
from timeit import default_timer as timer


# def isfloat(value):
#     try:
#         float(value)
#         return True
#     except ValueError:
#         return False


# def path_file_curve_i(prefix_def):
#     path_file_curve_i = path_folder_curve_ticker + path_file_curve + '_' + str(prefix_def) + '.csv'
#
#     return path_file_curve_i
#
#
# def path_file_bot_result_i(prefix_def):
#     path_file_bot_result_i = path_folder_bot_result_ticker + path_file_bot_result + '_' + str(prefix_def) + '.csv'
#
#     return path_file_bot_result_i
#
#
# def path_folder_bot_result_ticker(ticker_def): # создание папки, если еще не существует
#
#     file_ticker = path_folder_bot_result + ticker_def + '/'
#     dirName = file_ticker
#
#     try:
#         os.mkdir(dirName)
#         print("Directory ", dirName, " Created ")
#     except FileExistsError:
#         print("Directory ", dirName, " already exists")
#
#     return file_ticker


# START
start = timer()

# path_folder_curve_ticker = path_folder_curve + ticker + '/'
# path_folder_bot_result_ticker = path_folder_bot_result_ticker(ticker)
path_bot = path_file_without_prefix(path_folder_bot, path_file_bot, experiment, ticker)
path_curve = path_file_without_prefix(path_folder_curve, path_file_curve, experiment, ticker)



procent = [0, 0.15, 0.20, 0.25, 0.30]
amounts_S = [1000, 1000, 2000, 4000, 8000]
r_fin = 10
procent_loss = 10
r = 10

print("Процент самого глубокого снижения (от стартовой цены): \n", prod(4, procent) * 100, "%\n")

for i in range (count_experiments_global):

    count_step = [0] * (len(amounts_S) + 1)
    size_profit = [0] * (len(amounts_S) + 1)
    count_days = [0] * (len(amounts_S) + 1)

    path_curve_i = path_file(path_curve, i + 1)
    df = pd.read_csv(path_curve_i, sep=',')
    print("Файл считан: ", path_curve_i)
    # print("Стартовая цена: \n", df['Price'][0],"\n")

    df, profit = bot_martingale(df, amounts_S, procent, r, r_fin, procent_loss)
    # print("Result TAB \n", df.head(), "\n")
    print('profit = ', profit)

    path_bot_i = path_file(path_bot, i + 1)
    df.to_csv(path_bot_i, sep = ';', index=False,)
    print("Файл создан: ", path_bot_i, "\n")

    # result_df = df[['Date','total_profit']]
    # print(result_df)

duration = timer() - start
print('Время обработки алгоритма = ', duration)