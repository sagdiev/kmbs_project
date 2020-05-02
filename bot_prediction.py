import numpy as np
import os
import matplotlib.pyplot as plt
import stochastic.continuous
import stochastic.diffusion
from constants import *
from bot_generator import *


import pandas as pd
import math as m
import numpy as np
from timeit import default_timer as timer


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def file_curve_i(prefix_def):
    file_curve_i = file_folder_curve_ticker + '/' + file_curve + '_' + str(prefix_def) + '.csv'

    return file_curve_i

def file_bot_result_i(prefix_def):
    file_bot_result_i = file_folder_bot_result_ticker + '/' + file_bot_result + '_' + str(prefix_def) + '.csv'

    return file_bot_result_i


def file_folder_bot_result_ticker(ticker_def): # создание папки, если еще не существует

    file_ticker = file_folder_bot_result + '/' + ticker_def
    dirName = file_ticker

    try:
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")

    return file_ticker

# START
start = timer()


file_folder_curve = 'data_curve/'
file_folder_curve_ticker = file_folder_curve + '/' + ticker
file_curve = 'curve'

file_folder_bot_result = 'data_result/'
file_folder_bot_result_ticker = file_folder_bot_result_ticker(ticker)
file_bot_result = 'result'

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

    df = pd.read_csv(file_curve_i(i + 1), sep=',')
    print("Файл считан: ", file_curve_i(i + 1))
    # print("Стартовая цена: \n", df['Price'][0],"\n")

    df, profit = bot_martingale(df, amounts_S, procent, r, r_fin, procent_loss)
    # print("Result TAB \n", df.head(), "\n")
    print('profit = ', profit)

    df.to_csv(file_bot_result_i(i + 1), sep = ';', index=False,)
    print("Файл создан: ", file_bot_result_i(i + 1), "\n")

    # result_df = df[['Date','total_profit']]
    # print(result_df)

duration = timer() - start
print('Время обработки алгоритма = ', duration)