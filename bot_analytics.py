import numpy as np
import pandas as pd
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from path_file_generator import *
from base_functions import *
from bot_analytics_functions import *


# START
start = timer()

# записываем данные о начале обратоки этого файла в журнал
running_file = sys.argv[0]
logbook_text = logbook_text_compelling_start_algorithm(running_file)
print(logbook_text)

# папки и файлы
path_bot = path_file_without_prefix(PATH_FOLDER_BOT, PATH_FILE_BOT, EXPERIMENT, TICKER)
path_folder_analytic = folder_check(PATH_FOLDER_BOT_ANALYTIC)
path_analytic = path_folder_analytic + '/' + EXPERIMENT +'.csv'
path_analytic_total = path_folder_analytic + '/' + EXPERIMENT +'_total' + '.csv'
# print(path_analytic)

r = file_clear(path_analytic)

# старт применения алгоритма бота
i_cumulative_param = 0
# df_integral_total = pd.DataFrame()
col_names =  ['ticker', 'total_profit', 'return_bot_year_mean', 'return_bot_year_std', 'sharpe']
df_integral_total  = pd.DataFrame(columns = col_names)

with open(path_analytic, 'a') as f:
    with open(path_analytic_total, 'a') as f_total:

        for i in range (COUNT_EXPERIMENTS_GLOBAL):
            timer_start = timer()
            # считываение файлы
            path_bot_i = path_file(path_bot, i  + i_cumulative_param + 1)
            df = pd.read_csv(path_bot_i, sep=',')
            print("Файл считан: ", path_bot_i)
            print(df)

            df['curve_number'] = 'curve_' + str(i + 1)
            ticker = TICKER_HISTORY_LIST[i]
            df['ticker'] = ticker
            df['parameter_number'] = i_cumulative_param / COUNT_EXPERIMENTS_GLOBAL + 1

            df_integral, df_integral_total = integral_indicators_bot_sigle(df, df_integral_total, ticker)

            # записываем результаты дневные по каждой акции
            df_integral.to_csv(f, index=False) if i == 0 else df_integral.to_csv(f, index=False, header=0)
            print(df_integral_total)

            # записываем результаты годовые по всему портфелю
            f_total.truncate(0)
            df_integral_total.to_csv(f_total, index=False)

            # таймеры
            duration = timer() - timer_start
            print('Время обработки этапа алгоритма = ', duration)
            duration = timer() - start
            print('Время обработки алгоритма = ', duration)

        i_cumulative_param += COUNT_EXPERIMENTS_GLOBAL  # кумулятивный индекс для работы с рандомными параметрами

# таймер
duration = timer() - start
print('Время обработки алгоритма = ', duration)

# записываем данные об окончании в журнал
logbook_text_compelling_finish_algorithm(running_file, duration)
