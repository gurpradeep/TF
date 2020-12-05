import numpy as np
import pandas as pd
from pandas_datareader import data
from sklearn.preprocessing import MinMaxScaler
#import dataviz libraries
import matplotlib.pylab as plt
####
tsla = data.DataReader("TSLA",start='2015-1-1',end='2019-12-31',data_source='yahoo')
#print(tsla.head())
print("Number of rows and columns:", tsla.shape)

####split dataset
training_set = tsla.iloc[:800,1:2].values
test_set = tsla.iloc[800:,1:2].values


###scalar
sc =MinMaxScaler(feature_range=(0,1))
trained_scaled_set = sc.fit_transform(training_set)

#60 timesteps
nTimeSteps=60
xTrain,yTrain =[],[]
for i in range (nTimeSteps,800):
    xTrain.append(trained_scaled_set[i-nTimeSteps:i,0])
    yTrain.append(trained_scaled_set[i,0])

print(len(xTrain))
print(len(xTrain[0]))

import numpy as np
x_train , y_train = np.array(xTrain),np.array(yTrain)

print(x_train.shape)
print(y_train.shape)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

#LSTM

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import *

model = Sequential()
#input layer
model.add(LSTM(units=50,return_sequences=True,input_shape=(x_train.shape[1],1)))
model.add(Dropout(0.2))
#layer 2
model.add(LSTM(units=50,return_sequences=True))
model.add(Dropout(0.2))
#layer 3
model.add(LSTM(units=50,return_sequences=True))
model.add(Dropout(0.2))
#layer 4
model.add(LSTM(units=50))
model.add(Dropout(0.2))
#output layer
model.add(Dense(units =1))

#compile model
model.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Fitting the RNN to the Training set
model.fit(x_train, y_train, epochs = 20, batch_size = 32)

###Training done########################

#####Testing#######
dataset_train = tsla.iloc[:800, 1:2]
dataset_test = tsla.iloc[800:, 1:2]
dataset_total = pd.concat((dataset_train, dataset_test), axis = 0)
inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)
X_test = []
for i in range(60, 519):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
print(X_test.shape)
# (459, 60, 1)

predicted_stock_price = model.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

import matplotlib.pyplot as plt
plt.plot(tsla.loc[800:, "Date"],dataset_test.values, color = "red", label = "Real TESLA Stock Price")
plt.plot(tsla .loc[800:, "Date"],predicted_stock_price, color = "blue", label = "Predicted TESLA Stock Price")
plt.xticks(np.arange(0,459,50))
plt.title('TESLA Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('TESLA Stock Price')
plt.legend()
plt.show()