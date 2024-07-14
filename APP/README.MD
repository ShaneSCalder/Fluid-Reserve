

### `README.md` for Fluid Reserve Go Website

```markdown
# Fluid Reserve

Fluid Reserve is a Go-based web application designed to provide AI trading agents, data hooks for Uniswap and PancakeSwap, and comprehensive token price analysis. The application leverages modern web technologies and MetaMask integration for an enhanced user experience.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [MetaMask Integration](#metamask-integration)
- [License](#license)

## Overview

Fluid Reserve is a sophisticated web application that allows users to interact with AI trading agents, view data logged from Uniswap and PancakeSwap pools, and analyze token price movements. The application includes a user-friendly interface with sections for agent trading, APR balancing, portfolio management, and data hooks.

## Features

- **AI Trading Agents**: Select and configure AI trading agents to perform various trading strategies.
- **Data Hooks**: Log transaction data from Uniswap and PancakeSwap using hooks.
- **Token Price Analysis**: Visualize token price movements with interactive charts.
- **MetaMask Integration**: Connect your MetaMask wallet to interact with the application.
- **Responsive Design**: User-friendly and responsive web interface.

## Installation

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

## Usage

1. **Run the application**:
   ```sh
   ./bin/main
   ```

2. **Open your browser** and navigate to `http://localhost:8080`.

## Project Structure

```
fluid-reserve/
├── cmd/
│   └── main.go       # Entry point of the application
├── static/
│   ├── css/          # CSS files
│   ├── js/           # JavaScript files
│   └── images/       # Image assets
├── templates/
│   ├── base.html     # Base template
│   ├── navbar.html   # Navbar template
│   ├── home.html     # Home page template
│   ├── product1.html # Product 1 page template
│   ├── product2.html # Product 2 page template
│   ├── product3.html # Product 3 page template
│   └── aboutus.html  # About Us page template
├── static/data/
│   ├── CAKE-USD_1m_data.csv  # CAKE token data
│   ├── UNI-USD_1m_data.csv   # UNI token data
│   ├── createcakegraph.py    # Script to generate CAKE token graph
│   └── createunigraph.py     # Script to generate UNI token graph
└── README.md
```

## MetaMask Integration

To connect your MetaMask wallet:
1. Click the "Connect Wallet" button in the navbar.
2. Allow the connection in the MetaMask popup.
3. Your wallet address will be displayed on the button upon successful connection.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. Non comercial use full lisence coming soon

```

