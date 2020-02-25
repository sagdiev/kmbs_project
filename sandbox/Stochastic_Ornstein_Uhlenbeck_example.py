import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

sigma = 1.0  # Standard deviation.
mu = 10.  # Mean.
tau = .5  # Time constant.
dt = .001  # Time step.
T = 2.  # Total time.
count_experiment = 1000


def  OUP_generator(mu, sigma, T, dt, tau):
    n = int(T / dt)  # Number of time steps.
    t = np.linspace(0., T, n)  # Vector of times.
    sigma_bis = sigma * np.sqrt(2. / tau)
    sqrtdt = np.sqrt(dt)
    x = np.zeros(n)

    for i in range(n - 1):
        x[i + 1] = x[i] + dt * (-(x[i] - mu) / tau) + \
            sigma_bis * sqrtdt * np.random.randn()

    return t, x

for i in range(0, count_experiment):
    oup_t, oup_S  = OUP_generator(mu, sigma, T, dt, tau)
    plt.plot(oup_t, oup_S, linewidth=0.2)

plt.show()

#     7.  Let's display the evolution of the process:
# fig, ax = plt.subplots(1, 1, figsize=(8, 4))
# ax.plot(t, x, lw=2)

# 8.  Now, we are going to take a look at the time evolution of the distribution of the process.
# To do this, we will simulate many independent realizations of the same process in a vectorized way.
# We define a vector X that will contain all realizations of the process at a given time
# (that is, we do not keep all realizations at all times in memory).
# This vector will be overwritten at every time step.
# We will show the estimated distribution (histograms) at several points in time:

# ntrials = 10000
# X = np.zeros(ntrials)
# # We create bins for the histograms.
# bins = np.linspace(-2., 14., 100)
# fig, ax = plt.subplots(1, 1, figsize=(8, 4))
# for i in range(n):
#     # We update the process independently for
#     # all trials
#     X += dt * (-(X - mu) / tau) + \
#         sigma_bis * sqrtdt * np.random.randn(ntrials)
#     # We display the histogram for a few points in
#     # time
#     if i in (5, 50, 900):
#         hist, _ = np.histogram(X, bins=bins)
#         ax.plot((bins[1:] + bins[:-1]) / 2, hist,
#                 {5: '-', 50: '.', 900: '-.', }[i],
#                 label=f"t={i * dt:.2f}")
#     ax.legend()

