import pandas as pd
from constants import *
from path_file_generator import *

path_folder_history_source = PATH_FOLDER_HISTORY + '/source'

for i in range(COUNT_EXPERIMENTS_GLOBAL):

    # считываение крывых
    path_history_source_curve_i = path_file_history(path_folder_history_source, TICKER_HISTORY_LIST, i)
    df = pd.read_csv(path_history_source_curve_i, sep=',')

    df.drop(df.tail(1).index, inplace=True)
    df.sort_index(ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)

    print("Файл считан: ", path_history_source_curve_i)
    print(df)

    path_history_curve_i = path_file_history(PATH_FOLDER_HISTORY, TICKER_HISTORY_LIST, i)
    df.to_csv(path_history_curve_i, sep=',', index=False)
    print("Файл создан: ", path_history_curve_i, "\n")
