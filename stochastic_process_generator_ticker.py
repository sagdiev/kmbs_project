import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import stochastic.continuous
import stochastic.diffusion
from timeit import default_timer as timer
from constants import *
from path_file_generator import *


class StochasticProcess():
    """Генерируется одна из случайных реализаций стохастических процессов"""
    def __init__(self, mu_def, sigma_def, period_def, dt_def):
        """Инициируем атрибуты базового стохастического процесса"""
        self.mu = mu_def
        self.sigma = sigma_def
        self.period = period_def
        self.dt = dt_def
        self.n_times = self.period // self.dt

    def generator_gbm(self, s0_def):
        """GBR Геометрическое Броневское движение"""
        n = round(self.period / self.dt)
        print(n)
        t = np.linspace(1, self.period, n)
        w = np.random.standard_normal(size=n)
        w = np.cumsum(w) * np.sqrt(self.dt)  # standard brownian motion ###
        x = (self.mu - 0.5 * self.sigma ** 2) * t + self.sigma * w
        s = s0_def * np.exp(x)  # geometric brownian motion ###

        return t, s

    def generator_cev(self, gamma):
        """CEV Constant Elasticity Variance process"""
        stoch = stochastic.diffusion.ConstantElasticityVarianceProcess(self.mu, self.sigma, gamma, self.period)
        s = stoch.sample(self.n_times)
        t = stoch.times(self.n_times)

        return t, s


# START
start = timer()

# checking consnants
print("count_experiments_global = ", COUNT_EXPERIMENTS_GLOBAL)
print("period = ", PERIOD)
print("dt = ", DT)

# определение параметров из историчских данных
df = pd.read_csv(path_file_history(PATH_FOLDER_HISTORY, TICKER_HISTORY_LIST, 0), sep=',')
df = df.tail(250)
# df.sort_index(ascending=False, inplace=True)
df.reset_index(drop=True, inplace=True)
print(df)

# nsample = len(df)                   ## довжина датафрейму
start_price = df['Open'][len(df) - 1]  # ціна, з якої стартує генерування
# print(start_price)

T = 252*3
mu = np.mean(df['Open'].pct_change())
sigma = np.std(df['Open'].pct_change())
s0 = start_price  # ціна, з якої стартує генерування
dt = 1  # дейт-тайм: ділимо "Т" на це число - отримуємо к-ть точок
# count_experiment = 100  # к-ть спостережень(графіків)


print(mu, sigma)

# # setting parameters
# mu = 0
# sigma = 0.1
# s0 = 1000

# path
path_curve = path_file_without_prefix(PATH_FOLDER_CURVE, PATH_FILE_CURVE, EXPERIMENT, TICKER)
# os.makedirs(path_curve)

# Starting curves generation
for i in range(COUNT_EXPERIMENTS_GLOBAL):
    t_curve, s_curve = StochasticProcess(mu, sigma, PERIOD, dt).generator_gbm(s0)

    with open(path_file(path_curve, i + 1), "w", newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['count', 'Time', 'Open'])

        for k, j in zip(t_curve, s_curve):
            print(k)
            date_k = DATE_EXPERIMENT_START + timedelta(days=k - 1)
            writer.writerow([k, date_k, round(j, 2)])

    plt.plot(t_curve, s_curve, linewidth=0.1)

plt.show()

# timer
duration = timer() - start
print('Время обработки алгоритма = ', duration)
