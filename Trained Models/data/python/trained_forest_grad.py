import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import os
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

# Function to load and preprocess data from the data directory
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

        # Initialize the models
        rf_model = RandomForestRegressor(random_state=42)
        gb_model = GradientBoostingRegressor(random_state=42)

        # Hyperparameter tuning using GridSearchCV
        rf_param_grid = {
            'n_estimators': [100, 200],
            'max_depth': [10, 20, None],
            'min_samples_split': [2, 5, 10]
        }

        gb_param_grid = {
            'n_estimators': [100, 200],
            'learning_rate': [0.01, 0.1, 0.2],
            'max_depth': [3, 5, 10]
        }

        rf_grid_search = GridSearchCV(rf_model, rf_param_grid, cv=5, scoring='neg_mean_squared_error')
        gb_grid_search = GridSearchCV(gb_model, gb_param_grid, cv=5, scoring='neg_mean_squared_error')

        # Fit the models
        rf_grid_search.fit(X_train, y_train)
        gb_grid_search.fit(X_train, y_train)

        # Get the best models
        best_rf_model = rf_grid_search.best_estimator_
        best_gb_model = gb_grid_search.best_estimator_

        # Save the trained models
        rf_model_filename = f'trained/{symbol}_{interval}_rf_model.joblib'
        gb_model_filename = f'trained/{symbol}_{interval}_gb_model.joblib'
        joblib.dump(best_rf_model, rf_model_filename)
        joblib.dump(best_gb_model, gb_model_filename)

        # Predict and evaluate the models
        rf_predictions = best_rf_model.predict(X_test)
        gb_predictions = best_gb_model.predict(X_test)

        # Calculate performance metrics
        rf_mse = mean_squared_error(y_test, rf_predictions)
        gb_mse = mean_squared_error(y_test, gb_predictions)

        rf_r2 = r2_score(y_test, rf_predictions)
        gb_r2 = r2_score(y_test, gb_predictions)

        print(f'{symbol} - {interval} - Best Random Forest MSE: {rf_mse}, R2: {rf_r2}')
        print(f'{symbol} - {interval} - Best Gradient Boosting MSE: {gb_mse}, R2: {gb_r2}')

        # Plot the predictions
        plt.figure(figsize=(14, 7))
        plt.plot(y_test.values, label='Actual Prices')
        plt.plot(rf_predictions, label='Random Forest Predictions')
        plt.plot(gb_predictions, label='Gradient Boosting Predictions')
        plt.legend()
        plt.title(f'{symbol} - {interval} - Model Predictions vs Actual Prices')
        plt.show()
