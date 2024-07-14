import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('CAKE-USD_1m_data.csv')

# Convert Datetime column to datetime object
data['Datetime'] = pd.to_datetime(data['Datetime'])

# Set the Datetime column as the index
data.set_index('Datetime', inplace=True)

# Pull the last 2 hours of data
two_hour_data = data.last('2H')

# Ensure that data is sorted by Datetime
two_hour_data = two_hour_data.sort_index()

# Calculate momentum from volume
two_hour_data['Volume_Momentum'] = two_hour_data['Volume'].diff()

# Plot composite graph
plt.figure(figsize=(12, 8))

# Trading Volume
plt.plot(two_hour_data.index, two_hour_data['Volume'], label='Volume', color='blue', linestyle='-', marker='o')

# Volume Momentum
plt.plot(two_hour_data.index, two_hour_data['Volume_Momentum'], label='Volume Momentum', color='green', linestyle='--', marker='x')

plt.title('CAKE-USD Volume and Momentum Analysis (Last 2 Hours)')
plt.xlabel('Datetime')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.savefig('CAKE-USD_volume_momentum_analysis.png')
plt.show()





















