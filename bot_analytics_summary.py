import numpy as np
import pandas as pd
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from path_file_generator import *
from base_functions import *
from bot_analytics_functions import *

# START
start = timer()

bot_analytics_summary(EXPERIMENT, '')

# таймер
duration = timer() - start
print('Время обработки алгоритма = ', duration)
