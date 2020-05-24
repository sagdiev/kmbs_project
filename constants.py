from datetime import date, datetime, timedelta
from typing import Dict

from constants_tickers import *

# input main
EXPERIMENT = 'experiment_35_multi_rebalance_own'
EXPERIMENT_TYPES = ['HISTORY', 'GBM', 'GBM HISTORY ONE', 'GBM HISTORY TWO', 'ARMA ONE']
EXPERIMENT_TYPE = 'HISTORY'
TICKER = 'history'

# TICKER_HISTORY_LIST = \
#     sp500_2020_05_01_part_1 +\
#     sp500_2020_05_01_part_2 +\
#     sp500_2020_05_01_part_3 +\
#     sp500_2020_05_01_part_4 +\
#     sp500_2020_05_01_part_5 +\
#     sp500_2020_05_01_part_6

# TICKER_HISTORY_LIST = losers_2000
# TICKER_HISTORY_LIST = crypto_history
# TICKER_HISTORY_LIST = ['SPX']
# TICKER_HISTORY_LIST = ['AAPL', 'ABBV', 'BBY', 'ABT', 'ACN', 'F', 'C']
# TICKER_HISTORY_LIST = ['AAPL', 'F', 'C']
TICKER_HISTORY_LIST = ['AMD', 'AMCR']
# TICKER_HISTORY_LIST = ['AABA_TEST']
# TICKER_HISTORY_LIST = ['C']


# print('len TICKER_HISTORY_LIST = ', len(TICKER_HISTORY_LIST))

# STOCHASTIC_PROCESS_TYPES: Dict[str, int] = {
#     'ARMA': 0,
#     'GARCH': 1,
#     'GBM': 2,
#     'OUP': 3,
#     'CEV': 4
# }
# print(STOCHASTIC_PROCESS_TYPES)
#
# BOT_TYPES: Dict[str, int] = {
#     'MARTINGALE': 0,
#     'ANTIMARTINGALE': 1
# }
# print(BOT_TYPES)

# type_stochastic_process = ['arma', 'garch', 'gbm', 'oup', 'cev']
# print(type_stochastic_process[0])

# main constants

PERIOD = 252*5  # период, на котором рассматриваем поведение бота
DT = 1  # единица времени, пучть будет 1 день

# count_experiments_global = 50 # к-во экспериментов - сгенерированных крывых
COUNT_EXPERIMENTS_GLOBAL = len(TICKER_HISTORY_LIST)  # к-во экспериментов - сгенерированных крывых

WINDOW_ROLLING_STD = 252  # окно скользящего стреднего для оптимизации параметров бота при следующем старте

# настройки путей папок и файлов
PATH_FOLDER_CURVE = 'data_curve'
PATH_FILE_CURVE = 'curve'
PATH_FOLDER_BOT = 'data_bot'
PATH_FOLDER_BOT_ANALYTIC = 'data_bot_analytic'
PATH_FILE_BOT = 'bot'
PATH_FOLDER_BI = 'data_bi'
PATH_FOLDER_HISTORY = 'data_history'

# date calculation now
# date_today = date.today()
# # date_today_format = date_today.strftime("%Y_%m_%d")

DATE_LIST_ETALON = DATE_LIST_ETALON_TICKERS

# # date calculation start of experiment
date_year_start = 2020
date_month_start = 5
date_day_start = 1
DATE_EXPERIMENT_START = datetime(date_year_start, date_month_start, date_day_start)
# date_experiment_start_format = date_experiment_start.strftime("%Y_%m_%d")

# Базоыве параметы бота, на основе которых определюяются относительные параметры всех ботов

# PROCENT_BASE = [0, 0.05, 0.10, 0, 0]  # эксперимент
# PROCENT_BASE = [0, 0.15, 0.20, 0, 0]  # эксперимент
PROCENT_BASE = [0, 0.10, 0.15, 0, 0]  # эксперимент
# PROCENT_BASE = [0, 0.07, 0.14, 0, 0]  # эксперимент
# PROCENT_BASE = [0, 0.035, 0.07, 0, 0]  # эксперимент
# PROCENT_BASE = [0, 0.15, 0.20, 0.25, 0.30]  # эксперимент

R_BASE = 5
R_FIN_BASE = 7
PROCENT_LOSS_BASE = 3

# параметры биржи
FEE = 7  # стоимость одного выполненного ордера на бирже

# experiment_22_history = PROCENT_BASE = [0, 0.07, 0.14] total_bot = 10000, 5, 7, 3
# experiment_23_history = PROCENT_BASE = [0, 0.05, 0.10] total_bot = 10000, 5, 7, 3
# experiment_24_history = PROCENT_BASE = [0, 0.15, 0.20] total_bot = 10000, 5, 7, 3
# experiment_25_history = PROCENT_BASE = [0, 0.10, 0.15] total_bot = 10000, 5, 7, 3


# experiment_30_losers_2000 = PROCENT_BASE = [0, 0.10, 0.15] total_bot = 10000, 5, 7, 3 losers
# experiment_31_spx = PROCENT_BASE = [0, 0.10, 0.15] total_bot = 10000, 5, 7, 3 losers

