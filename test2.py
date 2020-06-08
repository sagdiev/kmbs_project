import pandas as pd
from constants import *
from funtions_path_file_generator import *
from functions_base import *


# приведение файлов исторических данных к стандартизированному формату
# path_bot = path_file_without_prefix(PATH_FOLDER_BOT, PATH_FILE_BOT, EXPERIMENT, TICKER)

for i in range(COUNT_EXPERIMENTS_GLOBAL):

    # считываение крывых
    path_curve_i = path_file_history(PATH_FOLDER_HISTORY, TICKER_HISTORY_LIST, i)
    df = pd.read_csv(path_curve_i, sep=',')

    print(df.tail(1))

    # print(max(df['Time']))
