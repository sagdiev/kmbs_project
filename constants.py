from datetime import date

# input main
ticker = 'AAPL'
#ticker = str(input('Input ticker: '))

# main constants
type_stochastic_process = ['arma', 'garch', 'gbm', 'oup', 'cev']
#print(type_stochastic_process[0])

# date calculation
today = date.today()
date_today = today.strftime("%Y_%m_%d")
print("date_today =", date_today)

# file name
file_input = '/data_src/total_df_coin.csv'
file_result = '/data_result/result_' + ticker + '_' + date_today + '.csv'
file_result_sandbox = '/data_result/result_sandbox_' + date_today + '.csv'
print("file_result =", file_result)
print("file_result_sandbox =", file_result_sandbox)



