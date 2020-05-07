

                                ################ INSTALLING PACKAGES ################
#############################################################################################################
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_process import arma_generate_sample
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.statespace.sarimax import SARIMAX




                        ##################### UPLOADING DATA #####################
####################################################################################################################
df = pd.read_csv('MMM.csv', sep=',')
df.drop(df.tail(1).index,inplace=True)
df.sort_index(ascending=False, inplace=True)
df.reset_index(drop=True, inplace=True)
df = df['Open']
print(len(df))



                            ############   CREATE ARMA MODEL  ############
################################################################################################
arima = SARIMAX(df, order=(1,0,1)) # when generating data, d=0 !
arima_results = arima.fit()


                            ############ EXTRACTING PARAMETERS ############
################################################################################################
print(arima_results.summary())
print(arima_results.params.sigma2)
print(arima_results.params[0])




                                ################ GENERATING DATA ################
#############################################################################################################
# GENERATING DATA from PARAMETERS
# import arma_generate_sample function
from statsmodels.tsa.arima_process import arma_generate_sample
ar_coefs = [1, - arima_results.params[0]]
ma_coefs = [1, arima_results.params[1]]
std = np.sqrt(arima_results.params.sigma2) ## sigma
nsample = len(df)
start_price = df[nsample-1]         ## початкова ціна акції


for i in range (100):
    y = arma_generate_sample(ar_coefs, ma_coefs, nsample=nsample, sigma=std)+start_price
    sdf = pd.DataFrame(y)
    # print(sdf)
    file_name = 'data_' + str(i) + '.csv'
    sdf.to_csv(file_name, sep = ',', index=False,)
    print("Файл создан: ", file_name, "\n")
    plt.plot(sdf, linewidth=0.5)

plt.plot(df.index-nsample, df, label='MMM', color="k", linewidth=1)  ## plot real historical stock data
plt.xlabel('DAYS')
plt.ylabel('PRICE')
plt.legend()
plt.show()