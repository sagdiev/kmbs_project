from datetime import date, datetime, timedelta
from typing import Dict


# input main
ticker = 'TSLA'
#ticker = str(input('Input ticker: '))


STOCHASTIC_PROCESS_TYPES: Dict[str, int] = {
    'ARMA': 0,
    'GARCH': 1,
    'GBM': 2,
    'OUP': 3,
    'CEV': 4
}
print(STOCHASTIC_PROCESS_TYPES)

BOT_TYPES: Dict[str, int] = {
    'MARTINGALE': 0,
    'ANTIMARTINGALE': 1
}
print(BOT_TYPES)

#type_stochastic_process = ['arma', 'garch', 'gbm', 'oup', 'cev']
#print(type_stochastic_process[0])

# main constants

period = 365 # период, на котором рассматриваем поведение бота
dt = 1 # единица времени, пучть будет 1 день
count_experiments_global = 100 # к-во экспериментов - сгенерированных крывых
path_folder = 'data_research/'
path_file = 'outfile'

# date calculation
date_today = date.today()
date_today_format = date_today.strftime("%Y_%m_%d")
print("date_today =", date_today)

date_year_start = 2020
date_month_start = 12
date_day_start = 4
date_experiment_start = datetime(date_year_start, date_month_start, date_day_start)
date_experiment_start_format = date_experiment_start.strftime("%Y_%m_%d")
print("date_today - 1 day =", date_today - timedelta(days=1) )
print("date_today - 1 day =", date_experiment_start - timedelta(days=1) )

# file name
file_input = '/data_src/total_df_coin.csv'
file_result = '/data_result/result_' + ticker + '_' + date_today_format + '.csv'
file_result_sandbox = '/data_result/result_sandbox_' + date_today_format + '.csv'
print("file_result =", file_result)
print("file_result_sandbox =", file_result_sandbox)



