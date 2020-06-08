
# взято с https://plotly.com/python/v3/ipython-notebooks/markowitz-portfolio-optimization/
# TODO применить у нас

# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import cvxopt as opt
from cvxopt import blas, solvers
# import pandas as pd

np.random.seed(123)

import plotly
import cufflinks
# version(plotly)

# (*) To communicate with Plotly's server, sign in with credentials file
# import plotly.plotly as py

# (*) Useful Python/Plotly tools
# import plotly.tools as tls

# (*) Graph objects to piece together plots
# from plotly.graph_objs import *


def optimal_portfolio(returns):
    n = len(returns)
    returns = np.asmatrix(returns)

    N = 100
    mus = [10**(5.0 * t/ N - 1.0) for t in range(N)]

    # Convert to cvxopt matrices
    S = opt.matrix(np.cov(returns))
    pbar = opt.matrix(np.mean(returns, axis=1))

    # Create constraint matrices
    G = -opt.matrix(np.eye(n))  # negative n x n identity matrix
    h = opt.matrix(0.0, (n, 1))
    A = opt.matrix(1.0, (1, n))
    b = opt.matrix(1.0)

    # Calculate efficient frontier weights using quadratic programming
    portfolios = [solvers.qp(mu * S, -pbar, G, h, A, b)['x']
                  for mu in mus]
    ## CALCULATE RISKS AND RETURNS FOR FRONTIER
    returns = [blas.dot(pbar, x) for x in portfolios]
    risks = [np.sqrt(blas.dot(x, S * x)) for x in portfolios]
    ## CALCULATE THE 2ND DEGREE POLYNOMIAL OF THE FRONTIER CURVE
    m1 = np.polyfit(returns, risks, 2)
    x1 = np.sqrt(m1[2] / m1[0])
    # CALCULATE THE OPTIMAL PORTFOLIO
    wt = solvers.qp(opt.matrix(x1 * S), -pbar, G, h, A, b)['x']
    return np.asarray(wt), returns, risks


def random_portfolio(returns):
    '''
    Returns the mean and standard deviation of returns for a random portfolio
    '''

    p = np.asmatrix(np.mean(returns, axis=1))
    w = np.asmatrix(rand_weights(returns.shape[0]))
    C = np.asmatrix(np.cov(returns))

    mu = w * p.T
    sigma = np.sqrt(w * C * w.T)

    # This recursion reduces outliers to keep plots pretty
    if sigma > 2:
        return random_portfolio(returns)
    return mu, sigma


def rand_weights(n):
    ''' Produces n random weights that sum to 1 '''
    k = np.random.rand(n)
    return k / sum(k)


# return_vec = [1,2, 3,4,56,55,77,86,66,53,23,4]

## NUMBER OF ASSETS
n_assets = 4

## NUMBER OF OBSERVATIONS
n_obs = 1000

return_vec = np.random.randn(n_assets, n_obs)

print(return_vec)

# fig = plt.figure()
# plt.plot(return_vec.T, alpha=.4);
# plt.xlabel('time')
# plt.ylabel('returns')
# py.iplot_mpl(fig, filename='s6_damped_oscillation')


n_portfolios = 500
means, stds = np.column_stack([
    random_portfolio(return_vec)
    for _ in range(n_portfolios)  # xrange
])



weights, returns, risks = optimal_portfolio(return_vec)

print('weights = ', weights)

# fig = plt.figure()
# plt.plot(stds, means, 'o')
# plt.ylabel('mean')
# plt.xlabel('std')
# plt.plot(risks, returns, 'y-o')
# py.iplot_mpl(fig, filename='efficient_frontier', strip_style=True)



