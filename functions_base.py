import numpy as np
import pandas as pd
from datetime import datetime
import random
import itertools

from constants import *
from bot_generator import *
from functions_parameters_generator import *
from funtions_path_file_generator import *


def date_convert(date_string):
    # конвертация из текстового типа записи в дату
    datetime_object = datetime.strptime(date_string, '%m/%d/%Y')

    return datetime_object


def date_convert_inverse(datetime_object):
    # конвертация из даты в текстовый вид
    date_string = datetime_object.strftime('%m/%d/%Y')

    return date_string


def find_last_days_year(df_def):

    time_list = df_def['Time'].to_list()

    date_start = date_convert(time_list[0])
    date_end = date_convert(time_list[-1])

    year_start = date_start.year
    year_end = date_end.year

    date_last_list = []
    date_first_list = []
    year_list = []

    for year_i in range(year_start, year_end + 1):
        item_in_year = [x for x in time_list
                        if date_convert(x) >= datetime(year_i, 1, 1)
                        and date_convert(x) < datetime(year_i + 1, 12, 31)]
        # print(date_convert(min(item_in_year)))
        # print('item_in_year = ', item_in_year)
        date_first = min(item_in_year)
        date_last = max(item_in_year)
        date_first_list.append(date_first)
        date_last_list.append(date_last)
        year_list.append(year_i)
        # item_in_year = [date_convert(x) for x in time_list]
        # print(r)
        # item_in_year = date_convert(item_in_year_str)
        # list_last_days.append(min(item_in_year))
        # date_last_list[year_i] = date_last
        # date_first_list[year_i] = date_first
    # print(date_last_list)
    # print(date_first_list)

    return date_first_list, date_last_list, year_list


def rolling_std(df_def):
    # расчет скользящего среднего приведенного к годовому c окном WINDOW_ROLLING_STD
    # ВНИМАНИЕ! первый период временно обогощается средними данными периода - в идеале надо наполнять историческими данными прошлых периодов
    global WINDOW_ROLLING_STD

    rolling_std_calc = df_def['Open'].pct_change().rolling(WINDOW_ROLLING_STD).std(ddof=0)
    rolling_std = np.mean(rolling_std_calc)

    # первый период обогощаем средними данными периода
    for i in range(WINDOW_ROLLING_STD):
        rolling_std_calc[i] = rolling_std

    return rolling_std_calc


def date_drop_in_df(df_def, date_start_def, date_finish_def):
    # отсекаем лишние периоды
    date_list = df_def['Time'].unique().tolist()
    df_dated = pd.DataFrame()
    for j in range(len(date_list)):
        date_j = date_list[j]
        date_j_converted = date_convert(date_j)
        if date_j_converted >= date_finish_def or date_j_converted <= date_start_def:
            df_def.drop(df_def[df_def['Time'] == date_j].index, axis=0, inplace=True)

    return df_def


def random_weights_seed(count_items_portfolio, seed_for_random):
    random.seed(seed_for_random)
    random_portfolio_weights = random.sample(range(100), count_items_portfolio)
    random_portfolio_weights = [ x / sum(random_portfolio_weights) for x in random_portfolio_weights]

    return random_portfolio_weights


def random_portfolio_weights_list_seed(count_portfolios , count_items_portfolio, seed_for_random):
    weight_zero = [0] * count_items_portfolio
    portfolio_weights = []
    type_weights =[]

    # одинаковые веса
    native_weights = [ 1 / count_items_portfolio ] * count_items_portfolio
    portfolio_weights.append(native_weights)
    type_weights.append('native_portfolio')

    # единичные веса
    # for i in range(count_items_portfolio):   todo вернуть назад
    for i in range(count_items_portfolio - 55):
        weights_ones_i = weight_zero
        weights_ones_i = [ 1 if k == i else weight_zero[k] for k in range(count_items_portfolio)]
        # print(weights_ones_i)
        portfolio_weights.append(weights_ones_i)
        # print(portfolio_weights)
        type_weights.append('single_bot')

    # случайные веса
    # for j in range(count_portfolios - count_items_portfolio):     todo вернуть назад
    for j in range(count_portfolios - count_items_portfolio + 55):
        random_portfolio_weights = random_weights_seed(count_items_portfolio, seed_for_random)
        portfolio_weights.append(random_portfolio_weights)
        type_weights.append('random_portfolio')
        seed_for_random += 1

    return portfolio_weights, type_weights


def logbook_text_compelling(running_file_def, param_dict_list_def):
    logbook_text_def = '\n\n\n' + \
        '==========================================================================================================' + \
        '\n\n' \
        '\nЭКСПЕРИМЕНТ: ' + str(EXPERIMENT) + \
        '\nВРЕМЯ НАЧАЛА: ' + str(date.today()) + \
        '\nИНИЦИИРУЮЩИ ФАЙЛ: ' + str(running_file_def) + \
        '\nСПИСОК АКТИВОВ: ' + str(TICKER_HISTORY_LIST) + \
        '\nПЕРВЫЙ ПАРАМЕТР: ' + str(param_dict_list_def[0]) + \
        '\nВСЕ ПАРАМЕТРЫ ЭКСПЕРИМЕНТА: ' + str(param_dict_list_def) + \
        '\nКОЛИЧЕСТВО ЭКСПЕРИМЕНТОВ ПАРАМЕТРОМ: ' + str(COUNT_RANDOM_PARAMETERS_EXPERIMENTS) + \
        '\nКОЛИЧЕСТВО ЭКСПЕРИМЕНТОВ С ВЕСАМИ: ' + str(COUNT_WEIGHT_EXPERIMENTS) + \
        '\nКОЭФФИЦИЕНТ СЛУЧАНОСТИ: ' + str(SEED_EXPERIMENT) + \
        '\nDATE_EXPERIMENT_START:' + str(DATE_EXPERIMENT_START) + \
        '\nDATE_EXPERIMENT_FINISH: ' + str(DATE_EXPERIMENT_FINISH)

    with open('experiments_logbook.txt', 'a') as file:
        file.write(logbook_text_def)

    return logbook_text_def


def logbook_text_compelling_start_algorithm(running_file_def):
    logbook_text_def = '\n' \
        '\nИНИЦИИРУЮЩИЙ ФАЙЛ ЗАПУЩЕН: ' + str(running_file_def) + \
        '\nЭКСПЕРИМЕНТ: ' + str(EXPERIMENT) + \
        '\nВРЕМЯ НАЧАЛА АЛГОРИТМА: ' + str(datetime.today())

    with open('experiments_logbook.txt', 'a') as file:
        file.write(logbook_text_def)

    return logbook_text_def


def logbook_text_compelling_finish_algorithm(running_file_def, duration_def):
    logbook_text_def = '\nВРЕМЯ ЗАВЕРШЕНИЯ АЛГОРИТМА: ' + str(duration_def / 60) + ' минут'

    with open('experiments_logbook.txt', 'a') as file:
        file.write(logbook_text_def)

    return logbook_text_def


def convert_day_stock_df_to_week(df_def):
    # TODO не завершено -доделать позже
    # Converting date to pandas datetime format
    df_def['Time'] = pd.to_datetime(df_def['Time'])

    df_def['Week_Number'] = df_def['Time'].dt.week
    df_def['Month'] = df_def['Time'].dt.month
    df_def['Year'] = df_def['Time'].dt.year

    for i in range(len(df_def)):
        df_def.loc[i, 'Time'] = date_convert_inverse(df_def.loc[i, 'Time'] )

    # Grouping based on required values

    df_result = df_def.groupby(['Year', 'Month', 'Week_Number']).agg(
        {'Time': 'first',
         'Open': 'first',
         'day_profit_unrealized_pnl': 'sum',
         'reserved_sum_investment': 'last',
         'day_profit': 'sum',
         'total_profit': 'last',
         'count_buy': 'last'})

    print(df_result)
    # df_result = df_agg.copy()
    # df2 = df_def.groupby(['Year', 'Week_Number']).agg(
    #     {'Open': 'first',
    #      'High': 'max',
    #      'Low': 'min',
    #      'Close': 'last',
    #      'day_profit_unrealized_pnl': 'sum'})

    # for i in range(0,len(df_result)):
    #     print(i)
    #     print('len(df_result) ', len(df_result))
    #     print(df_result.loc[i, 'Time'])
    #     df_result.loc[i, 'Time'] = date_convert_inverse(df_result.loc[i, 'Time'] )



    df_result.to_csv('Weekly_OHLC.csv')
    print('*** Program ended ***')

    print(df_result)

    return df_result


def convert_day_stock_df_to_month(df_def):
    # TODO не завершено -доделать позже
    # Converting date to pandas datetime format
    df_def['Time'] = pd.to_datetime(df_def['Time'])

    # df_def['Week_Number'] = df_def['Time'].dt.week
    df_def['Month'] = df_def['Time'].dt.month
    df_def['Year'] = df_def['Time'].dt.year

    # Grouping based on required values
    df2 = df_def.groupby(['Year', 'Month']).agg(
        {'Time': 'first',
         'Open': 'first',
         'day_profit_unrealized_pnl': 'sum',
         'reserved_sum_investment': 'last',
         'total_profit': 'last'})

    # df2 = df_def.groupby(['Year', 'Week_Number']).agg(
    #     {'Open': 'first',
    #      'High': 'max',
    #      'Low': 'min',
    #      'Close': 'last',
    #      'day_profit_unrealized_pnl': 'sum'})

    for i in range(len(df_def)):
        df_def.loc[i, 'Time'] = date_convert_inverse(df_def.loc[i, 'Time'] )

    df2.to_csv('Monthly_OHLC.csv')
    print('*** Program ended ***')

    print(df_def)

# print(random_portfolio_weights_list_seed(20 , 5, 3))


# random_portfolio_weights_seed(5, 3)
#
# random.seed(3)
# random_example = random.sample(range(100), 5)
# print('random_example ', random_example)

# path_bot = path_file_without_prefix(PATH_FOLDER_BOT, PATH_FILE_BOT, EXPERIMENT, TICKER)
#
# rrr = {}
# for i in range(2):
#     path_bot_i = path_file(path_bot, i + 1)
#     df = pd.read_csv(path_bot_i, sep=',')
#     print("Файл считан: ", path_bot_i)
#     print(type(df))
#     rrr[i] = find_last_days_year(df)
#
# print(rrr)


# # df = read_csv('file_name', skiprows=1)
# # df.dropna(axis=0, inplace=True)
# # x = df.loc[:-2]
# # # print(df['Time'][0])
# # # print(df)
# # print(x)
# #
# # # запись в файл бота
# # #     path_bot_i = path_file('test.csv', i + 1)
# #     # path_bot_i = path_file(path_bot, i + 1 + 153)
# # df.to_csv('test.csv', sep=',', index=False)
# # print("Файл создан: ", 'test.csv', "\n")
#
# find_last_days_year(df)

# Для тестов
# datetime_str_start = '09/19/18'
# date_formated = date_convert(datetime_str_start)
# print(date_formated)
# date_string_again = date_convert_inverse(date_formated)
# print(date_string_again)
