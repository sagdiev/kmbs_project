import numpy as np
import pandas as pd
from timeit import default_timer as timer
import matplotlib.pyplot as plt

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

count_weight_experiment = COUNT_WEIGHT_EXPERIMENTS
weight_experiment_i = WEIGHT_START

mean_markowitz_list = []
std_markowitz_list = []

path_folder_bi = folder_check(PATH_FOLDER_BI)
path_bi = path_folder_bi + '/' + EXPERIMENT + '.csv'
print(path_bi)

if len(TICKER_HISTORY_LIST) == 2:

    with open(path_bi, 'a') as f:

        for i in range(count_weight_experiment + 1):
            weight_experiment_i[0] = i / count_weight_experiment
            weight_experiment_i[1] = 1 - i / count_weight_experiment
            print('i = ', i, 'i / count_weight_experiment = ', i / count_weight_experiment, ' : ', weight_experiment_i)

            prefix_experiment_i = '_weight_exp_' + str(i + 1)
            experiment_i = EXPERIMENT

            # подготовка обработки BI (объединение построчно всех bot-файлов в один)
            bot_bi_preparation_weight(experiment_i, prefix_experiment_i, weight_experiment_i)

            # подготовка файла Аналитики (подсчет суммарно действий всех bot'ов)
            df_experiment_summary_i = bot_analytics_summary(experiment_i, prefix_experiment_i)

            return_mean = np.mean(df_experiment_summary_i['return'])
            return_std = np.std(df_experiment_summary_i['return'])
            return_mean_annual = return_mean * YEAR_DAYS
            return_std_annual = return_std * np.sqrt(YEAR_DAYS)

            print(return_mean_annual, return_std_annual)
            mean_markowitz_list.append(return_mean_annual)
            std_markowitz_list.append(return_std_annual)

            df_experiment_summary_i['return_mean_annual'] = return_mean_annual
            df_experiment_summary_i['return_std_annual'] = return_std_annual

            df_experiment_summary_i['weights'] = str(weight_experiment_i)

            weights_tickers = str(TICKER_HISTORY_LIST[0]) + ': ' + str(weight_experiment_i[0]) + ', ' \
                              + str(TICKER_HISTORY_LIST[1]) + ': ' + str(weight_experiment_i[1])
            df_experiment_summary_i['weights_tickers'] = weights_tickers

            df_experiment_summary_i['prefix_experiment'] = str(prefix_experiment_i)



            df_experiment_summary_i.to_csv(f, index=False) if i == 0 else df_experiment_summary_i.to_csv(f, index=False, header=0)

            duration = timer() - start
            print('Время обработки варианта весов  №', i + 1, weight_experiment_i, ' ', duration)

    print(mean_markowitz_list)
    print(std_markowitz_list)
    # plt.scatter(std_markowitz_list, mean_markowitz_list)
    # plt.show()

    plot = figure()
    plot.circle(std_markowitz_list, mean_markowitz_list, size=5)
    output_file('plots/plot_' + EXPERIMENT + '_weight_exp.html')
    show(plot)



else:
    print('Количество активов в эксперименте превышает 2. Измените константы')


# таймер
duration = timer() - start
print('Время обработки алгоритма = ', duration)



# xs = [x[0] for x in li]
# ys = [x[1] for x in li]

#
# # # for j in range(count_weight_experiment):
# # plot = figure()
# # plot.circle(mean_markowitz_list,
# #             std_markowitz_list, size=1)
# # # output_file('pandas.html')
# # show(plot)



