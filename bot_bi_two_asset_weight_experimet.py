import numpy as np
import pandas as pd
from timeit import default_timer as timer
# from pandas_datareader import data, wb

from constants import *
from bot_generator import *
from path_file_generator import *
from base_functions import *
from bot_bi_functions import *


# START
start = timer()

count_weight_experiment = 10
weight_start = [0, 1]
weight_experiment_i = weight_start


if len(TICKER_HISTORY_LIST) == 2:

    for i in range(count_weight_experiment):
        weight_experiment_i[0] = i / count_weight_experiment
        weight_experiment_i[1] = 1 - i / count_weight_experiment
        print('i = ', i, 'i / count_weight_experiment = ', i / count_weight_experiment, ' : ', weight_experiment_i)

        prefix_experiment_i = '_weight_exp_' + str(i + 1)
        experiment_i = EXPERIMENT
        bot_bi_preparation_weight(experiment_i, prefix_experiment_i, weight_experiment_i)
        # print(TICKER_WEIGHT)

else:
    print('Количество активов в эксперименте превышает 2. Измените константы')

# таймер
duration = timer() - start
print('Время обработки алгоритма = ', duration)