import numpy as np
import pandas as pd
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from funtions_path_file_generator import *
from functions_parameters_generator import *
from functions_base import *
from functions_integral_indicators import *


# START
start = timer()

# генерирование портфелей
param_dict_list = random_bot_parameters_seed(COUNT_RANDOM_PARAMETERS_EXPERIMENTS, SEED_EXPERIMENT)
i_cumulative_param = 0

# записываем данные эксперимента в журнал
running_file = sys.argv[0]
logbook_text = logbook_text_compelling(running_file, param_dict_list)
print(logbook_text)


# папки и файлы
path_bot = path_file_without_prefix(PATH_FOLDER_BOT, PATH_FILE_BOT, EXPERIMENT, TICKER)
# path_curve = path_file_without_prefix(path_folder_curve, path_file_curve, experiment, ticker)
# path_curve = path_file_history_without_prefix(path_folder_history, history_ticker)
create_folder_or_check_existence(path_bot)



 # старт применения алгоритма бота
for i in range(COUNT_EXPERIMENTS_GLOBAL):
    timer_start = timer()
    print('Старт ', i + i_cumulative_param + 1)

    # считываение крывых
    path_curve_i = path_file_history(PATH_FOLDER_HISTORY, TICKER_HISTORY_LIST, i)
    df_i = pd.read_csv(path_curve_i, sep=',')
    # df.sort_index(ascending=False, inplace=True)
    df_i = date_drop_in_df(df_i, DATE_EXPERIMENT_START, DATE_EXPERIMENT_FINISH)
    df_i.reset_index(drop=True, inplace=True)
    # print("Файл считан: ", path_curve_i)
    print(df_i)

    if TRIGGER_OF_CALCULATION_INTEGRAL_INDICATORS_ON_SOURCE_CURVE is True:
        # подсчет интегральных показателей самой акции - просто для сравнения

        df_i['returns_stock_price'] = df_i['Open'].pct_change()  # так оперделяем Returns самой акции без применения бота
        df_i['returns_stock_price_log'] = np.log( 1 +  df_i['returns_stock_price'] )  # используем только логарифмические приросты
        integral_indicators_dict_stock = caclulation_integral_indicators(df_i, 'returns_stock_price_log')
        df_i['stock_mean'] = integral_indicators_dict_stock.get('mean_annual')
        df_i['stock_std'] = integral_indicators_dict_stock.get('std_annual')
        df_i['stock_skew'] = integral_indicators_dict_stock.get('skewness_day')
        df_i['stock_kurt'] = integral_indicators_dict_stock.get('kurtosis_day')
        df_i['stock_information_ratio'] = integral_indicators_dict_stock.get('information_ratio_annual')
        # df_i['stock_sharpe_ratio'] = integral_indicators_dict_stock.get('sharpe_ratio')
        df_i['stock_max_drawdown'] = integral_indicators_dict_stock.get('max_drawdown')
        df_i['stock_VaR_95'] = integral_indicators_dict_stock.get('VaR_95')
        # df_i['stock_CVaR_95'] = integral_indicators_dict_stock.get('CVaR_95')

    # подсчет каждого варианта параметров
    for param_dict in param_dict_list:
        timer_start_parameters = timer()

        print('\n\nСТАРТ РАБОТЫ БОТОВ С ПАРАМЕТРАМИ = ', param_dict)
        print('Старт ', i + i_cumulative_param + 1)

        df = df_i.copy()

        # rolling_std_cacl = df['Open'].pct_change().rolling(WINDOW_ROLLING_STD).std(ddof=0)
        # rolling_std_mean = np.mean(rolling_std_cacl)
        # x = param_rebalance(param_dict, 0.37195826601590254)
        # print('rolling_std_mean = ', rolling_std_mean)

        # применение бота
        df, profit = bot_martingale(df, param_dict)
        print('profit = ', profit)

        df['Curve'] = str(TICKER_HISTORY_LIST[i])

        if TRIGGER_OF_CALCULATION_INTEGRAL_INDICATORS_ON_EACH_BOT is True:
            # подсчет интегральных показателей результатов работы бота
            df['return_bot_procent_simple'] = df['day_profit'] / df['reserved_sum_investment']  # так оперделяем Returns бота
            df['return_bot_procent_log'] = np.log(1 + df['return_bot_procent_simple'])  # используем только логарифмические приросты
            # TODO учесть временные просадки
            # TODO df['return_log'] = np.log(df['return'])
            integral_indicators_dict_bot = caclulation_integral_indicators(df, 'return_bot_procent_log')
            df['bot_mean'] = integral_indicators_dict_bot.get('mean_annual')
            df['bot_std'] = integral_indicators_dict_bot.get('std_annual')
            df['bot_skew'] = integral_indicators_dict_bot.get('skewness_day')
            df['bot_kurt'] = integral_indicators_dict_bot.get('kurtosis_day')
            df['bot_information_ratio'] = integral_indicators_dict_bot.get('information_ratio_annual')
            # df['bot_sharpe_ratio'] = integral_indicators_dict_bot.get('sharpe_ratio')
            df['bot_max_drawdown'] = integral_indicators_dict_bot.get('max_drawdown')
            df['bot_VaR_95'] = integral_indicators_dict_bot.get('VaR_95')
            # df['bot_CVaR_95'] = integral_indicators_dict_bot.get('CVaR_95')


        # запись в файл бота
        path_bot_i = path_file(path_bot, i + i_cumulative_param + 1)  # с каждым новым рандомным параметром увеличивается индекс файла
        # path_bot_i = path_file(path_bot, i + 1 + 153)
        df.to_csv(path_bot_i, sep=',', index=False,)
        print("Файл создан: ", path_bot_i)

        # таймеры
        duration = timer() - timer_start
        print('\nВремя обработки одного бота = ', duration)
        duration = timer() - start
        print('Время обработки всего = ', duration)

        i_cumulative_param += 1



    # print(i_cumulative_param)
    # i_cumulative_param += COUNT_EXPERIMENTS_GLOBAL
    # print(i_cumulative_param)

    # # таймеры
    # duration = timer() - timer_start_parameters
    # print('Время обработки одного типа ПАРАМЕТРОМ = ', duration)
    # duration = timer() - start
    # print('Время обработки всего = ', duration)

# таймер
duration = timer() - start
print('Время обработки всего алгоритма = ', duration)

# записываем данные об окончании в журнал
logbook_text_compelling_finish_algorithm(running_file, duration)
