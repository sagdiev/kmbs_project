import numpy as np
import pandas as pd
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import random

# from pandas_datareader import data, wb
from bokeh.io import output_file, show
from bokeh.plotting import figure
# from bokeh.sampledata.iris import flowers

from constants import *
from bot_generator import *
from path_file_generator import *
from base_functions import *
from bot_bi_functions import *
from bot_analytics_functions import *


# START
start = timer()


mean_markowitz_list = []
std_markowitz_list = []

path_folder_bi = folder_check(PATH_FOLDER_BI)
path_bi = path_folder_bi + '/' + EXPERIMENT + '.csv'
print(path_bi)

weights_tickers = ''

try:
    file_clear = open(path_bi,"r+")
    file_clear.truncate(0)
    file_clear.close()
    print('Старый файл ', path_bi, ' очищен')
except Exception:
    print('Файл ', path_bi, ' будет создавться первый раз')

weight_experiment_list, type_weights_list = \
    random_portfolio_weights_list_seed(COUNT_WEIGHT_EXPERIMENTS , len(TICKER_HISTORY_LIST), SEED_EXPERIMENT)

if len(TICKER_HISTORY_LIST) <= COUNT_EXPERIMENTS_GLOBAL:

    with open(path_bi, 'a') as f:

        for i in range(COUNT_WEIGHT_EXPERIMENTS):
            print(TICKER_HISTORY_LIST)
            weights_tickers = ''
            weight_experiment_i = weight_experiment_list[i]

            # всмомогательный вариант равномерного распределения весов в случае двух акций
            # weight_experiment_i[0] = i / count_weight_experiment
            # weight_experiment_i[1] = 1 - i / count_weight_experiment

            prefix_experiment_i = '_weight_exp_' + str(i + 1)
            print('\n\n START expneriment ', prefix_experiment_i)
            print('weight_experiment = ', weight_experiment_i)
            experiment_i = EXPERIMENT

            # подготовка обработки BI (объединение построчно всех bot-файлов в один)
            bot_bi_preparation_weight(experiment_i, prefix_experiment_i, weight_experiment_i)

            # подготовка файла Аналитики (подсчет суммарно действий всех bot'ов)
            df_experiment_summary_i = bot_analytics_summary(experiment_i, prefix_experiment_i)

            # дополнительные расчеты показателей портфеля
            return_mean = np.mean(df_experiment_summary_i['return'])
            return_std = np.std(df_experiment_summary_i['return'])
            return_mean_annual = return_mean * YEAR_DAYS
            return_std_annual = return_std * np.sqrt(YEAR_DAYS)

            print(return_mean_annual, return_std_annual)
            mean_markowitz_list.append(return_mean_annual)
            std_markowitz_list.append(return_std_annual)

            df_experiment_summary_i['return_mean_annual'] = return_mean_annual
            df_experiment_summary_i['return_std_annual'] = return_std_annual
            df_experiment_summary_i['information_ratio'] = return_mean_annual / return_std_annual

            for k in range(len(TICKER_HISTORY_LIST)):
                weights_tickers = \
                    weights_tickers + str(TICKER_HISTORY_LIST[k]) + ': ' + str(round(weight_experiment_i[k],2)) + ','

            df_experiment_summary_i['weights'] = str(weight_experiment_i)
            df_experiment_summary_i['weights_tickers'] = weights_tickers
            df_experiment_summary_i['type_weights'] = type_weights_list[i]

            # записываем файл
            df_experiment_summary_i.to_csv(f, index=False) if i == 0 \
                else df_experiment_summary_i.to_csv(f, index=False, header=0)

            duration = timer() - start
            print('Время обработки варианта весов  №', i + 1, weight_experiment_i, ' ', duration)

    print(mean_markowitz_list)
    print(std_markowitz_list)

    plot = figure()
    plot.circle(std_markowitz_list, mean_markowitz_list, size=5)
    output_file('plots/plot_' + EXPERIMENT + '_weight_exp.html')
    show(plot)

else:
    print('Количество активов в эксперименте превышает 2. Измените константы')

# таймер
duration = timer() - start
print('Время обработки алгоритма = ', duration)
