import pandas as pd
from constants import *
from path_file_generator import *
from base_functions import *


# приведение файлов исторических данных к стандартизированному формату
path_folder_history_source = PATH_FOLDER_HISTORY + '/source'

# считываение файлов дополнительной информации о тикерах
df_ticker_info = pd.read_csv(PATH_FILE_TICKER_INFO, sep=',')
# print("Файл считан: ", PATH_FILE_TICKER_INFO)
# print(df_ticker_info)

for i in range(COUNT_EXPERIMENTS_GLOBAL):

    # считываение крывых
    path_history_source_curve_i = path_file_history(path_folder_history_source, TICKER_HISTORY_LIST, i)
    df = pd.read_csv(path_history_source_curve_i, sep=',')
    print("Файл считан: ", path_history_source_curve_i)


    df.drop(df.tail(1).index, inplace=True)
    df.sort_index(ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)

    # отсекаем лишние периоды
    df = date_drop_in_df(df, DATE_GLOBAL_START, DATE_GLOBAL_FINISH)

    df['ticker'] = TICKER_HISTORY_LIST[i]

    # добавление сектора
    for j in range(1,len(df_ticker_info)):
            ticker_sector = str(df_ticker_info['sector'][j])
            ticker_symbol = str(df_ticker_info['symbol'][j])
            if df.loc[0, 'ticker'] == ticker_symbol:
                df['sector'] = ticker_sector
                print(df['ticker'][0], df['sector'][0], '<=', ticker_symbol, ticker_sector)
            else:
                df['sector'] = 'no sector info'

    print(df)

    path_history_curve_i = path_file_history(PATH_FOLDER_HISTORY, TICKER_HISTORY_LIST, i)
    df.to_csv(path_history_curve_i, sep=',', index=False)
    print("Файл создан: ", path_history_curve_i, "\n")
