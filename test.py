import pandas as pd
from constants import *

weight = [i / sum(TICKER_WEIGHT) for i in TICKER_WEIGHT]

print(TICKER_WEIGHT)
print(weight)
