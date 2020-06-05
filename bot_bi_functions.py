import numpy as np
import pandas as pd
from timeit import default_timer as timer
# from pandas_datareader import data, wb

from constants import *
from bot_generator import *
from path_file_generator import *
from base_functions import *


def bot_bi_preparation_weight(experiment_def, prefix_experiment_def, weight_def):
    start = timer()

    # папки и файлы
    path_bot = path_file_without_prefix(PATH_FOLDER_BOT, PATH_FILE_BOT, experiment_def, TICKER)
    path_folder_bi = folder_check(PATH_FOLDER_BI)
    path_bi = path_folder_bi + '/' + experiment_def + str(prefix_experiment_def) +'.csv'
    print(path_bi)

    r = file_clear(path_bi)

    # старт применения алгоритма бота

    # считываение файлов дополнительной информации о тикерах
    # df_ticker_info = pd.read_csv(PATH_FILE_TICKER_INFO, sep=',')
    # print("Файл считан: ", PATH_FILE_TICKER_INFO)
    # print(df_ticker_info)

    with open(path_bi, 'a') as f:

        for i in range (COUNT_EXPERIMENTS_GLOBAL):

            # считываение файлов кривых
            path_bot_i = path_file(path_bot, i + 1)
            df = pd.read_csv(path_bot_i, sep=',')
            # print("Файл считан: ", path_bot_i)
            # print(df)

            df = date_drop_in_df(df, DATE_EXPERIMENT_START, DATE_EXPERIMENT_FINISH)
            df.reset_index(drop=True, inplace=True)
            # print(df)

            df['curve_number'] = 'curve_' + str(i + 1)
            df['ticker'] = TICKER_HISTORY_LIST[i]
            df['equity_line'] = df['total_profit'] + df['reserved_sum_investment']
            df['return'] = df['equity_line'].pct_change()


            # довавление весов для тикеров
            weight = [x / sum(weight_def) for x in weight_def]
            print(weight)

            # print(df['total_profit'])
            # df['total_profit'] = df['total_profit'] * weight[i]
            # print(df['total_profit'])

            for y in range(len(COLUMNS_WEIGHT_IMPACTED)):
                # print(df[COLUMNS_WEIGHT_IMPACTED[y]])
                print('weight[i] ', i, 'i ', weight[i])
                df[COLUMNS_WEIGHT_IMPACTED[y]] = df[COLUMNS_WEIGHT_IMPACTED[y]] * weight[i]
                # print(df[COLUMNS_WEIGHT_IMPACTED[y]])

            # добавление сектора
            # for j in range(1,len(df_ticker_info)):
            #         # print(j)
            #         ticker_sector = str(df_ticker_info['sector'][j])
            #         # print(j, ticker_sector)
            #         ticker_symbol = str(df_ticker_info['symbol'][j])
            #         if df.loc[0, 'ticker'] == ticker_symbol:
            #             # print(df['ticker'][0], ticker_symbol, ticker_sector)
            #             df['sector'] = ticker_sector
            #             print(df['ticker'][0], df['sector'][0], '<=', ticker_symbol, ticker_sector)


            df.to_csv(f, index=False) if i == 0 else df.to_csv(f, index=False, header=0)

    # таймер
    duration = timer() - start
    print('Время обработки алгоритма = ', duration)

    return df

# # start test
# bot_bi_preparation_weight(EXPERIMENT, TICKER_WEIGHT)

# weight_def = [3 , 2/3]
# weight = [x / sum(weight_def) for x in weight_def]
# print(weight)