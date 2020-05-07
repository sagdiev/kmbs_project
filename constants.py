from datetime import date, datetime, timedelta
from typing import Dict


# input main
experiment = 'experiment_9_history'
ticker = 'history'
# ticker = 'history_currency'

# history_ticker = ['aapl', 'amzn', 'bac', 'bp', 'brk.b', 'c', 'f', 'fb', 'goog', 'googl',
                  # 'jnj', 'jpm', 'msft',  'nflx', 'pfe', 'spx', 't', 'tsla', 'twtr', 'xom']
history_ticker_1 = ['AAPL', 'ABBV', 'ABT', 'ACN', 'ADBE', 'AMGN', 'AMZN', 'AVGO', 'AXP',
                  'BA', 'BAC', 'BKNG', 'BLK', 'BMY', 'BRK.B',
                  'C', 'CAT', 'CB', 'CELG', 'CHTR', 'CMCSA', 'COP', 'COST', 'CRM', 'CSCO', 'CVS', 'CVX',
                  'DIS', 'FB', 'GE', 'GILD', 'GOOG', 'GOOGL', 'GS', 'HD', 'HON', 'IBM', 'INTC',
                  'JNJ', 'JPM', 'KO', 'LLY', 'LMT', 'LOW',
                  'MA', 'MCD', 'MDLZ', 'MDT', 'MMM', 'MO', 'MRK', 'MS', 'MSFT', 'MU', 'NEE', 'NFLX', 'NKE', 'NVDA',
                  'ORCL', 'PEP', 'PFE', 'PG', 'PM', 'PNC', 'PYPL', 'QCOM', 'SBUX', 'SCHW', 'SLB',
                  'T', 'TMO', 'TWX', 'TXN', 'UNH', 'UNP', 'UPS', 'USB', 'V', 'VZ', 'WFC', 'WMT', 'XOM']

history_ticker_2 = ['ADP', 'AGN', 'AIG', 'AMAT', 'AMT', 'ANTM', 'AON', 'APD', 'ATVI',
                  'BDX', 'BIIB', 'BK', 'BSX', 'CCI', 'CI', 'CL', 'CME', 'COF', 'CSX', 'CTSH',
                  'D', 'DAL', 'DE', 'DHR', 'DUK', 'EA', 'EBAY', 'EMR', 'EOG', 'ESRX', 'ETN', 'EXC',
                  'F', 'FDX', 'FOXA', 'GD', 'GM', 'HAL', 'HPQ', 'HUM',
                  'ICE', 'ILMN', 'INTU', 'ISRG', 'ITW', 'JCI', 'KHC', 'KMB', 'LRCX',
                  'MAR', 'MET', 'MMC', 'NOC', 'NSC', 'OXY', 'PRU', 'PSX',
                  'SO', 'SPG', 'SPGI', 'STT', 'STZ', 'SYK', 'TEL', 'TGT', 'TJX', 'TRV',
                  'VLO', 'VRTX', 'WBA', 'ZTS']

history_ticker_3 = ['A', 'AAL', 'AAP', 'ABC', 'ABMD', 'ADI', 'ADM', 'ADS', 'ADSK', 'AEE', 'AEP',
                    'AFL', 'AIV', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALK', 'ALL', 'ALLE', 'ALXN',
                    'AMCR', 'AMD', 'AME', 'AMP', 'ANET', 'ANSS', 'AOS', 'APA', 'APH', 'APTV', 'ARE',
                    'ATO', 'AVB', 'AVY', 'AWK', 'AZO', 'BAX', 'BBY', 'BF.B', 'BKR', 'BLL', 'BR', 'BWA', 'BXP',
                    'CDNS', 'CHRW', 'COG', 'CPB', 'ECL', 'LNT', 'LYB', 'PGR', 'SHW', 'WM']

history_ticker = history_ticker_1 + history_ticker_2 + history_ticker_3
# history_ticker = history_ticker_3

# history_ticker = ['aapl', 'amzn', 'bac', 'twtr']
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

period = 365*5 # период, на котором рассматриваем поведение бота
dt = 1 # единица времени, пучть будет 1 день

# count_experiments_global = 3 # к-во экспериментов - сгенерированных крывых
count_experiments_global = len(history_ticker)

path_folder_curve = 'data_curve'
path_file_curve = 'curve'

path_folder_bot = 'data_bot'
path_file_bot = 'bot'

path_folder_bi = 'data_bi'

path_folder_history = 'data_history'



# date calculation now
date_today = date.today()
# date_today_format = date_today.strftime("%Y_%m_%d")

# date calculation start of experiment
# date_year_start = 2017
# date_month_start = 1
# date_day_start = 1
# date_experiment_start = datetime(date_year_start, date_month_start, date_day_start)
# date_experiment_start_format = date_experiment_start.strftime("%Y_%m_%d")
#



