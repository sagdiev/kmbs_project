import numpy as np
import pandas as pd
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from path_file_generator import *
from base_functions import *


def integral_indicators_bot_sigle(df_def, df_integral_total_def, ticker_def):
    # подсчет интегральных показателей результатов работы конкретного бота на конкретной кривой

    # подсчет прибыльности бота по годам
    date_first_list, date_last_list, year_list = find_last_days_year(df_def)

    profit_year_list = []
    profit_start = 0
    profit_end = 0
    return_bot_year_list = []
    reserved_sum_investment_max = df_def['reserved_sum_investment'][0]
    sum_invested_end = 0
    sum_invested_max = max(df_def['sum_invested'])
    cost_sum_invested_end = 0
    cost_sum_invested_list = []
    temporary_down_list =[]
    fee_count_start = 0
    fee_count_year = 0
    fee_count_list = []
    fee_list =[]
    profit_year_corrected_list = []
    profit_year_corrected_fee_list = []

    print(reserved_sum_investment_max)
    print(sum_invested_max)

    for i in range(len(year_list)):
        year_i = year_list[i]
        date_last_i = date_last_list[i]
        fee_count_year = 0

        for j in range(len(df_def)):
            if df_def['Time'][j] == date_last_i:
                profit_end = df_def['total_profit'][j]
                sum_invested_end = df_def['sum_invested'][j]
                cost_sum_invested_end = df_def['cost_of_sum_investment'][j]
                # fee_count_end = df_def['fee_count'][j]
                # TODO переделать на sum когда переведем fee_count из суммы в кол-во
            if date_convert(df_def['Time'][j]).year == year_i:
                # print(date_convert(df_def['Time'][j]).year)
                fee_count_year = fee_count_year + df_def['fee_count'][j]
                print(fee_count_year)

        temporary_down_end = cost_sum_invested_end - sum_invested_end
        fee_end = fee_count_year * FEE

        profit_year = profit_end - profit_start
        profit_year_corrected = profit_year + temporary_down_end
        profit_year_corrected_fee = profit_year_corrected - fee_end
        profit_start = profit_end

        profit_year_list.append(profit_year)
        cost_sum_invested_list.append(cost_sum_invested_end)
        temporary_down_list.append(temporary_down_end)
        fee_count_list.append(fee_count_year)
        fee_list.append(fee_end)
        profit_year_corrected_list.append(profit_year_corrected)
        profit_year_corrected_fee_list.append(profit_year_corrected_fee)

        # sum_invested_max = max([df_def['sum_invested'][j]
        #                         for j in range(len(df_def))
        #                         if date_convert(df_def['Time'][j]).year == year_i])
        #
        # print(reserved_sum_investment_max)
        # print(sum_invested_max)

        return_bot_year_i = profit_year/reserved_sum_investment_max
        return_bot_year_list.append(return_bot_year_i)
        print('return_bot_year ', year_i, '= ', return_bot_year_i)

        # year_profit_end = [df_def['total_profit'][j] for j in range(len(df_def)) if df_def['Time'][j] == date_last_i][0]

    return_bot_year_mean = np.mean(return_bot_year_list)
    return_bot_year_std = np.std(return_bot_year_list)
    sharpe = return_bot_year_mean/return_bot_year_std
    # print('return_bot_year_list = ', return_bot_year_list)
    # print('return_bot_year_mean = ', return_bot_year_mean)
    # print('return_bot_year_std = ', return_bot_year_std)
    # print('sharpe = ', sharpe)
    # print('year_profit_list = ', year_profit_list)
    # print('total_profit = ', sum(year_profit_list))

    df_integral = pd.DataFrame()
    df_integral['year'] = year_list
    df_integral['return_bot_year'] = return_bot_year_list
    df_integral['profit_year'] = profit_year_list
    df_integral['profit_year_corrected'] = profit_year_corrected_list
    df_integral['profit_year_corrected_fee'] = profit_year_corrected_fee_list
    df_integral['cost_sum_invested'] = cost_sum_invested_list
    df_integral['temporary_down'] = temporary_down_list
    df_integral['fee_count'] = fee_count_list
    df_integral['fee'] = fee_list
    df_integral['ticker'] = ticker_def

    # зпаисть интегральных показателей за весь период работы бота
    total_info_row = {'ticker': ticker_def,
                      'return_bot_year_mean': return_bot_year_mean,
                      'return_bot_year_std': return_bot_year_std,
                      'sharpe': sharpe,
                      'total_profit': sum(profit_year_list)}

    df_integral_total = df_integral_total_def.append(total_info_row, ignore_index=True) # , ignore_index=False

    # TODO Sharpe
    # TODO Information ratio
    # TODO Maximum Dropdown
    # TODO Среднегодовая доходность + Сигма
    # TODO Total Profit

    # print(df_integral)
    # print(df_integral_total)

    return df_integral, df_integral_total


# START
start = timer()

# папки и файлы
path_bi = PATH_FOLDER_BI + '/' + EXPERIMENT + '.csv'

# path_bot = path_file_without_prefix(PATH_FOLDER_BOT, PATH_FILE_BOT, EXPERIMENT, TICKER)
path_folder_analytic = folder_check(PATH_FOLDER_BOT_ANALYTIC)
path_bi_summary = path_folder_analytic + '/' + EXPERIMENT +'_summary.csv'
# path_analytic = path_folder_analytic + '/' + EXPERIMENT +'.csv'
# path_analytic_total = path_folder_analytic + '/' + EXPERIMENT +'_total' + '.csv'
# print(path_analytic)

# r = file_clear(path_analytic)

# старт применения алгоритма бота
# col_names =  ['ticker', 'total_profit', 'return_bot_year_mean', 'return_bot_year_std', 'sharpe']
# df_integral_total  = pd.DataFrame(columns = col_names)

# with open(path_analytic, 'a') as f:
#     with open(path_analytic_total, 'a') as f_total:
#
#         for i in range (COUNT_EXPERIMENTS_GLOBAL):
# timer_start = timer()

# считываение файлы
df = pd.read_csv(path_bi, sep=',')
print("Файл считан: ", path_bi)
print(df)

# df['curve_number'] = 'curve_' + str(i + 1)
# ticker = TICKER_HISTORY_LIST[i]
# weight = [x / sum(TICKER_WEIGHT) for x in TICKER_WEIGHT]
# print(weight)

# print(df['total_profit'])
# df['total_profit'] = df['total_profit'] * weight[i]
# print(df['total_profit'])

df_summary = pd.DataFrame(columns = ['Time'] + COLUMNS_WEIGHT_IMPACTED)

date_list = df['Time'].unique().tolist()
print(date_list)

df_summary['Time'] = date_list
print(df_summary)

# for i in range(len(COLUMNS_FOR_SUMMARY)):
#     column_i = COLUMNS_FOR_SUMMARY[i]
#     # print(df[column_i])

for j in range(len(date_list)):
    date_j = date_list[j]
    print('\n', date_j)
    for i in range(len(COLUMNS_FOR_SUMMARY)):
        column_i = COLUMNS_FOR_SUMMARY[i]
        df_summary.loc[j, column_i] = df.loc[df['Time'] == date_j, column_i].sum()
        print(column_i, df_summary.loc[j, column_i])


    # df[COLUMNS_WEIGHT_IMPACTED[y]] = sum(COLUMNS_WEIGHT_IMPACTED[y])
    # print(df[COLUMNS_WEIGHT_IMPACTED[y]])

# df_integral, df_integral_total = integral_indicators_bot_sigle(df, df_integral_total, ticker)
#
# df_integral.to_csv(f, index=False) if i == 0 else df_integral.to_csv(f, index=False, header=0)
# print(df_integral_total)

# f_total.truncate(0)
df_summary.to_csv(path_bi_summary, index=False)

# таймеры
# duration = timer() - timer_start
# print('Время обработки этапа алгоритма = ', duration)
# duration = timer() - start
# print('Время обработки алгоритма = ', duration)

# таймер
duration = timer() - start
print('Время обработки алгоритма = ', duration)
