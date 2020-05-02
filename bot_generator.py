import numpy as np
import matplotlib.pyplot as plt
from constants import *



def bot_martingale(df, amounts_S, procent, r, r_fin, procent_loss):

    column_p_sell = 'p_sell'
    column_p_buy = 'p_buy'
    column_price = 'Price'
    column_sell_buy = 'sell/buy'
    column_day_profit = 'day_profit'
    column_profit = 'total_profit'
    column_count_sell = 'count_sell'
    column_count_buy = 'count_buy'
    column_count_total_buy = 'count_total_buy'
    column_costs_of_bying = 'costs_of_bying'
    column_sum_invested = 'sum_invested'
    column_ticker = 'ticker'

    count_step = [0] * (len(amounts_S) + 1)
    size_profit = [0] * (len(amounts_S) + 1)
    count_days = [0] * (len(amounts_S) + 1)

    p0 = df.loc[0, column_price]
    # p0 = 327.40
    # print(p0)

    # визначаємо яку кількість акцій потрібно купувати на відповідному етапі докуповування
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
    Profit = 0
    t = 0
    p_sell = p0 * (1 + r / 100)
    p_buy = p0 * (1 - procent[1])

    df.loc[0, column_p_sell] = p_sell
    df.loc[0, column_p_buy] = p_buy
    df.loc[0, column_sell_buy] = 'buy'
    df.loc[0, column_day_profit] = K * df.loc[0, column_price] - C
    df.loc[0, column_profit] = Profit
    df.loc[0, column_count_buy] = k0
    df.loc[0, column_count_total_buy] = K
    df.loc[0, column_costs_of_bying] = S0
    df.loc[0, column_sum_invested] = C

    for i in range(1, len(df)):
        count_days[t] = count_days[t] + 1
        # count_days

        if df[column_price][i] > p_sell:
            if t < len(amounts_S):
                count_step[t] = count_step[t] + 1
                # count_step
                size_profit[t] = size_profit[t] + K * df[column_price][i] - C
                # size_profit
            else:
                pass
            Profit = Profit + (K * df[column_price][i] - C)
            df.loc[i, column_profit] = Profit
            df.loc[i, column_count_sell] = K

            p0 = df[column_price][i]
            p_sell = p0 * (1 + r / 100)
            p_buy = p0 * (1 - procent[1])

            df.loc[i, column_p_sell] = p_sell
            df.loc[i, column_p_buy] = p_buy
            df.loc[i, column_sell_buy] = 'sell'
            df.loc[i, column_day_profit] = K * df.loc[i, column_price] - C
            df.loc[i, column_sum_invested] = C

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
            t = 0

        elif df[column_price][i] < p_buy:
            t = t + 1

            if t < len(amounts_S):
                k0 = number[t]
                K = K + k0
                p0 = df[column_price][i]
                S0 = k0 * p0
                C = C + S0

                p_sell = (C / K) * (1 + r_fin / 100)

                if (t + 1) < len(amounts_S):
                    p_buy = p0 * (1 - procent[1])
                else:
                    p_buy = p0 * (1 - procent_loss / 100)

                df.loc[i, column_p_sell] = p_sell
                df.loc[i, column_p_buy] = p_buy
                df.loc[i, column_profit] = Profit
                df.loc[i, column_sell_buy] = 'buy'
                df.loc[i, column_count_buy] = k0
                df.loc[i, column_count_total_buy] = K
                df.loc[i, column_costs_of_bying] = S0
                df.loc[i, column_sum_invested] = C

            elif t == len(amounts_S):
                count_step[t] = count_step[t] + 1
                count_step
                df.loc[i, column_day_profit] = K * df.loc[i, column_price] - C
                size_profit[t] = size_profit[t] + K * df[column_price][i] - C
                df.loc[i, column_sell_buy] = 'StopLoss'
                df.loc[i, column_count_sell] = K
                df.loc[i, column_sum_invested] = C

                Profit = Profit + K * df[column_price][i] - C
                df.loc[i, column_profit] = Profit

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
                t = 0
        else:
            df.loc[i, column_p_sell] = df.loc[i - 1, column_p_sell]
            df.loc[i, column_p_buy] = df.loc[i - 1, column_p_buy]
            df.loc[i, column_profit] = Profit
            df.loc[i, column_sum_invested] = C
            df.loc[i, column_sell_buy] = 'waiting'

    df['day_profit'] = round(df['day_profit'], 0)
    df['total_profit'] = round(df['total_profit'], 0)
    #     df['Date'] = pd.to_datetime(df['Date'], format="%Y/%m/%d")
    df['p_buy'] = round(df['p_buy'], 2)
    df['p_sell'] = round(df['p_sell'], 2)
    df['count_buy'] = round(df['count_buy'], 2)
    #print('count_sell = ', df['count_sell'])
    #df['count_sell'] = round(df['count_sell'], 2)
    df['count_total_buy'] = round(df['count_total_buy'], 2)
    df['costs_of_bying'] = round(df['costs_of_bying'], 2)
    df['sum_invested'] = round(df['sum_invested'], 2)

    return df, Profit


def prod(j, array):
    p = 1
    if j == 0:
        return p * (1 - array[0])
    else:
        return prod(j-1, array) * (1-array[j])


# procent = [0, 0.15, 0.20, 0.25, 0.30]
# amounts_S = [1000,1000,2000,4000,8000]
# r_fin = 10
# procent_loss = 10
# r = 10
