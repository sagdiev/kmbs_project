import numpy as np
import pandas as pd
from timeit import default_timer as timer
# from pandas_datareader import data, wb

from constants import *
from bot_generator import *
from funtions_path_file_generator import *
from functions_base import *
from functions_bot_bi import *


# START
start = timer()

bot_bi_preparation_weight(EXPERIMENT, '', TICKER_WEIGHT)
print('TICKER_WEIGHT = ', TICKER_WEIGHT)

# таймер
duration = timer() - start
print('Время обработки алгоритма = ', duration)