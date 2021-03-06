from functions_base import *
import random

# print(random_weights_seed(5, 3))
# print(random_weights_seed(5, 3))
#
# random.seed(3)
# random_example = random.sample(range(100), 5)
# print('random_example ', random_example)
#
# print(random_portfolio_weights_list_seed(20 , 5, 3))
# print(len(random_portfolio_weights_list_seed(20 , 5, 3)))

# random_example = random_portfolio_weights_list_seed(COUNT_WEIGHT_EXPERIMENTS , len(TICKER_HISTORY_LIST), SEED_EXPERIMENT)
# print('random_example to code = ', random_example)

# # random.seed(3)
# random_try = random.randrange(5,60,5)
# print(random_try)
#
# random_try = random.randint(3,6)
# print(random_try)

count_parameters_experiments = 50
seed_for_random = 3
random_bot_parameters_seed(count_parameters_experiments, seed_for_random)

# mu, sigma = 0, 0.1  # mean and standard deviation
# s = np.random.normal(mu, sigma, 10000)
# print('\nNormal test for given data "TEST":\n', stats.normaltest(s))


logic = {'Open'  : 'first',
         'High'  : 'max',
         'Low'   : 'min',
         'Close' : 'last',
         'Volume': 'sum'}

offset = pd.offsets.timedelta(days=-6)

f = pd.read_clipboard(parse_dates=['Date'], index_col=['Date'])
f.resample('W', loffset=offset).apply(logic)


