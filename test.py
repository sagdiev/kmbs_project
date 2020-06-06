from base_functions import *

print(random_weights_seed(5, 3))
print(random_weights_seed(5, 3))

random.seed(3)
random_example = random.sample(range(100), 5)
print('random_example ', random_example)

print(random_portfolio_weights_list_seed(20 , 5, 3))
print(len(random_portfolio_weights_list_seed(20 , 5, 3)))

random_example = random_portfolio_weights_list_seed(COUNT_WEIGHT_EXPERIMENTS , len(TICKER_HISTORY_LIST), SEED_EXPERIMENT)

print('random_example to code = ', random_example)