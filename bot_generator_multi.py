from os.path import exists
import numpy as np
import matplotlib.pyplot as plt

from constants import *
from constants_bot_generator import *

from base_functions import *
from bot_generator import *



def bot_generator_restart_day(df, param):

    if t = 0:
        # todo сделать докупку

    return df



def bot_generator_next_day(df, param, step_info_previous, day_number):

    i = day_number

    procent = param.get('procent')
    amounts_S = param.get('amounts_S')
    r = param.get('r')
    r_fin = param.get('r_fin')
    procent_loss = param.get('procent_loss')

    t = df.loc[i-1, column_t]

    # todo считывание предыдущего шага
    count_buy_step_plan = df.loc[i, column_buy_step_plan]
    df.loc[i, column_p_sell] = step.get('p_sell')
    df.loc[i, column_p_buy] = step.get('p_buy')
    df.loc[i, column_sell_buy] = step.get('sell_buy_status')
    df.loc[i, column_profit] = step.get('profit')
    df.loc[i, column_day_profit] = step.get('day_profit')
    df.loc[i, column_count_buy] = step.get('count_buy')
    df.loc[i, column_count_total_buy] = step.get('count_buy_total')
    df.loc[i, column_count_sell] = step.get('count_sell')
    df.loc[i, column_costs_of_bying] = step.get('S0')
    df.loc[i, column_sum_invested] = step.get('C')
    df.loc[i, column_cost_of_sum_investment] = step.get('B')
    df.loc[i, column_reserved_sum_investment] = step.get('S')
    df.loc[i, column_fee_count] = step.get('fee_count')

    t = step_info_previous.get('t')
    p_sell = step_info_previous.get('p_sell')
    p_buy = step_info_previous.get('p_buy')
    sell_buy_status = step_info_previous.get('sell_buy_status')
    profit = step_info_previous.get('profit')
    day_profit = step_info_previous.get('day_profit')
    count_buy = step_info_previous.get('count_buy')
    K = step_info_previous.get('count_buy_total')
    count_sell = step_info_previous.get('count_sell')
    costs_of_bying = step_info_previous.get('S0')
    C = step_info_previous.get('C')
    cost_of_sum_investment = step_info_previous.get('B')
    S = step_info_previous.get('S')
    column_fee_count = step_info_previous.get('fee_count')

    # t = step_info_previous.get('t')
    # p_sell = step_info_previous.get('p_sell')
    # p_buy = step_info_previous.get('p_buy')
    # sell_buy_status = step_info_previous.get('sell_buy_status')
    # profit = step_info_previous.get('profit')
    # day_profit = step_info_previous.get('day_profit')
    # count_buy = step_info_previous.get('count_buy')
    # K = step_info_previous.get('count_buy_total')
    # count_sell = step_info_previous.get('count_sell')
    # costs_of_bying = step_info_previous.get('S0')
    # C = step_info_previous.get('C')
    # cost_of_sum_investment = step_info_previous.get('B')
    # S = step_info_previous.get('S')
    # column_fee_count = step_info_previous.get('fee_count')

    # for i in range(1, len(df)):



    price_current = df[column_price][i]

    if price_current > p_sell:
        # случай, когда цена выше уровня продажи, т.е. мы выходим из позиции и докумаем ее снова
        fee_count = 1  # довавляем 1 в счетчик комиссий, так как будет выполнен один ордер на выход части

        # фиксация прибыли и выход из позиции

        day_profit = K * price_current - C
        profit = profit + day_profit
        df.loc[i, column_profit] = profit
        df.loc[i, column_day_profit] = day_profit
        df.loc[i, column_sell_buy] = 'sell'

        # todo записывать важные переходящие параметры бота для следующего шага, если понадобится
        # todo написать в отдельной функции ррестарт бота и закупку новой позиции
        bot_generator_restart_day(df, param)


        df.loc[i, column_count_sell] = K
        df.loc[i, column_sum_invested] = C
        df.loc[i, column_cost_of_sum_investment] = B
        df.loc[i, column_reserved_sum_investment] = S
        df.loc[i, column_fee_count] = fee_count

        # начало новой закупки

        p0 = price_current
        p_sell = p0 * (1 + r / 100)
        p_buy = p0 * (1 - procent[1])

        df.loc[i, column_p_sell] = p_sell
        df.loc[i, column_p_buy] = p_buy
        count_buy_step_plan = calc_count_buy_step_plan(amounts_S, p0, procent)

        k0 = count_buy_step_plan[0]
        K = k0
        S0 = k0 * p0
        C = S0
        B = K * p0
        t = 0


    elif df[column_price][i] < p_buy:
        # цена опустилась ниже уровня ордера на покупку => тогда бот докупает еще или выходит в stop loss

        t = t + 1


        if t < len(amounts_S):
            # случай, когда мы докупаем актив, так как это еще не последний шаг алгоритма

            # докупание после спуска до следующего уровня

            fee_count = 1  # довавляем 1 к счетчику комиссий, так как в этих случаях будет выполнен ордер на покупку
            k0 = number[t]
            K = K + k0
            p0 = df[column_price][i]
            S0 = k0 * p0
            C = C + S0
            B = K * p0
            p_sell = (C / K) * (1 + r_fin / 100)

            if (t + 1) < len(amounts_S):
                p_buy = p0 * (1 - procent[1])
            else:
                p_buy = p0 * (1 - procent_loss / 100)

            df.loc[i, column_p_sell] = p_sell
            df.loc[i, column_p_buy] = p_buy
            df.loc[i, column_profit] = profit
            df.loc[i, column_sell_buy] = 'buy'
            df.loc[i, column_count_buy] = k0
            df.loc[i, column_count_total_buy] = K
            df.loc[i, column_costs_of_bying] = S0
            df.loc[i, column_sum_invested] = C
            df.loc[i, column_cost_of_sum_investment] = B
            df.loc[i, column_reserved_sum_investment] = S
            df.loc[i, column_fee_count] = fee_count


            # # TODO оформить на этом шаге универсальное обновление
            # df.loc[i, column_t] = step.get('t') # new
            # df.loc[i, column_buy_step_plan] = step.get('buy_step_plan') # прошлый
            # df.loc[i, column_p_sell] = step.get('p_sell') # new
            # df.loc[i, column_p_buy] = step.get('p_buy') # new
            # df.loc[i, column_sell_buy] = step.get('sell_buy_status') # buy
            # df.loc[i, column_profit] = step.get('profit') # прошлый
            # df.loc[i, column_day_profit] = step.get('day_profit') # 0
            # df.loc[i, column_count_buy] = step.get('count_buy') # new
            # df.loc[i, column_count_total_buy] = step.get('count_buy_total') # new
            # df.loc[i, column_count_sell] = step.get('count_sell') # None
            # df.loc[i, column_costs_of_bying] = step.get('S0') # new
            # df.loc[i, column_sum_invested] = step.get('C') # new
            # df.loc[i, column_cost_of_sum_investment] = step.get('B') # new
            # df.loc[i, column_reserved_sum_investment] = step.get('S') # прошлый
            # df.loc[i, column_fee_count] = step.get('fee_count') # new




            # df.loc[i, column_date] = date_convert(df.loc[i, column_date])


        elif t == len(amounts_S):
            # случай STOP LOSS, так как это последний шаг алгоритма

            # выход из всех позиций по Stop loss и фиксация убытков

            fee_count = 1  # довавляем 1 к счетчику комиссий, так как в этих случаях будет выполнен ордер на покупку
            fee_count = 2  # TODO разобраться

            day_profit = K * price_current - C
            profit = profit + day_profit

            df.loc[i, column_sell_buy] = 'StopLoss'
            df.loc[i, column_count_sell] = K
            df.loc[i, column_sum_invested] = C
            df.loc[i, column_cost_of_sum_investment] = B
            df.loc[i, column_reserved_sum_investment] = S
            df.loc[i, column_fee_count] = fee_count
            df.loc[i, column_profit] = profit
            df.loc[i, column_day_profit] = day_profit

            # новая закупка

            p0 = price_current
            p_sell = p0 * (1 + r / 100)
            p_buy = p0 * (1 - procent[1])

            df.loc[i, column_p_sell] = p_sell
            df.loc[i, column_p_buy] = p_buy

            count_buy_step_plan = calc_count_buy_step_plan(amounts_S, p0, procent)

            k0 = count_buy_step_plan[0]
            K = k0
            C = k0 * p0
            B = K * p0
            t = 0

    else:

        # Просто ОЖИДАНИЕ без каких либо действий

        fee_count = 0
        B = K * price_current

        df.loc[i, column_p_sell] = df.loc[i - 1, column_p_sell]
        df.loc[i, column_p_buy] = df.loc[i - 1, column_p_buy]
        df.loc[i, column_profit] = profit
        df.loc[i, column_sum_invested] = C
        df.loc[i, column_cost_of_sum_investment] = B
        df.loc[i, column_reserved_sum_investment] = S
        df.loc[i, column_sell_buy] = 'waiting'
        df.loc[i, column_fee_count] = fee_count

            # df.loc[i, column_date] = date_convert(df.loc[i, column_date])

    df_round(df)

    return df, profit



def bot_generator_initiation_first_day(df, param):

    procent = param.get('procent')
    amounts_S = param.get('amounts_S')
    r = param.get('r')
    r_fin = param.get('r_fin')
    procent_loss = param.get('procent_loss')

    t = 0
    p0 = df[column_price][0]
    count_buy_step_plan = calc_count_buy_step_plan(amounts_S, p0, procent)
    k0 = count_buy_step_plan[0]
    K = k0
    S0 = k0 * p0
    C = S0
    B = S0
    S = sum(amounts_S)
    profit = 0
    day_profit = 0
    p_sell = p0 * (1 + r / 100)
    p_buy = p0 * (1 - procent[1])
    fee_count = 1

    step_info = {
        't': t,
        'buy_step_plan': count_buy_step_plan,
        'p_sell': p_sell,
        'p_buy': p_buy,
        'sell_buy_status': 'buy',
        'profit': profit,
        'day_profit': day_profit,
        'count_buy': k0,
        'count_buy_total': K,
        'count_sell': 0,
        'S0': S0,
        'C': C,
        'B': B,
        'S': S,
        'fee_count': fee_count
    }

    update_df_bot_step(df, step_info, 0)

    df[column_std_rolling] = rolling_std(df)

    print(df[column_sum_invested])

    return df


def  calc_count_buy_step_plan(amounts_S, p0, procent):
    step_list = []
    for j in range(len(amounts_S)):
        step_list.append(amounts_S[j] / p0) if j == 0 else step_list.append(amounts_S[j] / (p0 * prod(j, procent)))
    print('step_list = ', step_list)

    return step_list


def update_df_bot_step(df, step, i):
    df.loc[i, column_t] = step.get('t')
    df.loc[i, column_buy_step_plan] = step.get('buy_step_plan')
    df.loc[i, column_p_sell] = step.get('p_sell')
    df.loc[i, column_p_buy] = step.get('p_buy')
    df.loc[i, column_sell_buy] = step.get('sell_buy_status')
    df.loc[i, column_profit] = step.get('profit')
    df.loc[i, column_day_profit] = step.get('day_profit')
    df.loc[i, column_count_buy] = step.get('count_buy')
    df.loc[i, column_count_total_buy] = step.get('count_buy_total')
    df.loc[i, column_count_sell] = step.get('count_sell')
    df.loc[i, column_costs_of_bying] = step.get('S0')
    df.loc[i, column_sum_invested] = step.get('C')
    df.loc[i, column_cost_of_sum_investment] = step.get('B')
    df.loc[i, column_reserved_sum_investment] = step.get('S')
    df.loc[i, column_fee_count] = step.get('fee_count')

    return df

def df_round(df):

    df['day_profit'] = round(df['day_profit'], 0)
    df['total_profit'] = round(df['total_profit'], 0)
    #     df['Date'] = pd.to_datetime(df['Date'], format="%Y/%m/%d")
    df['p_buy'] = round(df['p_buy'], 2)
    df['p_sell'] = round(df['p_sell'], 2)
    df['count_buy'] = round(df['count_buy'], 2)
    df['count_sell'] = round(df['count_sell'], 2)
    df['count_total_buy'] = round(df['count_total_buy'], 2)
    df['costs_of_bying'] = round(df['costs_of_bying'], 2)
    df['sum_invested'] = round(df['sum_invested'], 2)
    df['cost_of_sum_investment'] = round(df['cost_of_sum_investment'], 2)
    df['reserved_sum_investment'] = round(df['reserved_sum_investment'], 2)

    return df


def prod_multi(j, array):
    p = 1
    if j == 0:
        return p * (1 - array[0])
    else:
        return prod(j-1, array) * (1-array[j])


# def param_rebalance_multi(param_dict_rebalance_def, rolling_std_def):
#     PROCENT_BASE = [0, 0.05, 0.10, 0.25, 0.30]  # эксперимент 17
#     R_BASE = 5
#     R_FIN_BASE = 7
#     PROCENT_LOSS_BASE = 3
#
#     print('param_dict_def = ', param_dict_rebalance_def)
#
#     coef = rolling_std_def / 0.37195826601590254
#     param_dict_rebalance_def['procent'] = [x * coef for x in param_dict_rebalance_def['procent']]
#
#     print('rebalanced_param_dict_def[procent] = ', param_dict_rebalance_def['procent'])
#
#     # r = param_dict_def.get('r')
#     # r_fin = param_dict_def.get('r_fin')
#     # procent_loss = param_dict_def.get('procent_loss')
#
#     return param_dict_rebalance_def


