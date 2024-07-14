# Fluid-Reserve
 Fluid Reserve ETHGlobal Brussels hackathon Project July 12 - 14 

![FluidReservelogo](https://github.com/user-attachments/assets/659d0930-8a34-484e-9152-a9c9f422b199)

# Problem Statement 1: 

## Strategic Liquidity Provisions and Management 

In decentralized finance (DeFi), Uniswap v4 and PancakeSwap have emerged as leading automated market makers (AMMs) allowing for decentralized token swaps. However, liquidity providers face various challenges, including impermanent loss, sandwich attacks, and arbitrage opportunities that can affect their profitability. Additionally, market sentiment significantly influences these opportunities. Thus, integrating sentiment analysis can enhance the effectiveness of liquidity provision strategies across multiple platforms.

This project aims to develop a multi-agent Q-learning based liquidity agent that dynamically adjusts liquidity provision strategies in response to market events and sentiment analysis. The agents will be designed to operate on both Uniswap v4 and PancakeSwap, identifying optimal moments for liquidity provision, mitigating risks, and maximizing profitability by effectively responding to market conditions and sentiment indicators from sources like Twitter, Gecko, and betting pools.

## Objectives

1. Develop a Multi-Agent Q-learning Algorithm: Design and implement a multi-agent Q-learning framework capable of learning optimal strategies for liquidity provision on Uniswap v4 and PancakeSwap.

2. Event Detection and Sentiment Analysis: Integrate market event detection and sentiment analysis mechanisms to trigger the agents' actions, focusing on events that typically lead to sandwich attacks, arbitrage opportunities, and sentiment-driven market movements.

3. Risk Mitigation: Implement strategies within the Q-learning framework to mitigate sandwich attacks and minimize losses due to arbitrage.

4. Profit Maximization: Ensure the agents can adjust liquidity positions to maximize returns based on historical, real-time market data, and sentiment analysis across both platforms.

5. Utilize Stable coins like USDC (Circle) to optimize risk management.

---

## Solution Overview

1. Multi-Agent Q-learning Algorithm Design

- State Space: Define the state space to include relevant market conditions such as token prices, liquidity pool sizes, recent trade volumes, historical volatility, and sentiment scores.
Action Space: Define actions such as adding liquidity, removing liquidity, or adjusting the position within the liquidity range for both Uniswap v4 and PancakeSwap.

- Reward Function: Design a reward function that incentivizes actions leading to higher returns and penalizes actions resulting in losses due to sandwich attacks or arbitrage.

2. Event Detection and Sentiment Analysis Mechanisms

- Market Data Analysis: Use real-time and historical data to detect significant market events such as large trades or rapid price changes that typically precede sandwich attacks or create arbitrage opportunities.

- Sentiment Analysis: Integrate sentiment analysis from various sources (Twitter/X, Gecko, betting pools) to gauge market sentiment and predict potential market movements.

- Data Sources: Collect and preprocess sentiment data from Twitter/X, Gecko, and betting pools.

- Sentiment Scoring: Develop a sentiment scoring mechanism to quantify the market sentiment and incorporate it into the state space.

- Trigger Events: Implement triggers within the Q-learning algorithm to adjust liquidity positions based on detected events and sentiment changes.

3. Risk Mitigation Strategies

- Sandwich Attack Mitigation: Develop strategies to detect and avoid sandwich attacks, such as monitoring for suspicious transaction patterns and adjusting liquidity positions accordingly.

- Arbitrage Reduction: Implement measures to minimize the agents’ exposure to arbitrage, such as setting tight ranges for liquidity provision and dynamically adjusting these ranges based on market and sentiment conditions.

4. Profit Maximization

- Dynamic Adjustments: Allow the agents to dynamically adjust positions to capitalize on market conditions, utilizing a reward function that reflects both immediate and long-term profitability.

- Monte Carlo Analysis and Simulation:

- Historical Data and Monte Carlo Analysis: Use historical market data to perform Monte Carlo analysis, focusing on reducing the volatility range to a P40 to P60 confidence interval. This approach aims to filter out outlier information and create a more realistic training set.

- Simulation in 14-Day Increments: Simulate market data in 14-day increments within the P40 to P60 range. This simulated data will be used to train the meta stack, providing a balanced and realistic scenario for the Q-learning agents' trading decisions.

5. Future Learning Development

- Sentiment Analysis Integration: Continuously improve sentiment analysis algorithms to better predict market movements based on sentiment data.

- Machine Learning Enhancements: Incorporate advanced machine learning techniques, such as reinforcement learning with deep neural networks (Deep Q-Learning), to enhance the decision-making capabilities of the agents.

- Scalability and Adaptability: Ensure the multi-agent system is scalable and can adapt to evolving market conditions and new data sources.

---

## Q-Learning Meta Stack for Time-Series Predictions Work Flow

<img width="2880" alt="Fluid-Reserve" src="https://github.com/user-attachments/assets/0bf14202-7d4d-409d-86dd-440d3550baa9">

---

- Times series models and tools can be alterred to provide different outputs, Ai Q learning environment is modular and can support different requirements and outcomes. 

---

![Digital_Island](https://github.com/user-attachments/assets/5c2d9d43-5782-48ff-8854-efab226d3cf0)

---
# Problem Statement 2: 

## Maximizing short term times series profits while reducing risk

In decentralized finance (DeFi) and cryptocurrency trading, identifying optimal trading opportunities is crucial for maximizing returns. The volatility and complexity of markets for assets such as BTC, ETH, CAKE, BNB, and UNI present significant challenges. Utilizing advanced machine learning techniques, specifically Q-learning with a multi-agent approach, can enable traders to navigate these markets effectively.

This project aims to develop a multi-agent Q-learning based trading system that dynamically adjusts trading strategies in response to market events and sentiment analysis. The agents will focus on identifying trading opportunities for BTC, ETH, CAKE, BNB, and UNI, leveraging time series data, market indicators, and sentiment analysis from various sources like Twitter, Gecko, and betting pools.

---

## Objectives

1. Develop a Multi-Agent Q-learning Algorithm: Design and implement a multi-agent Q-learning framework capable of learning optimal trading strategies for BTC, ETH, CAKE, BNB, and UNI.
2. Event Detection and Sentiment Analysis: Integrate market event detection and sentiment analysis mechanisms to trigger the agents' actions, focusing on events that typically lead to significant price movements and trading opportunities.

3. Risk Management: Implement strategies within the Q-learning framework to manage trading risks and minimize losses.

4. Profit Maximization: Ensure the agents can adjust trading positions to maximize returns based on historical, real-time market data, and sentiment analysis.

---

## Solution Overview

1. Multi-Agent Q-learning Algorithm Design

- State Space: Define the state space to include relevant market conditions such as asset prices, volume, historical volatility, technical indicators (e.g., RSI, MACD), and sentiment scores.

- Action Space: Define actions such as buy, sell, or hold for each asset.

- Reward Function: Design a reward function that incentivizes profitable trades and penalizes actions resulting in losses.

2. Event Detection and Sentiment Analysis Mechanisms

- Market Data Analysis: Use real-time and historical data to detect significant market events such as large trades or rapid price changes that typically precede trading opportunities.

- Sentiment Analysis: Integrate sentiment analysis from various sources (Twitter/X, Gecko, betting pools) to gauge market sentiment and predict potential market movements.

- Data Sources: Collect and preprocess sentiment data from Twitter/X, Gecko, and betting pools.

- Sentiment Scoring: Develop a sentiment scoring mechanism to quantify the market sentiment and incorporate it into the state space.

- Trigger Events: Implement triggers within the Q-learning algorithm to adjust trading positions based on detected events and sentiment changes.

3. Risk Management Strategies

- Risk Assessment: Develop strategies to assess and manage risks associated with trading, such as stop-loss orders and position sizing.

- Diversification: Implement diversification strategies to spread risk across multiple assets and minimize exposure to any single asset.

4. Profit Maximization

- Dynamic Adjustments: Allow the agents to dynamically adjust trading positions to capitalize on market conditions, utilizing a reward function that reflects both immediate and long-term profitability.

- Monte Carlo Analysis and Simulation:

- Historical Data and Monte Carlo Analysis: Use historical market data to perform Monte Carlo analysis, focusing on reducing the volatility range to a P40 to P60 confidence interval. This approach aims to filter out outlier information and create a more realistic training set.

- Simulation in 14-Day Increments: Simulate market data in 14-day increments within the P40 to P60 range. This simulated data will be used to train the meta stack, providing a balanced and realistic scenario for the Q-learning agents' trading decisions.

5. Future Learning Development

- Sentiment Analysis Integration: Continuously improve sentiment analysis algorithms to better predict market movements based on sentiment data.

- Machine Learning Enhancements: Incorporate advanced machine learning techniques, such as reinforcement learning with deep neural networks (Deep Q-Learning), to enhance the decision-making capabilities of the agents.

- Scalability and Adaptability: Ensure the multi-agent system is scalable and can adapt to evolving market conditions and new data sources.
---

# Uniswap Hook for Pool Data Logging

This project leverages Uniswap v4 hooks to create a smart contract that logs transaction data from Uniswap pools. The contract, deployed using Hardhat, interacts with Uniswap pools to fetch and log transaction details such as transaction hash, block number, sender, receiver, gas used, and timestamp. The logged data is then exported to a JSON file for further analysis or integration into other DeFi applications.

### Key Features

- **Uniswap v4 Hooks Integration**: Utilizes Uniswap v4 hooks for enhanced interaction with Uniswap pools.
- **Comprehensive Data Logging**: Captures detailed transaction data including transaction hash, block number, addresses, gas used, and timestamps.
- **JSON Export**: Logs transaction data into a JSON file for easy access and analysis.

### [Instructions on How to Use](https://github.com/ShaneSCalder/Fluid-Reserve/tree/main/Contracts)

---

# PancakeSwap Hook for Token Transaction Logging

This project leverages PancakeSwap's smart contracts to create a logging system for token transactions. The deployed contract interacts with PancakeSwap pools to fetch and log detailed transaction data such as token addresses, transaction hash, block number, sender, receiver, amount, gas used, and timestamp. The logged data is then exported to a JSON file for further analysis or integration into other DeFi applications.

### Key Features

- **PancakeSwap Integration**: Utilizes PancakeSwap's smart contracts to log token transactions.
- **Comprehensive Data Logging**: Captures detailed transaction data including token addresses, transaction hash, block number, sender, receiver, amount, gas used, and timestamp.
- **JSON Export**: Logs transaction data into a JSON file for easy access and analysis.

### [Instructions on How to Use](https://github.com/ShaneSCalder/Fluid-Reserve/tree/main/Contracts)

---

## Fluid Reserve

Fluid Reserve is a sophisticated web application built with Go that offers an array of features tailored for AI trading, data logging from decentralized exchanges, and token price analysis. The application integrates with MetaMask for wallet connectivity, providing a seamless and interactive user experience.

### High-Level Overview

### **Features**

- **AI Trading Agents**: 
  - Users can select and configure various AI trading agents to perform different trading strategies. These agents leverage advanced machine learning models to make informed trading decisions.

- **Data Hooks for Uniswap and PancakeSwap**:
  - The application includes smart contracts that log transaction data from Uniswap and PancakeSwap. This data is exported to JSON files for further analysis or integration into other DeFi applications.

- **Token Price Analysis**:
  - Users can visualize token price movements with interactive charts. The charts display critical metrics like trading volume and momentum, providing deep insights into market behavior.

- **MetaMask Integration**:
  - Users can connect their MetaMask wallet directly from the web interface, allowing them to interact with the application seamlessly. This feature enhances the user experience by providing easy access to blockchain interactions.

### **Installation and Usage**

To get started with Fluid Reserve, follow the installation instructions provided in the GitHub repository:

[Fluid Reserve GitHub Repository](https://github.com/ShaneSCalder/Fluid-Reserve/tree/main/APP)

---

### **Installation Instructions (from GitHub)**

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/fluid-reserve.git
   cd fluid-reserve
   ```

2. **Install Go**: Ensure you have Go installed. You can download it from [golang.org](https://golang.org/).

3. **Install dependencies**:
   ```sh
   go mod tidy
   ```

4. **Build the application**:
   ```sh
   go build -o bin/main ./cmd/main.go
   ```

5. **Run the application**:
   ```sh
   ./bin/main
   ```

6. **Open your browser** and navigate to `http://localhost:8080`.

### **MetaMask Integration**

To connect your MetaMask wallet:
1. Click the "Connect Wallet" button in the navbar.
2. Allow the connection in the MetaMask popup.
3. Your wallet address will be displayed on the button upon successful connection.

For detailed instructions and additional information, please visit the [Fluid Reserve GitHub Repository](https://github.com/ShaneSCalder/Fluid-Reserve/tree/main/APP).

---

This high-level overview provides a concise summary of what the Go application does, its key features, and instructions on how to get started, including a link to the repository for further details.

---

![Aanne](https://github.com/user-attachments/assets/0e5b2224-d523-42bb-a9e8-5c8638721e98)

---

## Introducing the Q-Learning Meta Stack for Time-Series Predictions

Unlock the Future of AI with Adaptive Time-Series Predictions

Our innovative Q-Learning Meta Stack harnesses the power of advanced machine learning models and reinforcement learning to deliver unparalleled accuracy and adaptability in real-time data predictions. Designed to thrive in dynamic environments, our system integrates multiple AI models, including Random Forests, Gradient Boosters, LSTMs, and Neural Networks, ensuring precise predictions and efficient resource allocation.

### Key Features

- **Adaptive Decision-Making**: Employ Q-learning to dynamically select optimal models.
- **Continuous Learning**: Refine and update models with live data for ongoing improvement.
- **High Efficiency**: Streamline resource allocation for peak performance.

Experience the cutting edge of AI technology with our Q-Learning Meta Stack, where predictive accuracy meets real-time adaptability. Join us in revolutionizing time-series predictions today!

## Repository Overview

This repository provides the building blocks and examples needed to get started with the Q-Learning Meta Stack for time-series predictions. While the repository does not include the Q-learning environment itself due to our IP restrictions, it offers comprehensive guidance on training and simulating data using Monte Carlo analysis and historical data.

### Contents

- **Monte Carlo Analysis**: Techniques to generate and analyze simulated data for robust model training.
- **Historical Data Handling**: Methods to leverage historical data for model training and validation.
- **Simulated Data Generation**: Tools to create simulated datasets for various time-series scenarios.
- **Agent Results and Storage**: Save and utilize trained agents for future training and prediction tasks.
- **Training Models**: Instructions to train multiple models, including Random Forest, Gradient Boosting, Neural Networks, and LSTMs.

## Getting Started

To get started with building your own Q-Learning Meta Stack and utilizing the provided examples:

### Prerequisites

- **Python**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).
- **Dependencies**: Install the necessary Python packages using the following command:
  ```sh
  pip install -r requirements.txt
  ```

### Training and Simulation

1. **Monte Carlo Analysis**: Use the provided scripts to perform Monte Carlo analysis and generate simulated data.
2. **Historical Data Utilization**: Learn how to incorporate historical data into your training process.
3. **Training Models**: Follow the examples to train Random Forest, Gradient Boosting, Neural Networks, and LSTM models.

### Example Usage

Below is an example of how to train a Random Forest model using the provided scripts:

```python
import pandas as pd
from models.random_forest import train_random_forest

# Load your data
data = pd.read_csv('data/historical_data.csv')

# Train the Random Forest model
model = train_random_forest(data)

# Save the trained model
model.save('models/random_forest_model.pkl')
```

### Future Work

While this repository provides the foundational elements, future work involves integrating a Q-learning environment to dynamically select and employ these trained models in real-time data prediction scenarios.

---

For detailed instructions and additional information, please visit the [Fluid Reserve GitHub Repository]([https://github.com/ShaneSCalder/Fluid-Reserve/tree/main/Trained Models](https://github.com/ShaneSCalder/Fluid-Reserve/tree/main/Trained%20Models)).

---
