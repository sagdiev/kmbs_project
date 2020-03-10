import numpy as np
import matplotlib.pyplot as plt
import stochastic.continuous
import stochastic.diffusion
from model.constants import *


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
        t = np.linspace(0, self.period, N)
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


