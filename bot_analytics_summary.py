import numpy as np
import pandas as pd
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from funtions_path_file_generator import *
from functions_base import *
from functions_bot_analytics import *

# START
start = timer()

# записываем данные о начале обратоки этого файла в журнал
running_file = sys.argv[0]
logbook_text = logbook_text_compelling_start_algorithm(running_file)
print(logbook_text)

bot_analytics_summary(EXPERIMENT, '')

# таймер
duration = timer() - start
print('Время обработки алгоритма = ', duration)

# записываем данные об окончании в журнал
logbook_text_compelling_finish_algorithm(running_file, duration)
