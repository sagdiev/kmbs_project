import numpy as np
import pandas as pd
from timeit import default_timer as timer

from constants import *
from bot_generator import *
from path_file_generator import *


def param_generate_base_point_amount_first(point_def, amount_first_def, step_count_def):
    # генерирование араметров бота по базовому поинту и по первой сумме, и по кол-ву шагов опирсаясь на базовое расперделение процентов
    global PROCENT_BASE, R_BASE, R_FIN_BASE, PROCENT_LOSS_BASE

    procent_cutted = PROCENT_BASE[:step_count_def]
    procent_def = [ x * point_def for x in procent_cutted ]
    r_def = R_BASE * point_def
    r_fin_def = R_FIN_BASE * point_def
    procent_loss_def = PROCENT_LOSS_BASE * point_def

    amounts_S_def = [amount_first_def]
    for i in range (0, step_count_def - 1):
        amounts_S_def.append(amount_first_def * 2 ** i)

    param_dict_def = param_to_dict(procent_def, amounts_S_def, r_def, r_fin_def, procent_loss_def)

    return param_dict_def


def param_generate_base_point_total_amount(point_def, total_amount_def, step_count_def):
    # генерирование араметров бота по базовому поинту и по ОБЩЕЙ сумме, и по кол-ву шагов опирсаясь на базовое расперделение процентов
    global PROCENT_BASE

    param_dict_first_def = param_generate_base_point_amount_first(point_def, 1, step_count_def)
    param_dict_def = param_correction_to_total_amount(total_amount_def, param_dict_first_def)

    return param_dict_def


def param_correction_to_total_amount(total_amount_def, param_dict_def):
    # пересчет параметров бота, если необходимо опираться на общую Сумму всего резерва из amounts_S,
    # а не на первое базовое значение amounts_S
    global PROCENT_BASE

    sum_amonuts_s = sum(param_dict_def.get('amounts_S'))

    point = param_dict_def.get('procent')[1]/PROCENT_BASE[1]
    amount_first = total_amount_def / sum_amonuts_s * param_dict_def.get('amounts_S')[0]
    step_count = len(param_dict_def.get('amounts_S'))

    param_dict_corrected_def = param_generate_base_point_amount_first(point, amount_first, step_count)

    return param_dict_corrected_def


def param_to_dict(procent_def, amounts_S_def, r_def, r_fin_def, procent_loss_def):
    # преобразование набора параметров в словарь параметров

    param_dict_def = {'procent': procent_def,
                      'amounts_S' : amounts_S_def,
                      'r': r_def,
                      'r_fin': r_fin_def,
                      'procent_loss': procent_loss_def}

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


# тест генерирования упрощенных параметров
point = 0.01
amount_first = 1000
step_count = 3

total_amount = 1000 # возможен вариант подсчета параметром исходя из Общей суммы резерва

print(param_generate_base_point_amount_first(point, amount_first, step_count)) # вариант генерирования параметров по первой сумме amounts_S

print(param_generate_base_point_total_amount(point, total_amount, step_count)) # вариант генерирования параметров по Общей сумме amounts_S
