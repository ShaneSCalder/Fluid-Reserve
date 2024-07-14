import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import joblib

# Preprocess the data
def preprocess_data(filename):
    data = pd.read_csv(filename, parse_dates=['Datetime'], index_col='Datetime')

    # Calculate price changes
    data['price_change'] = data['Close'].pct_change()

    # Calculate volatility
    data['volatility'] = data['price_change'].rolling(window=12).std()  # Adjust window size as needed

    # Calculate volume
    data['volume'] = data['Volume'].rolling(window=12).sum()

    # Calculate RSI
    def calculate_rsi(data, window):
        delta = data.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    data['rsi'] = calculate_rsi(data['Close'], window=12)

    # Calculate moving averages
    data['short_ma'] = data['Close'].rolling(window=3).mean()
    data['long_ma'] = data['Close'].rolling(window=9).mean()

    # Drop NA values
    data.dropna(inplace=True)

    return data

# Load and preprocess data
def load_and_preprocess_data(symbol, interval):
    filename = f'data/{symbol}_{interval}_data.csv'
    return preprocess_data(filename)

# Create directories if they don't exist
if not os.path.exists('data'):
    os.makedirs('data')
if not os.path.exists('trained'):
    os.makedirs('trained')

# Load and preprocess data for each interval
symbols = ['BNB-USD', 'BTC-USD', 'ETH-USD', 'CAKE-USD', 'UNI-USD']
intervals = ['1m', '5T', '15T']

# Function to build and save LSTM model
def build_and_save_lstm_model(symbol, interval, X_train, y_train, X_test, y_test):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(LSTM(units=50))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')

    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), verbose=2)

    model_filename = f'trained/{symbol}_{interval}_lstm_model.h5'
    model.save(model_filename)
    print(f"Saved LSTM model: {model_filename}")

# Function to build and save a basic neural network model
def build_and_save_nn_model(symbol, interval, X_train, y_train, X_test, y_test):
    model = Sequential()
    model.add(Dense(64, activation='relu', input_dim=X_train.shape[1]))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')

    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), verbose=2)

    model_filename = f'trained/{symbol}_{interval}_nn_model.h5'
    model.save(model_filename)
    print(f"Saved Neural Network model: {model_filename}")

# Loop through each symbol and interval
for symbol in symbols:
    for interval in intervals:
        data = load_and_preprocess_data(symbol, interval)

        # Features and target variable
        features = ['price_change', 'volatility', 'volume', 'rsi', 'short_ma', 'long_ma']
        target = 'Close'

        X = data[features]
        y = data[target]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Scale the features
        scaler = MinMaxScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Save the scaler
        scaler_filename = f'trained/{symbol}_{interval}_scaler.joblib'
        joblib.dump(scaler, scaler_filename)
        print(f"Saved scaler: {scaler_filename}")

        # Reshape data for LSTM model
        X_train_lstm = X_train_scaled.reshape((X_train_scaled.shape[0], 1, X_train_scaled.shape[1]))
        X_test_lstm = X_test_scaled.reshape((X_test_scaled.shape[0], 1, X_test_scaled.shape[1]))

        # Build and save models
        build_and_save_lstm_model(symbol, interval, X_train_lstm, y_train, X_test_lstm, y_test)
        build_and_save_nn_model(symbol, interval, X_train_scaled, y_train, X_test_scaled, y_test)
