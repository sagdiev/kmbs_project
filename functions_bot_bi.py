import numpy as np
import pandas as pd
from timeit import default_timer as timer
# from pandas_datareader import data, wb

from constants import *
from bot_generator import *
from funtions_path_file_generator import *
from functions_base import *


def bot_bi_preparation_weight(experiment_def, prefix_experiment_def, weight_def):
    """
    обработка по составлению файла data_bi/experiment_NN_weight_exp_NN
    Портфеля ботов с заданными весами, но не сведенного общего по дням,
    а с детализацией по каждому тикеру
    """
    start = timer()

    # папки и файлы
    path_bot = path_file_without_prefix(PATH_FOLDER_BOT, PATH_FILE_BOT, experiment_def, TICKER)
    path_folder_bi = folder_check(PATH_FOLDER_BI)
    path_bi = path_folder_bi + '/' + experiment_def + str(prefix_experiment_def) +'.csv'
    print(path_bi)

    r = file_clear(path_bi)

    # старт применения алгоритма бота
    param_dict_list = random_bot_parameters_seed(COUNT_RANDOM_PARAMETERS_EXPERIMENTS, SEED_EXPERIMENT)
    print('\nВСЕ ПАРАМЕТРЫ ЭКСПЕРИМЕНТА = ', param_dict_list)
    i_cumulative_param = 0

    for param_dict in param_dict_list:
        with open(path_bi, 'a') as f:

            for i in range (COUNT_EXPERIMENTS_GLOBAL):

                # считываение файлов кривых
                path_bot_i = path_file(path_bot, i + i_cumulative_param + 1)
                df = pd.read_csv(path_bot_i, sep=',')

                df = date_drop_in_df(df, DATE_EXPERIMENT_START, DATE_EXPERIMENT_FINISH)
                df.reset_index(drop=True, inplace=True)

                df['curve_number'] = 'curve_' + str(i + 1)
                df['ticker'] = TICKER_HISTORY_LIST[i]
                df['equity_line'] = df['total_profit'] + df['reserved_sum_investment']

                df['return'] = df['day_profit'] / df['reserved_sum_investment']
                # TODO df['return_log'] = np.log(df['return'])
                # print(df['return_log'])
                # df['return_log'] = np.log( (df['day_profit'] + df['reserved_sum_investment'] ) / df['reserved_sum_investment'] )

                df['parameter_number'] = int( i_cumulative_param / COUNT_EXPERIMENTS_GLOBAL + 1 )
                print (int(i_cumulative_param / COUNT_EXPERIMENTS_GLOBAL + 1))

                # довавление весов для тикеров
                weight = [x / sum(weight_def) for x in weight_def]
                print(weight)

                # применение коэффициентов весов для всех полей, к которым такие веса относятся
                for y in range(len(COLUMNS_WEIGHT_IMPACTED)):
                    print('weight[i] ', i, 'i ', weight[i])
                    df[COLUMNS_WEIGHT_IMPACTED[y]] = df[COLUMNS_WEIGHT_IMPACTED[y]] * weight[i]

                df.to_csv(f, index=False) if i == 0 else df.to_csv(f, index=False, header=0)

            i_cumulative_param += COUNT_EXPERIMENTS_GLOBAL  # кумулятивный индекс для работы с рандомными параметрами

    # таймер
    duration = timer() - start
    print('Время обработки алгоритма = ', duration)

    return df

# # start test
# bot_bi_preparation_weight(EXPERIMENT, TICKER_WEIGHT)
# weight_def = [3 , 2/3]
# weight = [x / sum(weight_def) for x in weight_def]
# print(weight)