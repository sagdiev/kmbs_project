import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import stochastic.continuous
import stochastic.diffusion

count_experiment = 1000
speed=0.5
mean=10
vol=0.7
tau=1 #GaussianNoise(t)
t=20
times=365
T = 3.65
mu = 0.0
sigma = 0.2
S0 = 10
dt = 0.01
rate_func=1
rate_args=1
rate_kwargs=1

for i in range(0, count_experiment):
    stoch = stochastic.continuous.MixedPoissonProcess(rate_func, rate_args, rate_kwargs)
    s = stoch.sample(32)
    times = stoch.times(32)
    plt.plot(times, s, linewidth=0.1)

plt.show()

# def stochastic_fractionalbrownianmotion(hurst, t):
#     fbm = stochastic.continuous.FractionalBrownianMotion(hurst, t)
#     s = fbm.sample(32)
#     times = fbm.times(32)
#     return times, s
#
# for i in range(0, count_experiment):
#     stoch_t, stoch_S  = stochastic_fractionalbrownianmotion(hurst, t)
#     plt.plot(stoch_t, stoch_S, linewidth=0.1)
#


# T = 3.65
# mu = 0.0
# sigma = 0.2
# S0 = 10
# dt = 0.01
# count_experiment = 1000
#
# def  GBM_generator(mu, sigma, T, dt, S0):
#     N = round(T / dt)
#     print(N)
#     t = np.linspace(0, T, N)
#     W = np.random.standard_normal(size=N)
#     W = np.cumsum(W) * np.sqrt(dt)  ### standard brownian motion ###
#     X = (mu - 0.5 * sigma ** 2) * t + sigma * W
#     S = S0 * np.exp(X)  ### geometric brownian motion ###
#
#     return t, S
#
# for i in range(0, count_experiment):
#     gbm_t, gbm_S  = GBM_generator(mu, sigma, T, dt, S0)
#     plt.plot(gbm_t, gbm_S, linewidth=0.1)
#
# plt.show()