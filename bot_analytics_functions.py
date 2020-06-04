import numpy as np
import pandas as pd
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from path_file_generator import *
from base_functions import *


def bot_analytics_summary(experiment_def, prefix_experiment_def):
    start = timer()

    # папки и файлы
    path_bot = path_file_without_prefix(PATH_FOLDER_BOT, PATH_FILE_BOT, experiment_def, TICKER)
    path_folder_bi = folder_check(PATH_FOLDER_BI)
    path_bi = path_folder_bi + '/' + experiment_def + str(prefix_experiment_def) +'.csv'
    path_folder_analytic = folder_check(PATH_FOLDER_BOT_ANALYTIC)
    path_bi_summary = path_folder_analytic + '/' + experiment_def + str(prefix_experiment_def) +'_summary.csv'
    print(path_bi)

    # считываение файлы
    df = pd.read_csv(path_bi, sep=',')
    print("Файл считан: ", path_bi)
    print(df)

    df_summary = pd.DataFrame(columns=['Time'] + COLUMNS_WEIGHT_IMPACTED)

    date_list = df['Time'].unique().tolist()
    print(date_list)

    df_summary['Time'] = date_list
    print(df_summary)

    for j in range(len(date_list)):
        date_j = date_list[j]
        print('\n', 'experiment ', prefix_experiment_def, ' ', date_j)
        for i in range(len(COLUMNS_FOR_SUMMARY)):
            column_i = COLUMNS_FOR_SUMMARY[i]
            df_summary.loc[j, column_i] = df.loc[df['Time'] == date_j, column_i].sum()
            # print(column_i, df_summary.loc[j, column_i])

    df_summary['return'] = df_summary['equity_line'].pct_change()

    df_summary.to_csv(path_bi_summary, index=False)

    return df_summary
