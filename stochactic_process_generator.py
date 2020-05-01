import numpy as np
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


def path_out_csv (prefix):
    path = 'data_research_del/outfile'
    path_prefix = path + '_' + str(prefix) + '.csv'

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

for i in range (count_experiments_global):
    t_curve, s_curve = StochasticProcess(mu, sigma, period, dt).generator_gbm(s0)

    plt.plot(t_curve, s_curve, linewidth=0.1)

print(type(t_curve))
print(s_curve)
for i in range (len(t_curve)):
    for j in range(len(s_curve)):
    # print(i, j)
        with open(path_out_csv(i), "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow([i,j])

#plt.show()