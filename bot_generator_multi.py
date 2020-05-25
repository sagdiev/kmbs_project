from os.path import exists
import numpy as np
import matplotlib.pyplot as plt

from constants import *
from constants_bot_generator import *

from base_functions import *
# from bot_generator import *


def bot_generator_restart_day(df, param, i, restart_signal):
    # print('СТАРТ перезапуска')
    t = int(df.loc[i, column_t])
    # print('t_previous =', t)
    if t in [0, 1, 2, 3, 4]:
        # print('пропускаем рестарт')
        return df

    if restart_signal == True:

        procent = param.get('procent')
        amounts_S = param.get('amounts_S')
        r = param.get('r')

        t = int(0)
        p0 = df[column_price][i]
        count_buy_step_plan = calc_count_buy_step_plan(amounts_S, p0, procent)
        # print('ПРИ РЕСТАРТЕ count_buy_step_plan =', count_buy_step_plan)
        k0 = count_buy_step_plan[0]
        K = k0
        S0 = k0 * p0
        C = S0
        B = S0
        S = sum(amounts_S)
        profit = df.loc[i, column_profit]  # просто фиксируем, что осталась та же после продаж в этот день (удалить)
        day_profit = df.loc[i, column_day_profit] # просто фиксируем, что осталась та же после продаж в этот день
        p_sell = p0 * (1 + r / 100)
        p_buy = p0 * (1 - procent[1])
        fee_count = df.loc[i, column_fee_count] + 1  # счетчик +1 на случай, если предыдущая покупка была в этот же день

        # sell_buy_status = 'buy' # todo потом подумать, что писать при пеерзакупке через период (если в тот же день, то sell или Stop Loss
        count_sell = 0

        df.loc[i, column_t] = t
        df[column_buy_step_plan] = np.nan
        df[column_buy_step_plan] = df[column_buy_step_plan].astype('object')
        df.at[i, column_buy_step_plan] = count_buy_step_plan
        df.loc[i, column_p_sell] = p_sell
        df.loc[i, column_p_buy] = p_buy
        # df.loc[i, column_sell_buy] = sell_buy_status # todo потом подумать, что писать при пеерзакупке через период (если в тот же день, то sell или Stop Loss
        df.loc[i, column_profit] = profit
        # print('ПРИ РЕСТАРТЕ profit =', profit)
        df.loc[i, column_day_profit] = day_profit
        df.loc[i, column_count_buy] = k0
        df.loc[i, column_count_total_buy] = K
        # print('count_total_buy =', K)
        # print('count_day =',i)
        df.loc[i, column_count_sell] = count_sell
        df.loc[i, column_costs_of_bying] = S0
        df.loc[i, column_sum_invested] = C
        df.loc[i, column_cost_of_sum_investment] = B
        df.loc[i, column_reserved_sum_investment] = S
        df.loc[i, column_fee_count] = fee_count

        print(df[column_sum_invested][0])

        print('Рестарт бота произведен')



    else: # Просто ОЖИДАНИЕ без каких либо действий без входа в позиции вообще + сохранение записей о состоянии прибыли

        # просто запись сохранения предыдущей прибыли, если пропускаем шаг
        if df.loc[i - 1, column_t] == -1:
            # print('НАДО СОХРАНИТЬ ПРИБЫЛЬ')
            df.loc[i, column_profit] = df.loc[i - 1, column_profit]

        t = int(-1)
        fee_count = 0
        day_profit = 0
        df.loc[i, column_sell_buy] = 'waiting'
        df.loc[i, column_t] = t
        df.loc[i, column_day_profit] = day_profit
        # print('ПРИ РЕСТАРТЕ profit = ', df.loc[i, column_profit])
        df.loc[i, column_fee_count] = fee_count

        # print('Рестарт ожидание')

    return df

def bot_generator_initiation_first_day(df, param, ticker, i):
    # print('Старт')

    procent = param.get('procent')
    amounts_S = param.get('amounts_S')
    r = param.get('r')

    t = 0
    p0 = df[column_price][0]
    count_buy_step_plan = calc_count_buy_step_plan(amounts_S, p0, procent)
    k0 = count_buy_step_plan[0]
    # print('ПРИ ИЦИИАЛИЗАЦИИ count_buy_step_plan =', count_buy_step_plan)
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

    sell_buy_status = 'buy'
    count_sell = 0

    df[column_t] = int()
    df.loc[i, column_t] = t
    # print('ПЕРВЫЙ РАЗ t and type(t) = ', t, type(t))
    df[column_buy_step_plan] = np.nan
    df[column_buy_step_plan] = df[column_buy_step_plan].astype('object')
    df.at[i, column_buy_step_plan] = count_buy_step_plan
    df.loc[i, column_p_sell] = p_sell
    df.loc[i, column_p_buy] = p_buy
    df.loc[i, column_sell_buy] = sell_buy_status
    df.loc[i, column_profit] = profit
    df.loc[i, column_day_profit] = day_profit
    df.loc[i, column_count_buy] = k0
    df.loc[i, column_count_total_buy] = K
    # print(K)
    # print(i)
    df.loc[i, column_count_sell] = count_sell
    df.loc[i, column_costs_of_bying] = S0
    df.loc[i, column_sum_invested] = C
    df.loc[i, column_cost_of_sum_investment] = B
    df.loc[i, column_reserved_sum_investment] = S
    df.loc[i, column_fee_count] = fee_count

    df[column_std_rolling] = rolling_std(df)
    df[column_ticker] = ticker

    print('Первая закупка бота завершена')

    return df


def bot_generator_next_day(df, param, day_number):

    i = day_number
    # print('Date ', i)

    procent = param.get('procent')
    amounts_S = param.get('amounts_S')
    r = param.get('r')
    r_fin = param.get('r_fin')
    procent_loss = param.get('procent_loss')

    t = int(df.loc[i - 1, column_t])
    # print('НАЧАЛО СЛЕДУЮЩЕГО ДНЯ t and type(t) = ', t, type(t))
    # print(i)
    if t == -1:
        return df
    # print('t and type(t) = ', t, type(t))
    count_buy_step_plan = df.loc[i - 1, column_buy_step_plan]
    # print('ПРИ НАЧАЛЕ СЛЕДУЮЩЕГО ДНЯ count_buy_step_plan =', count_buy_step_plan)
    p_sell = df.loc[i - 1, column_p_sell]
    p_buy = df.loc[i - 1, column_p_buy]
    profit = df.loc[i - 1, column_profit]
    K = df.loc[i - 1, column_count_total_buy]  # count_buy_total
    C = df.loc[i - 1, column_sum_invested]
    S = df.loc[i - 1, column_reserved_sum_investment]

    price_current = df[column_price][i]

    if price_current > p_sell:
        fee_count = 1  # довавляем 1 в счетчик комиссий, так как будет выполнен один ордер на выход части
        # фиксация прибыли и выход из позиции

        day_profit = K * price_current - C
        profit = profit + day_profit

        df.loc[i, column_profit] = profit
        # print('ПОСЛЕ ПЕРЕЗАКУПКИ profit ', i, ' =', profit)
        df.loc[i, column_day_profit] = day_profit
        df.loc[i, column_sell_buy] = 'sell'

        # todo записывать важные переходящие параметры бота для следующего шага, если понадобится
        # todo написать в отдельной функции ррестарт бота и закупку новой позиции

        # print('СТОП после выхода в ПЛЮС ', df.loc[i, column_ticker])
        df.loc[i, column_t] = -1  # t = -1 будет сигналом к новой закупке
        df.loc[i, column_fee_count] = fee_count

    elif df[column_price][i] < p_buy:  # цена ниже уровня покупки => тогда бот Докупает еще или выходит в Stop loss
        t = t + 1
        # print('t_previous =', t)
        # print('t and type(t) = ', t, type(t))

        if t < len(amounts_S):  # мы докупаем актив, так как это еще не последний шаг алгоритма

            fee_count = 1  # довавляем 1 к счетчику комиссий, так как в этих случаях будет выполнен ордер на покупку
            # print('ПРИ ЗАКУПКЕ count_buy_step_plan =', count_buy_step_plan)

            k0 = count_buy_step_plan[t]
            # print(k0)
            K = K + k0
            p0 = price_current
            S0 = k0 * p0
            C = C + S0
            B = K * p0
            p_sell = (C / K) * (1 + r_fin / 100)
            day_profit = 0

            if (t + 1) < len(amounts_S):
                p_buy = p0 * (1 - procent[1])
            else:
                p_buy = p0 * (1 - procent_loss / 100)

            df.loc[i, column_t] = t
            df.loc[i, column_p_sell] = p_sell
            df.loc[i, column_p_buy] = p_buy
            df.at[i, column_buy_step_plan] = df.at[i - 1, column_buy_step_plan]
            df.loc[i, column_profit] = profit
            df.loc[i, column_day_profit] = day_profit
            df.loc[i, column_sell_buy] = 'sell'
            df.loc[i, column_count_buy] = k0
            df.loc[i, column_count_total_buy] = K
            df.loc[i, column_costs_of_bying] = S0
            df.loc[i, column_sum_invested] = C
            df.loc[i, column_cost_of_sum_investment] = B
            df.loc[i, column_reserved_sum_investment] = S
            df.loc[i, column_fee_count] = fee_count


        elif t == len(amounts_S):  # случай STOP LOSS, так как это последний шаг алгоритма
            # выход из всех позиций по Stop loss и фиксация убытков

            fee_count = 1  # довавляем 1 к счетчику комиссий, так как будет выполнен ордер на продажу позиции

            day_profit = K * price_current - C
            profit = profit + day_profit

            df.loc[i, column_sell_buy] = 'StopLoss'
            df.loc[i, column_profit] = profit
            df.loc[i, column_day_profit] = day_profit

            # print('СТОП после SPOPLOSS ', df.loc[i, column_ticker])

            df.loc[i, column_t] = -1  # t = -1 будет сигналом к новой закупке
            df.loc[i, column_fee_count] = fee_count

    else:  # Просто ОЖИДАНИЕ без каких либо действий

        fee_count = 0
        day_profit = 0
        B = K * price_current

        df.loc[i, column_t] = t
        df.loc[i, column_p_sell] = p_sell
        df.loc[i, column_p_buy] = p_buy
        df.at[i, column_buy_step_plan] = df.at[i-1, column_buy_step_plan]
        df.loc[i, column_profit] = profit
        df.loc[i, column_day_profit] = day_profit
        df.loc[i, column_count_total_buy] = K
        df.loc[i, column_sum_invested] = C
        df.loc[i, column_cost_of_sum_investment] = B
        df.loc[i, column_reserved_sum_investment] = S
        df.loc[i, column_sell_buy] = 'waiting'
        df.loc[i, column_fee_count] = fee_count

        # print('Ожидание')

    # print('profit ', i, ' =', profit)

    return df_round(df)


def df_round(df):

    df['day_profit'] = round(df['day_profit'], 0)
    df['total_profit'] = round(df['total_profit'], 0)
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


def  calc_count_buy_step_plan(amounts_S, p0, procent):
    step_list = []
    for j in range(len(amounts_S)):
        step_list.append(amounts_S[j] / p0) if j == 0 else step_list.append(amounts_S[j] / (p0 * prod(j, procent)))

    return step_list


def prod(j, array):
    return np.prod([1 - x for x in array[:j+1]])
