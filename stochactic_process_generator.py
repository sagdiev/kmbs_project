import numpy as np
import os
import csv
import matplotlib.pyplot as plt
import stochastic.continuous
import stochastic.diffusion
from constants import *





class StochasticProcess():
    """Генерируется одна из случайных реализаций стохастических процессов"""
    def __init__(self, mu, sigma, period, dt):
        """Инициируем атрибуты базового стохастического процесса"""
        self.mu = mu
        self.sigma = sigma
        self.period = period
        self.dt = dt
        self.n_times = self.period // self.dt


    def  generator_gbm(self, s0):
        """GBR Геометрическое Броневское движение"""
        N = round(self.period / self.dt)
        print(N)
        t = np.linspace(1, self.period, N)
        W = np.random.standard_normal(size=N)
        W = np.cumsum(W) * np.sqrt(self.dt)  # standard brownian motion ###
        X = (self.mu - 0.5 * self.sigma ** 2) * t + self.sigma * W
        s = s0 * np.exp(X)  # geometric brownian motion ###

        return t, s


    def generator_cev(self, gamma):
        """CEV Constant Elasticity Variance process"""
        stoch = stochastic.diffusion.ConstantElasticityVarianceProcess(self.mu, self.sigma, gamma, self.period)
        s = stoch.sample(self.n_times)
        t = stoch.times(self.n_times)

        return t, s


def path_csv_curve (ticker_def, prefix_def):
    path_prefix = path_folder + str(ticker_def) + '/' + path_file + '_' + str(prefix_def) + '.csv'
    print(path_prefix)

    return path_prefix


#Start

# checking consnants
print("count_experiments_global = ", count_experiments_global)
print("period = ", period)
print("dt = ", dt)

# setting parameters
mu = 0
sigma = 0.02
s0 = 1000
# path = 'outfile'

#create dir if not exsit yet
dirName = path_folder + '/' + ticker

try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory ", dirName, " Created ")
except FileExistsError:
    print("Directory ", dirName, " already exists")



for i in range (count_experiments_global):
    t_curve, s_curve = StochasticProcess(mu, sigma, period, dt).generator_gbm(s0)

    with open(path_csv_curve(ticker, i + 1), "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['count', 'Date', 'Price'])

        for k, j in zip(t_curve, s_curve):
            date_k = date_experiment_start + timedelta(days = k - 1)
            writer.writerow([k, date_k, j])

    plt.plot(t_curve, s_curve, linewidth=0.1)


plt.show()