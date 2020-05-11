from datetime import date, datetime, timedelta
from typing import Dict


# input main
EXPERIMENT = 'experiment_16_history'
TICKER = 'history'
# ticker = 'history_currency'

# history_ticker = ['aapl', 'amzn', 'bac', 'brk.b', 'c', 'f', 'fb', 'goog', 'googl',
#                   'msft',  'nflx', 'pfe', 't', 'xom']

# history_SP500_ticker_1 = ['AAPL', 'ABBV', 'ABT', 'ACN', 'ADBE', 'AMGN', 'AMZN', 'AVGO', 'AXP',
#                   'BA', 'BAC', 'BKNG', 'BLK', 'BMY', 'BRK.B',
#                   'C', 'CAT', 'CB', 'CELG', 'CHTR', 'CMCSA', 'COP', 'COST', 'CRM', 'CSCO', 'CVS', 'CVX',
#                   'DIS', 'FB', 'GE', 'GILD', 'GOOG', 'GOOGL', 'GS', 'HD', 'HON', 'IBM', 'INTC',
#                   'JNJ', 'JPM', 'KO', 'LLY', 'LMT', 'LOW',
#                   'MA', 'MCD', 'MDLZ', 'MDT', 'MMM', 'MO', 'MRK', 'MS', 'MSFT', 'MU', 'NEE', 'NFLX', 'NKE', 'NVDA',
#                   'ORCL', 'PEP', 'PFE', 'PG', 'PM', 'PNC', 'PYPL', 'QCOM', 'SBUX', 'SCHW', 'SLB',
#                   'T', 'TMO', 'TWX', 'TXN', 'UNH', 'UNP', 'UPS', 'USB', 'V', 'VZ', 'WFC', 'WMT', 'XOM']
#
# history_SP500_ticker_2 = ['ADP', 'AGN', 'AIG', 'AMAT', 'AMT', 'ANTM', 'AON', 'APD', 'ATVI',
#                   'BDX', 'BIIB', 'BK', 'BSX', 'CCI', 'CI', 'CL', 'CME', 'COF', 'CSX', 'CTSH',
#                   'D', 'DAL', 'DE', 'DHR', 'DUK', 'EA', 'EBAY', 'EMR', 'EOG', 'ESRX', 'ETN', 'EXC',
#                   'F', 'FDX', 'FOXA', 'GD', 'GM', 'HAL', 'HPQ', 'HUM',
#                   'ICE', 'ILMN', 'INTU', 'ISRG', 'ITW', 'JCI', 'KHC', 'KMB', 'LRCX',
#                   'MAR', 'MET', 'MMC', 'NOC', 'NSC', 'OXY', 'PRU', 'PSX',
#                   'SO', 'SPG', 'SPGI', 'STT', 'STZ', 'SYK', 'TEL', 'TGT', 'TJX', 'TRV',
#                   'VLO', 'VRTX', 'WBA', 'ZTS']
#
# history_SP500_ticker_3 = ['A', 'AAL', 'AAP', 'ABC', 'ABMD', 'ADI', 'ADM', 'ADS', 'ADSK', 'AEE', 'AEP',
#                     'AFL', 'AIV', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALK', 'ALL', 'ALLE', 'ALXN',
#                     'AMCR', 'AMD', 'AME', 'AMP', 'ANET', 'ANSS', 'AOS', 'APA', 'APH', 'APTV', 'ARE',
#                     'ATO', 'AVB', 'AVY', 'AWK', 'AZO', 'BAX', 'BBY', 'BF.B', 'BKR', 'BLL', 'BR', 'BWA', 'BXP',
#                     'CDNS', 'CHRW', 'COG', 'CPB', 'ECL', 'LNT', 'LYB', 'PGR', 'SHW', 'WM']
#
# history_ticker = history_SP500_ticker_1 + history_SP500_ticker_2 + history_SP500_ticker_3

# history_ticker = history_SP500_ticker_1

TICKER_HISTORY_LIST = ['AAPL', 'ABBV', 'BBY']
# history_ticker = ['t']
#ticker = str(input('Input ticker: '))

# history_ticker = ['^USDZAR', '^USDAUD', '^USDCAD', '^USDCHF', '^USDDKK', '^USDEUR', '^USDGBP', '^USDJPY', '^USDNOK', '^USDSEK', '^USDSGD']


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

#type_stochastic_process = ['arma', 'garch', 'gbm', 'oup', 'cev']
#print(type_stochastic_process[0])

# main constants

PERIOD = 365*5 # период, на котором рассматриваем поведение бота
DT = 1 # единица времени, пучть будет 1 день

# count_experiments_global = 50 # к-во экспериментов - сгенерированных крывых
COUNT_EXPERIMENTS_GLOBAL = len(TICKER_HISTORY_LIST)

PATH_FOLDER_CURVE = 'data_curve'
PATH_FILE_CURVE = 'curve'

PATH_FOLDER_BOT = 'data_bot'
PATH_FILE_BOT = 'bot'

PATH_FOLDER_BI = 'data_bi'

PATH_FOLDER_HISTORY = 'data_history'



# date calculation now
# date_today = date.today()
# # date_today_format = date_today.strftime("%Y_%m_%d")

# # date calculation start of experiment
date_year_start = 2020
date_month_start = 5
date_day_start = 1
DATE_EXPERIMENT_START = datetime(date_year_start, date_month_start, date_day_start)
# date_experiment_start_format = date_experiment_start.strftime("%Y_%m_%d")



# Базоыве параметы бота, на основе которых определюяются относительные параметры всех ботов
PROCENT_BASE = [0, 0.15, 0.20, 0.25, 0.30]
R_BASE = 5
R_FIN_BASE = 4
PROCENT_LOSS_BASE = 3


