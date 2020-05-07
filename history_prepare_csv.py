import pandas as pd
from constants import *
from path_file_generator import *

path_folder_history_source = path_folder_history + '/source'

for i in range (count_experiments_global):

    # считываение крывых
    path_history_source_curve_i = path_file_history(path_folder_history_source, history_ticker, i)
    df = pd.read_csv(path_history_source_curve_i, sep=',')

    df.drop(df.tail(1).index,inplace=True)
    df.sort_index(ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)

    print("Файл считан: ", path_history_source_curve_i)
    print(df)

    path_history_curve_i = path_file_history(path_folder_history, history_ticker, i)
    df.to_csv(path_history_curve_i, sep = ',', index=False,)
    print("Файл создан: ", path_history_curve_i, "\n")