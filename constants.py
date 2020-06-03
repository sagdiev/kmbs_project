from datetime import date, datetime, timedelta
from typing import Dict

from constants_tickers import *

# input main
EXPERIMENT = 'experiment_54_history'
# EXPERIMENT = 'experiment_41_multi_rebalance_own'
# EXPERIMENT_TYPES = ['HISTORY', 'GBM', 'GBM HISTORY ONE', 'GBM HISTORY TWO', 'ARMA ONE']
EXPERIMENT_TYPE = 'HISTORY'
TICKER = 'history'

# TICKER_HISTORY_LIST = \
#     sp500_2020_05_01_part_1 +\
#     sp500_2020_05_01_part_2 +\
#     sp500_2020_05_01_part_3 +\
#     sp500_2020_05_01_part_4 +\
#     sp500_2020_05_01_part_5 +\
#     sp500_2020_05_01_part_6

# TICKER_HISTORY_LIST = sp500_2020_05_01_part_1
# TICKER_HISTORY_LIST = portfolio_selected_from_2000_2020
# TICKER_HISTORY_LIST = losers_2000
# TICKER_HISTORY_LIST = crypto_history
# TICKER_HISTORY_LIST = ['SPX']
# TICKER_HISTORY_LIST = ['AAPL', 'ABBV', 'BBY', 'ABT', 'ACN', 'F', 'C']
# TICKER_HISTORY_LIST = ['AAPL', 'F', 'C', 'GE']
TICKER_HISTORY_LIST = ['AMZN', 'AXP']
# TICKER_HISTORY_LIST = ['AAPL', 'F']
# TICKER_HISTORY_LIST = ['AMD', 'AMCR']
# TICKER_HISTORY_LIST = ['AABA_TEST']
# TICKER_HISTORY_LIST = ['C']

# TICKER_WEIGHT = [5, 2, 1, 8]
TICKER_WEIGHT = [1] * len(TICKER_HISTORY_LIST)
COLUMNS_WEIGHT_IMPACTED = [
    'day_profit', 'total_profit', 'count_buy', 'count_total_buy', 'costs_of_bying',
    'sum_invested', 'cost_of_sum_investment', 'reserved_sum_investment', 'count_sell', 'equity_line']

COLUMNS_FOR_SUMMARY = [
    'day_profit', 'total_profit', 'costs_of_bying', 'sum_invested', 'cost_of_sum_investment',
    'reserved_sum_investment', 'equity_line']

PATH_FILE_TICKER_INFO = 'data_src/ticker_info.csv'

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

COUNT_WEIGHT_EXPERIMENTS = 20  # к-во экпериментов с весами Марковица
WEIGHT_START = [0, 1]

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
PROCENT_BASE = [0, 0.10, 0.15, 0.20, 0.25]  # эксперимент
# PROCENT_BASE = [0, 0.07, 0.14, 0, 0]  # эксперимент
# PROCENT_BASE = [0, 0.035, 0.07, 0, 0]  # эксперимент
# PROCENT_BASE = [0, 0.07, 0.11, 0.15, 0]  # эксперимент
# PROCENT_BASE = [0, 0.05, 0.08, 0.12, 0]  # эксперимент
# PROCENT_BASE = [0, 0.12, 0.17, 0.20, 0]  # эксперимент

R_BASE = 5
R_FIN_BASE = 7
PROCENT_LOSS_BASE = 3

POINT_BOT_START = 1
STEP_BOT_START = 4
TOTAL_RESERVED_BOT_START = 10000

# параметры биржи
FEE = 7  # стоимость одного выполненного ордера на бирже

# experiment_22_history = PROCENT_BASE = [0, 0.07, 0.14] total_bot = 10000, 5, 7, 3
# experiment_23_history = PROCENT_BASE = [0, 0.05, 0.10] total_bot = 10000, 5, 7, 3
# experiment_24_history = PROCENT_BASE = [0, 0.15, 0.20] total_bot = 10000, 5, 7, 3
# experiment_25_history = PROCENT_BASE = [0, 0.10, 0.15] total_bot = 10000, 5, 7, 3


# experiment_30_losers_2000 = PROCENT_BASE = [0, 0.10, 0.15] total_bot = 10000, 5, 7, 3 losers
# experiment_31_spx = PROCENT_BASE = [0, 0.10, 0.15] total_bot = 10000, 5, 7, 3 losers

# experiment_42_history = PROCENT_BASE = [0, 0.10, 0.15] total_bot = 10000, 5, 7, 3,  step = 3
# experiment_43_history = PROCENT_BASE = [0, 0.10, 0.15, 0.25] total_bot = 10000, 5, 7, 3,  step = 4
# experiment_44_history = PROCENT_BASE = [0, 0.10, 0.15, 0.25] total_bot = 10000, 10, 15, 5,  step = 4
# experiment_45_history = PROCENT_BASE = [0, 0.15, 0.20, 0.25] total_bot = 10000, 10, 15, 5,  step = 4
# experiment_46_history = PROCENT_BASE = [0, 0.07, 0.11, 0.15] total_bot = 10000, 10, 15, 5,  step = 4
# experiment_47_history = PROCENT_BASE = [0, 0.07, 0.11, 0.15] total_bot = 10000, 5, 7, 3,  step = 4
# experiment_48_history = PROCENT_BASE = [0, 0.05, 0.08, 0.12] total_bot = 10000, 5, 7, 3,  step = 4
# experiment_42_history = PROCENT_BASE = [0, 0.05, 0.08] total_bot = 10000, 5, 7, 3,  step = 3

# experiment_50_history = PROCENT_BASE = [0, 0.07, 0.11] total_bot = 10000, 5, 7, 3,  step = 3
# experiment_51_history = PROCENT_BASE = [0, 0.07, 0.11] total_bot = 10000, 5, 7, 3,  step = 3
# experiment_52_history = PROCENT_BASE = [0, 0.07, 0.11] total_bot = 10000, 5, 7, 3,  step = 3


# experiment_53_history = PROCENT_BASE = [0, 0.07, 0.11] total_bot = 10000, 5, 7, 3,  step = 3 TICKER_HISTORY_LIST = ['AAPL', 'F']
