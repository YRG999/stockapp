# stockpred2.py

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('SPY_stock_data.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Number of previous days' data to use for prediction
lookback = 60

# Extract the adjusted closing prices
prices = data['Adj Close'].values.reshape(-1, 1)

# Scale the data to be between 0 and 1
scaler = MinMaxScaler(feature_range=(0, 1))
prices = scaler.fit_transform(prices)

# Split the data into training and test sets
train_size = int(len(prices) * 0.8)
train, test = prices[0:train_size], prices[train_size - lookback:]

# Function to create a dataset for the LSTM model
def create_dataset(dataset, lookback):
    dataX, dataY = [], []
    for i in range(lookback, len(dataset)):
        a = dataset[i - lookback:i, 0]
        dataX.append(a)
        dataY.append(dataset[i, 0])
    return np.array(dataX), np.array(dataY)

# Create the data for the LSTM model
trainX, trainY = create_dataset(train, lookback)
testX, testY = create_dataset(test, lookback)

# Reshape the data to be 3D as required by the LSTM model
trainX = np.reshape(trainX, (trainX.shape[0], trainX.shape[1], 1))
testX = np.reshape(testX, (testX.shape[0], testX.shape[1], 1))

# Initialize the LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(trainX.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(1))

# Compile and fit the LSTM model
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=1, batch_size=1, verbose=2)

# Number of days into the future to predict
forecast_days = 90

# Take the last `lookback` days of prices and scale it
inputs = prices[-lookback:]

# List to hold the predicted prices
predicted_future = []

# Predict the next `forecast_days` days
for _ in range(forecast_days):
    # Reshape the inputs
    X_test = np.reshape(inputs, (1, lookback, 1))
    
    # Make a prediction and undo the scaling
    pred_price = model.predict(X_test)
    
    # Add the prediction to the list of predicted future prices
    predicted_future.append(scaler.inverse_transform(pred_price)[0,0])
    
    # Update the inputs with the predicted price
    inputs = np.append(inputs[1:], pred_price, axis=0)

# Create a list of dates for the predicted prices
last_date = data.index[-1]
forecast_dates = pd.date_range(start=last_date, periods=forecast_days + 1).tolist()[1:]

# Plot the actual and predicted prices
plt.figure(figsize=(14,7))
plt.plot(data.index, data['Adj Close'], color='blue', label='Actual SPY Price')
plt.plot(forecast_dates, predicted_future, color='red', label='Predicted SPY Price')
plt.title('SPY Price Prediction')
plt.xlabel('Time')
plt.ylabel('SPY Price')
plt.legend()
plt.show()
