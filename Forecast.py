import numpy as np
import pandas as pd
from pandas_datareader import data
#import dataviz libraries
import matplotlib.pyplot as plt
import seaborn as sns

aapl = data.DataReader("AAPL",start='2015-1-1',end='2019-12-31',data_source='yahoo')
print(aapl.head())
sns.set(style='darkgrid')
#Plot "Adj Close"
plt.figure(figsize=(12,8))
sns.lineplot(x=aapl.index, y='Adj Close', data=aapl)
plt.title("APPLE Stock Prices", fontsize=15)

hist = []
target = []
length = 90
adj_close = aapl['Adj Close']
for i in range(len(adj_close) - length):
   x = adj_close[i:i+length]
   print(x)
   y = adj_close[i+length]
   print(y)
   hist.append(x)
   target.append(y)

target = np.array(target)

hist = np.array(hist)
target = target.reshape(-1,1)
print(hist.shape)
print(target.shape)


X_train = hist[:1138]
X_test = hist[1138:]
y_train = target[:1138]
y_test = target[1138:]


from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
#train set, fit_transform
X_train_scaled = sc.fit_transform(X_train)
y_train_scaled = sc.fit_transform(y_train)
#test set, only transform
X_test_scaled = sc.transform(X_test)
y_test_scaled = sc.transform(y_test)

X_train_scaled = X_train_scaled.reshape((len(X_train_scaled), length, 1))
X_test_scaled = X_test_scaled.reshape((len(X_test_scaled), length, 1))

import tensorflow as tf
from tensorflow.keras import layers

model = tf.keras.Sequential()
model.add(layers.LSTM(units=64, return_sequences=True, input_shape=(90,1), dropout=0.2))
model.add(layers.LSTM(units=32, return_sequences=True, dropout=0.2))
model.add(layers.LSTM(units=32, return_sequences=True, dropout=0.2))
model.add(layers.LSTM(units=16, dropout=0.2))
model.add(layers.Dense(units=1))
model.summary()


model.compile(optimizer='adam', loss='mean_squared_error')

history = model.fit(X_train_scaled, y_train_scaled,
                    epochs=10, batch_size=16)

loss = history.history['loss']
epoch_count = range(1, len(loss) + 1)
plt.figure(figsize=(12,8))
plt.plot(epoch_count, loss, 'r--')
plt.legend(['Training Loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show();


pred = model.predict(X_test_scaled)
pred_transformed = sc.inverse_transform(pred)
y_test_transformed = sc.inverse_transform(y_test_scaled)
plt.figure(figsize=(12,8))
plt.plot(y_test_transformed, color='blue', label='Real')
plt.plot(pred_transformed, color='red', label='Prediction')
plt.title('Apple Stock Price Prediction')
plt.legend()
plt.show()