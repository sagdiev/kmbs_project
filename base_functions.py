import numpy as np
import pandas as pd
from datetime import datetime

from constants import *
from bot_generator import *
from path_file_generator import *


def date_convert(date_string):
    # конвертация из текстового типа записи в дату
    datetime_object = datetime.strptime(date_string, '%m/%d/%Y')

    return datetime_object


def date_convert_inverse(datetime_object):
    # конвертация из даnы в текстовый вид
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
    rolling_std_mean = np.mean(rolling_std_calc)

    for i in range(WINDOW_ROLLING_STD):  # первый период обогощаем средними данными периода
        rolling_std_calc[i] = rolling_std_mean

    return rolling_std_calc


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
