# Fluid-Reserve
 Fluid Reserve ETHGlobal Brussels hackathon Project July 12 - 14 

![FluidReservelogo](https://github.com/user-attachments/assets/659d0930-8a34-484e-9152-a9c9f422b199)

# Strategic Liquidity Provisions and Management 

## Problem Statement

In decentralized finance (DeFi), Uniswap v4 and PancakeSwap have emerged as leading automated market makers (AMMs) allowing for decentralized token swaps. However, liquidity providers face various challenges, including impermanent loss, sandwich attacks, and arbitrage opportunities that can affect their profitability. Additionally, market sentiment significantly influences these opportunities. Thus, integrating sentiment analysis can enhance the effectiveness of liquidity provision strategies across multiple platforms.

This project aims to develop a multi-agent Q-learning based liquidity agent that dynamically adjusts liquidity provision strategies in response to market events and sentiment analysis. The agents will be designed to operate on both Uniswap v4 and PancakeSwap, identifying optimal moments for liquidity provision, mitigating risks, and maximizing profitability by effectively responding to market conditions and sentiment indicators from sources like Twitter, Gecko, and betting pools.

## Objectives

1. Develop a Multi-Agent Q-learning Algorithm: Design and implement a multi-agent Q-learning framework capable of learning optimal strategies for liquidity provision on Uniswap v4 and PancakeSwap.

2. Event Detection and Sentiment Analysis: Integrate market event detection and sentiment analysis mechanisms to trigger the agents' actions, focusing on events that typically lead to sandwich attacks, arbitrage opportunities, and sentiment-driven market movements.

3. Risk Mitigation: Implement strategies within the Q-learning framework to mitigate sandwich attacks and minimize losses due to arbitrage.

4. Profit Maximization: Ensure the agents can adjust liquidity positions to maximize returns based on historical, real-time market data, and sentiment analysis across both platforms.

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


## Q-Learning Meta Stack for Time-Series Predictions Work Flow

<img width="2880" alt="Fluid-Reserve" src="https://github.com/user-attachments/assets/0bf14202-7d4d-409d-86dd-440d3550baa9">

- Times series models and tools can be alterred to provide different outputs, Ai Q learning environment is modular and can support different requirements and outcomes. 

![Digital_Island](https://github.com/user-attachments/assets/5c2d9d43-5782-48ff-8854-efab226d3cf0)


# Maximizing short term times series profits while reducing risk

## Problem Statement

In decentralized finance (DeFi) and cryptocurrency trading, identifying optimal trading opportunities is crucial for maximizing returns. The volatility and complexity of markets for assets such as BTC, ETH, CAKE, BNB, and UNI present significant challenges. Utilizing advanced machine learning techniques, specifically Q-learning with a multi-agent approach, can enable traders to navigate these markets effectively.

This project aims to develop a multi-agent Q-learning based trading system that dynamically adjusts trading strategies in response to market events and sentiment analysis. The agents will focus on identifying trading opportunities for BTC, ETH, CAKE, BNB, and UNI, leveraging time series data, market indicators, and sentiment analysis from various sources like Twitter, Gecko, and betting pools.

## Objectives

1. Develop a Multi-Agent Q-learning Algorithm: Design and implement a multi-agent Q-learning framework capable of learning optimal trading strategies for BTC, ETH, CAKE, BNB, and UNI.
2. Event Detection and Sentiment Analysis: Integrate market event detection and sentiment analysis mechanisms to trigger the agents' actions, focusing on events that typically lead to significant price movements and trading opportunities.

3. Risk Management: Implement strategies within the Q-learning framework to manage trading risks and minimize losses.

4. Profit Maximization: Ensure the agents can adjust trading positions to maximize returns based on historical, real-time market data, and sentiment analysis.

Solution Overview

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
 
