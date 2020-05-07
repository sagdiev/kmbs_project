                               ################ INSTALLING PACKAGES ################
#############################################################################################################
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_process import arma_generate_sample
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.statespace.sarimax import SARIMAX





                        ##################### UPLOADING DATA #####################
####################################################################################################################
df = pd.read_csv('ABBV.csv', sep=',')
df.drop(df.tail(1).index,inplace=True)
df.sort_index(ascending=False, inplace=True)
df.reset_index(drop=True, inplace=True)
df = df['Open']


nsample = len(df)                   ## довжина датафрейму
start_price = df[nsample-1]         ## ціна, з якої стартує генерування



                        ############ GENERATING STOCHASTIC DATA --> GBM ############
#######################################################################################################################

T = nsample
mu = np.mean(df.pct_change())
sigma = np.std(df.pct_change())
S0 = start_price  # ціна, з якої стартує генерування
dt = 1  # дейт-тайм: ділимо "Т" на це число - отримуємо к-ть точок
count_experiment = 100  # к-ть спостережень(графіків)


def GBM_generator(mu, sigma, T, dt, S0):
    N = round(T / dt)  # к-ть точок для кожної кривої
    t = np.linspace(0, T, N)  # створення вектору послідовних чисел: від, до, з якою к-тю точок
    W = np.random.standard_normal(size=N)
    W = np.cumsum(W) * np.sqrt(dt)  ### standard brownian motion ### # кумулятивна сума 2000 рандомних чисел,
    # помножена на корінь квадратний з дей-тайму
    X = (mu - 0.5 * sigma ** 2) * t + sigma * W
    S = S0 * np.exp(X)  ### geometric brownian motion ###

    return t, S


for i in range(0, count_experiment):
    gbm_t, gbm_S = GBM_generator(mu, sigma, T, dt, S0)
    print((gbm_S[-1]))
    #     print(np.mean(gbm_S))
    plt.plot(gbm_t, gbm_S, linewidth=.3)


plt.plot(df.index-nsample, df, label='ABBV', color="k", linewidth=1)  ## plot real historical stock data a little bit left
plt.show()