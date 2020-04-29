import matplotlib.pyplot as plt
import numpy as np

T = 3.65
mu = 0.0
sigma = 0.2
S0 = 10
dt = 0.01
count_experiment = 1

def  GBM_generator(mu, sigma, T, dt, S0):
    N = round(T / dt)
    print(N)
    t = np.linspace(0, T, N)
    W = np.random.standard_normal(size=N)
    W = np.cumsum(W) * np.sqrt(dt)  ### standard brownian motion ###
    X = (mu - 0.5 * sigma ** 2) * t + sigma * W
    S = S0 * np.exp(X)  ### geometric brownian motion ###

    return t, S

for i in range(0, count_experiment):
    gbm_t, gbm_S  = GBM_generator(mu, sigma, T, dt, S0)
    plt.plot(gbm_t, gbm_S, linewidth=1)

plt.show()