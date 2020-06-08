import numpy as np
import pandas as pd
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from path_file_generator import *
from parameters_generator import *
from base_functions import *


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

for param_dict in param_dict_list:
    timer_start_parameters = timer()

    print('\n\nСТАРТ РАБОТЫ БОТОВ С ПАРАМЕТРАМИ = ', param_dict)

    # старт применения алгоритма бота
    for i in range(COUNT_EXPERIMENTS_GLOBAL):
        timer_start = timer()
        print('Старт ', i + i_cumulative_param + 1)

        # считываение крывых
        path_curve_i = path_file_history(PATH_FOLDER_HISTORY, TICKER_HISTORY_LIST, i)
        df = pd.read_csv(path_curve_i, sep=',')
        # df.sort_index(ascending=False, inplace=True)
        df = date_drop_in_df(df, DATE_EXPERIMENT_START, DATE_EXPERIMENT_FINISH)
        df.reset_index(drop=True, inplace=True)
        # print("Файл считан: ", path_curve_i)
        # print(df)

        rolling_std_cacl = df['Open'].pct_change().rolling(WINDOW_ROLLING_STD).std(ddof=0)
        rolling_std_mean = np.mean(rolling_std_cacl)
        # x = param_rebalance(param_dict, 0.37195826601590254)
        # print('rolling_std_mean = ', rolling_std_mean)

        # применение бота
        df, profit = bot_martingale(df, param_dict)
        print('profit = ', profit)

        df['Curve'] = str(TICKER_HISTORY_LIST[i])

        # запись в файл бота
        path_bot_i = path_file(path_bot, i  + i_cumulative_param + 1)  # с каждым новым рандомным параметром увеличивается индекс файла
        # path_bot_i = path_file(path_bot, i + 1 + 153)
        df.to_csv(path_bot_i, sep=',', index=False,)
        print("Файл создан: ", path_bot_i)
        # print("Бот: ", path_bot_i, ', profit = ', profit)


        # таймеры
        duration = timer() - timer_start
        print('Время обработки одного бота = ', duration)
        duration = timer() - start
        print('Время обработки всего = ', duration)

    # print(i_cumulative_param)
    i_cumulative_param += COUNT_EXPERIMENTS_GLOBAL
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
