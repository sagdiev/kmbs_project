from os.path import exists
import numpy as np
import matplotlib.pyplot as plt

from constants import *
from constants_bot_generator import *
from base_functions import *


def bot_martingale(df, param_dict_def):

    # # column_date = 'Time'
    # column_p_sell = 'p_sell'
    # column_p_buy = 'p_buy'
    # # column_price = 'Price'
    # column_price = 'Open'
    # column_sell_buy = 'sell/buy'
    # column_day_profit = 'day_profit'
    # column_profit = 'total_profit'
    # column_count_sell = 'count_sell'
    # column_count_buy = 'count_buy'
    # column_count_total_buy = 'count_total_buy'
    # column_costs_of_bying = 'costs_of_bying'
    # column_sum_invested = 'sum_invested'
    # column_cost_of_sum_investment = 'cost_of_sum_investment'
    # column_reserved_sum_investment = 'reserved_sum_investment'
    # column_portfolio_cost_in_day = 'portfolio_cost_in_day'
    # column_std_rolling = 'std_rolling'
    # column_fee_count = 'fee_count'
    # column_ticker = 'ticker'

    df[column_std_rolling] = rolling_std(df)
    # print(df['STD_rolling'])
    # param_dict_def = param_rebalance(param_dict_def, df['STD_rolling'][1])
    # print('df[STD_rolling][1] = ', df['STD_rolling'][1])

    procent = param_dict_def.get('procent')
    amounts_S = param_dict_def.get('amounts_S')
    r = param_dict_def.get('r')
    r_fin = param_dict_def.get('r_fin')
    procent_loss = param_dict_def.get('procent_loss')

    count_step = [0] * (len(amounts_S) + 1)
    size_profit = [0] * (len(amounts_S) + 1)
    count_days = [0] * (len(amounts_S) + 1)


    p0 = df.loc[0, column_price]
    print(p0)

    # визначаємо яку кількість акцій потрібно купувати на відповідному етапі докуповування
    number = []
    S = 0
    for j in range(0, len(amounts_S)):
        S = S + amounts_S[j]
        if j == 0:
            number.append(amounts_S[j] / p0)
        else:
            number.append(amounts_S[j] / (p0 * prod(j, procent)))

    k0 = number[0]
    K = k0
    S0 = k0 * p0
    C = S0
    B = K * p0
    PC = K * p0
    profit = 0
    t = 0
    p_sell = p0 * (1 + r / 100)
    p_buy = p0 * (1 - procent[1])
    fee_count = 1

    df.loc[0, column_p_sell] = p_sell
    df.loc[0, column_p_buy] = p_buy
    df.loc[0, column_sell_buy] = 'buy'
    df.loc[0, column_day_profit] = K * df.loc[0, column_price] - C
    df.loc[0, column_profit] = profit
    df.loc[0, column_count_buy] = k0
    df.loc[0, column_count_total_buy] = K
    df.loc[0, column_costs_of_bying] = S0
    df.loc[0, column_sum_invested] = C
    df.loc[0, column_cost_of_sum_investment] = B
    df.loc[0, column_reserved_sum_investment] = S
    df.loc[0, column_count_sell] = 0
    df.loc[0, column_fee_count] = fee_count
    # df.loc[0, column_date] = date_convert(df.loc[0, column_date])

    for i in range(1, len(df)):
        count_days[t] = count_days[t] + 1
        price_current = df[column_price][i]

        if df[column_price][i] > p_sell:
            # случай, когда цена выше уровня продажи, т.е. мы выходим из позиции и докумаем ее снова

            fee_count = 1  # довавляем 1 в счетчик комиссий, так как в этих случаях будут выполнен
                            # один ордер на продажу - выход части акций из позиции (не 2 ордера продажи и покупки)

            if t < len(amounts_S):
                count_step[t] = count_step[t] + 1
                size_profit[t] = size_profit[t] + K * df[column_price][i] - C

            profit = profit + (K * df[column_price][i] - C)
            df.loc[i, column_profit] = profit
            df.loc[i, column_count_sell] = K

            p0 = df[column_price][i]
            p_sell = p0 * (1 + r / 100)
            p_buy = p0 * (1 - procent[1])

            df.loc[i, column_p_sell] = p_sell
            df.loc[i, column_p_buy] = p_buy
            df.loc[i, column_sell_buy] = 'sell'
            df.loc[i, column_day_profit] = K * df.loc[i, column_price] - C
            df.loc[i, column_sum_invested] = C
            df.loc[i, column_cost_of_sum_investment] = B
            df.loc[i, column_reserved_sum_investment] = S
            df.loc[i, column_fee_count] = fee_count
            # df.loc[i, column_date] = date_convert(df.loc[i, column_date])

            number = []
            for j in range(0, len(amounts_S)):
                if j == 0:
                    number.append(amounts_S[j] / p0)
                else:
                    number.append(amounts_S[j] / (p0 * prod(j, procent)))
            k0 = number[0]
            K = k0
            S0 = k0 * p0
            C = S0
            B = K * p0
            t = 0

        elif df[column_price][i] < p_buy:
            # цена опустилась ниже уровня ордера на покупку => тогда бот докупает еще или выходит в stop loss

            t = t + 1
            fee_count = 1 # довавляем 1 к счетчику комиссий, так как в этих случаях будет выполнен ордер на покупку

            if t < len(amounts_S):
                # случай, когда мы докупаем актив, так как это еще не последний шаг алгоритма

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

                # df.loc[i, column_date] = date_convert(df.loc[i, column_date])


            elif t == len(amounts_S):
                # случай stop loss, так как это последний шаг алгоритма

                count_step[t] = count_step[t] + 1

                df.loc[i, column_day_profit] = K * df.loc[i, column_price] - C
                size_profit[t] = size_profit[t] + K * df[column_price][i] - C
                df.loc[i, column_sell_buy] = 'StopLoss'
                df.loc[i, column_count_sell] = K
                df.loc[i, column_sum_invested] = C
                df.loc[i, column_cost_of_sum_investment] = B
                df.loc[i, column_reserved_sum_investment] = S
                df.loc[i, column_fee_count] = fee_count

                # df.loc[i, column_date] = date_convert(df.loc[i, column_date])

                profit = profit + K * df[column_price][i] - C
                df.loc[i, column_profit] = profit

                p0 = df[column_price][i]
                p_sell = p0 * (1 + r / 100)
                p_buy = p0 * (1 - procent[1])

                df.loc[i, column_p_sell] = p_sell
                df.loc[i, column_p_buy] = p_buy

                number = []
                for j in range(0, len(amounts_S)):
                    if j == 0:
                        number.append(amounts_S[j] / p0)
                    else:
                        number.append(amounts_S[j] / (p0 * prod(j, procent)))
                #                 print('Stoploss', K * df[column_price][i] - C)
                k0 = number[0]
                K = k0
                C = k0 * p0
                B = K * p0
                t = 0
        else:
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

    return df, profit


def prod(j, array):
    p = 1
    if j == 0:
        return p * (1 - array[0])
    else:
        return prod(j-1, array) * (1-array[j])

#
# def param_rebalance(param_dict_rebalance_def, rolling_std_def):
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



