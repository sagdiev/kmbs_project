
count_weight_experiment = 20
weight_experiment_i =[1, 0]

for i in range(count_weight_experiment + 1):
    weight_experiment_i[0] = i / count_weight_experiment
    weight_experiment_i[1] = 1 - i / count_weight_experiment
    print('i = ', i, 'i / count_weight_experiment = ', i / count_weight_experiment, ' : ', weight_experiment_i)