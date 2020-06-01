import numpy as np
import pandas as pd
from timeit import default_timer as timer
# from pandas_datareader import data, wb

from constants import *
from bot_generator import *
from path_file_generator import *
from base_functions import *


# START
start = timer()

# папки и файлы
path_bot = path_file_without_prefix(PATH_FOLDER_BOT, PATH_FILE_BOT, EXPERIMENT, TICKER)
path_folder_bi = folder_check(PATH_FOLDER_BI)
path_bi = path_folder_bi + '/' + EXPERIMENT +'.csv'
print(path_bi)

r = file_clear(path_bi)

# старт применения алгоритма бота

# считываение файлов дополнительной информации о тикерах
df_ticker_info = pd.read_csv(PATH_FILE_TICKER_INFO, sep=',')
print("Файл считан: ", PATH_FILE_TICKER_INFO)
print(df_ticker_info)

with open(path_bi, 'a') as f:

    for i in range (COUNT_EXPERIMENTS_GLOBAL):

        # считываение файлов кривых
        path_bot_i = path_file(path_bot, i + 1)
        df = pd.read_csv(path_bot_i, sep=',')
        # print("Файл считан: ", path_bot_i)
        # print(df)

        df['curve_number'] = 'curve_' + str(i + 1)
        df['ticker'] = TICKER_HISTORY_LIST[i]
        df['equity_line'] = df['sum_invested'] + df['reserved_sum_investment']
        df['return'] = df['equity_line'].pct_change()

        # довавление весов для тикеров
        weight = [x / sum(TICKER_WEIGHT) for x in TICKER_WEIGHT]
        print(weight)

        # print(df['total_profit'])
        # df['total_profit'] = df['total_profit'] * weight[i]
        # print(df['total_profit'])

        for y in range(len(COLUMNS_WEIGHT_IMPACTED)):
            print(df[COLUMNS_WEIGHT_IMPACTED[y]])
            df[COLUMNS_WEIGHT_IMPACTED[y]] = df[COLUMNS_WEIGHT_IMPACTED[y]] * weight[i]
            print(df[COLUMNS_WEIGHT_IMPACTED[y]])

        # добавление сектора
        for j in range(1,len(df_ticker_info)):
                # print(j)
                ticker_sector = str(df_ticker_info['sector'][j])
                # print(j, ticker_sector)
                ticker_symbol = str(df_ticker_info['symbol'][j])
                if df.loc[0, 'ticker'] == ticker_symbol:
                    # print(df['ticker'][0], ticker_symbol, ticker_sector)
                    df['sector'] = ticker_sector
                    print(df['ticker'][0], df['sector'][0], '<=', ticker_symbol, ticker_sector)


        df.to_csv(f, index=False) if i == 0 else df.to_csv(f, index=False, header=0)

# таймер
duration = timer() - start
print('Время обработки алгоритма = ', duration)