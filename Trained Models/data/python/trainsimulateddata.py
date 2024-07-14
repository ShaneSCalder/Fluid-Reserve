import numpy as np
import pandas as pd
import os

# Function to load historical data
def load_historical_data(token):
    filename = f'data/{token}_1m_data.csv'
    return pd.read_csv(filename, parse_dates=['Datetime'], index_col='Datetime')

# Function to perform Monte Carlo simulation
def monte_carlo_simulation(historical_data, periods=1440*14, simulations=1000):
    log_returns = np.log(historical_data / historical_data.shift(1)).dropna()
    mean = log_returns.mean()
    variance = log_returns.var()

    monte_carlo_results = np.zeros((periods, simulations))
    initial_price = historical_data.iloc[-1]

    for i in range(simulations):
        prices = [initial_price]
        for _ in range(periods):
            shock = np.random.normal(mean, np.sqrt(variance))
            price = prices[-1] * np.exp(shock)
            prices.append(price)
        monte_carlo_results[:, i] = prices[1:]
    
    return monte_carlo_results

# Function to calculate the range between p30 and p70
def calculate_percentile_range(monte_carlo_results):
    p30 = np.percentile(monte_carlo_results, 43, axis=1)
    p70 = np.percentile(monte_carlo_results, 60, axis=1)
    return p30, p70

# Function to generate synthetic data
def generate_synthetic_data(token, periods=1440*14, seed=None):
    if seed is not None:
        np.random.seed(seed)
    historical_data = load_historical_data(token)['Close']
    monte_carlo_results = monte_carlo_simulation(historical_data, periods)
    p30, p70 = calculate_percentile_range(monte_carlo_results)
    
    dates = pd.date_range(start='2024-01-01', periods=periods, freq='1min')
    synthetic_data = pd.DataFrame(index=dates, columns=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
    
    for i in range(periods):
        price = np.random.uniform(p30[i], p70[i])
        synthetic_data.iloc[i] = [price, price, price, price, price, 0]  # Setting volume to 0
    
    return synthetic_data

# Function to aggregate data to different intervals
def aggregate_data(data, interval):
    ohlc_dict = {
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Adj Close': 'last',
        'Volume': 'sum'
    }
    return data.resample(interval).apply(ohlc_dict)

# Main function to generate and save simulated data
def main():
    tokens = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'Cake-USD', 'UNI-USD']
    base_dir = 'traineddata'
    os.makedirs(base_dir, exist_ok=True)
    
    for test_num in range(1, 11):  # Generate 10 different datasets
        test_dir = os.path.join(base_dir, f'testdata{test_num}')
        os.makedirs(test_dir, exist_ok=True)
        
        for token in tokens:
            print(f"Generating synthetic data for {token} in test set {test_num}...")
            synthetic_data_1m = generate_synthetic_data(token, seed=test_num)
            synthetic_data_1m.to_csv(os.path.join(test_dir, f'{token}_1m_simulated.csv'))
            
            synthetic_data_5m = aggregate_data(synthetic_data_1m, '5T')
            synthetic_data_5m.to_csv(os.path.join(test_dir, f'{token}_5m_simulated.csv'))
            
            synthetic_data_15m = aggregate_data(synthetic_data_1m, '15T')
            synthetic_data_15m.to_csv(os.path.join(test_dir, f'{token}_15m_simulated.csv'))

if __name__ == "__main__":
    main()