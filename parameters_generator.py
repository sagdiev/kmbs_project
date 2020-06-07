import numpy as np
import pandas as pd
import random
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from path_file_generator import *


def random_bot_parameters_seed(count_parameters_experiments, seed_for_random):

    procent_before_random = PROCENT_BASE
    amounts_s_weight_before_random = AMOUNT_S_WEIGHT_BASE
    r_before_random = R_BASE
    r_fin_before_random  = R_FIN_BASE
    procent_loss_before_random = PROCENT_LOSS_BASE
    step_before_random = STEP_BOT_START
    # point_before_random = POINT_BOT_START
    total_reserve_before_random = TOTAL_RESERVED_BOT_START

    procent_min = PROCENT_RANDOM_MIN
    amounts_s_weight_min = AMOUNT_S_WEIGHT_RANDOM_MIN
    r_min = R_RANDOM_MIN
    r_fin_min = R_FIN_RANDOM_MIN
    procent_loss_min = PROCENT_LOSS_RANDOM_MIN
    # point_min = POINT_RANDOM_MIN
    step_min = STEP_RANDOM_MIN
    total_min = TOTAL_RANDOM_MIN

    procent_max = PROCENT_RANDOM_MAX
    amounts_s_weight_max = AMOUNT_S_WEIGHT_RANDOM_MAX
    r_max = R_RANDOM_MAX
    r_fin_max = R_FIN_RANDOM_MAX
    procent_loss_max = PROCENT_LOSS_RANDOM_MAX
    # point_max = POINT_RANDOM_MAX
    step_max = STEP_RANDOM_MAX
    total_max = TOTAL_RANDOM_MAX

    param_dict_list = []
    step_random_list = []
    procent_random = []
    amounts_s_weight_random = []

    # первый параметр - базовый для стандартной работы подготовки параметров только 1 раз
    # с заданами парметрами в constants.py (без рандомной составляющей)
    procent_before_random = procent_before_random[:step_before_random]
    amounts_s_weight_before_random = amounts_s_weight_before_random[:step_before_random]
    amounts_s_coef_before_random = total_reserve_before_random / sum(amounts_s_weight_before_random)
    amounts_s_before_random = [ round( x * amounts_s_coef_before_random ) for x in amounts_s_weight_before_random ]

    param_dict_before_random = param_to_dict(procent_before_random, amounts_s_before_random,
                                     r_before_random, r_fin_before_random,
                                     procent_loss_before_random, step_before_random)
    # print(param_dict_before_random)

    param_dict_list.append(param_dict_before_random)

    # генерирование рандомных параметров для тестов
    random.seed(seed_for_random)

    for i in range(count_parameters_experiments-1):
        # print('start')
        procent_random = [random.randint(int(procent_min[j]*100), int(procent_max[j]*100)) / 100
                          for j in range(len(procent_min))]
        amounts_s_weight_random = [random.randint(amounts_s_weight_min[j], amounts_s_weight_max[j])
                                   for j in range(len(amounts_s_weight_min))]
        # print(procent_random)
        r_random = random.randint(r_min, r_max)
        r_fin_random = random.randint(r_fin_min, r_fin_max)
        procent_loss_random = random.randint(procent_loss_min, procent_loss_max)
        step_random = random.randint(step_min, step_max)
        # print(step_random)
        # point_random = random.randint(point_min, point_max)
        total_random = random.randint(total_min, total_max)

        # отсекаем ненужные елементы параметров по длине step_random
        procent_random = procent_random[:step_random]
        amounts_s_weight_random = amounts_s_weight_random[:step_random]

        amounts_s_coef = total_random / sum(amounts_s_weight_random)
        amounts_s_random = [ round( x * amounts_s_coef ) for x in amounts_s_weight_random ]

        param_dict_i = param_to_dict(procent_random, amounts_s_random,
                                     r_random, r_fin_random, procent_loss_random, step_random)
        # преобразование набора параметров в словарь параметров
        # param_dict_def = {'procent': procent_def,
        #                   'amounts_S': amounts_S_def,
        #                   'r': r_def,
        #                   'r_fin': r_fin_def,
        #                   'procent_loss': procent_loss_def}


        seed_for_random += 1

        # print(param_dict_i)

        param_dict_list.append(param_dict_i)
        # step_random_list.append(step_random)

    # print(param_dict_list)

    return param_dict_list


def param_generate_base_point_total_amount(point_def, total_amount_def, step_count_def):
    # генерирование араметров бота по базовому поинту и
    # по ОБЩЕЙ сумме, и по кол-ву шагов опирсаясь на базовое расперделение процентов
    param_dict_first_def = param_generate_base_point_amount_first(point_def, 1, step_count_def)
    param_dict_def = param_correction_to_total_amount(total_amount_def, param_dict_first_def)

    return param_dict_def


def param_generate_base_point_amount_first(point_def, amount_first_def, step_count_def):
    # генерирование араметров бота по базовому поинту и по
    # первой сумме, и по кол-ву шагов опирсаясь на базовое расперделение процентов
    global PROCENT_BASE, R_BASE, R_FIN_BASE, PROCENT_LOSS_BASE

    procent_cutted = PROCENT_BASE[:step_count_def]
    procent_def = [x * point_def for x in procent_cutted]
    r_def = R_BASE * point_def
    r_fin_def = R_FIN_BASE * point_def
    procent_loss_def = PROCENT_LOSS_BASE * point_def

    amounts_S_def = [amount_first_def]
    for i in range ( 0, step_count_def - 1 ):
        amounts_S_def.append(amount_first_def * 2 ** i)

    param_dict_def = param_to_dict(procent_def, amounts_S_def, r_def, r_fin_def, procent_loss_def, step_count_def)

    return param_dict_def


def param_correction_to_total_amount(total_amount_def, param_dict_def):
    # пересчет параметров бота, если необходимо опираться на общую Сумму всего резерва из amounts_S,
    # а не на первое базовое значение amounts_S
    global PROCENT_BASE

    sum_amonuts_s = sum(param_dict_def.get('amounts_S'))

    point_def = param_dict_def.get('procent')[1]/PROCENT_BASE[1]
    amount_first_def = total_amount_def / sum_amonuts_s * param_dict_def.get('amounts_S')[0]
    step_count_def = len(param_dict_def.get('amounts_S'))

    param_dict_corrected_def = param_generate_base_point_amount_first(point_def, amount_first_def, step_count_def)

    return param_dict_corrected_def


def param_to_dict(procent_def, amounts_S_def, r_def, r_fin_def, procent_loss_def, step_def):
    # преобразование набора параметров в словарь параметров

    param_dict_def = {'procent': procent_def,
                      'amounts_S': amounts_S_def,
                      'r': r_def,
                      'r_fin': r_fin_def,
                      'procent_loss': procent_loss_def,
                      'step': step_def}

    return param_dict_def


# def param_form_dict(param_dict_def):
#     # преобразование словаря параметров в list - возможно что это бесполезная функция
#
#     procent_def = param_dict_def.get('procent')
#     amounts_S_def = param_dict_def.get('amounts_S')
#     r_def = param_dict_def.get('r')
#     r_fin_def = param_dict_def.get('r_fin')
#     procent_loss_def = param_dict_def.get('procent_loss')
#
#     return procent_def, amounts_S_def, r_def, r_fin_def, procent_loss_def


# # тест генерирования упрощенных параметров
# point = 1
# # amount_first = 1000
# step_count = 3
#
# total_amount = 10000  # возможен вариант подсчета параметром исходя из Общей суммы резерва
#
# # print(param_generate_base_point_amount_first(point, amount_first, step_count)) # вариант генерирования параметров по первой сумме amounts_S
#
# print(param_generate_base_point_total_amount(point, total_amount, step_count)) # вариант генерирования параметров по Общей сумме amounts_S
