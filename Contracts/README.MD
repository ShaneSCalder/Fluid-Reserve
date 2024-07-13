
# Uniswap Hook for Pool Data Logging

This repository contains a Hardhat project that deploys a smart contract to log transaction data from Uniswap pools. It includes scripts for deploying the contract and interacting with it to fetch and log transaction data.

## Features

- **Deploy Smart Contract**: Deploy a smart contract that interacts with Uniswap pools.
- **Transaction Logging**: Log transaction details such as transaction hash, block number, sender, receiver, gas used, and timestamp.
- **Export to JSON**: Save logged transaction data into a JSON file for further analysis.

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v14 or higher)
- [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)
- [Hardhat](https://hardhat.org/)
- [Infura](https://infura.io/) project ID
- Private key from a wallet with some testnet ETH

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/uniswap-hook.git
   cd uniswap-hook
   ```

2. **Install dependencies**:

   ```bash
   npm install
   ```

3. **Set up environment variables**:

   Create a `.env` file in the root directory with the following content:

   ```plaintext
   INFURA_PROJECT_ID=your_infura_project_id
   PRIVATE_KEY=your_private_key
   ```

### Configuration

1. **Hardhat Configuration**:

   Update `hardhat.config.js` with your network configuration:

   ```javascript
   require("@nomiclabs/hardhat-waffle");
   require("dotenv").config();

   module.exports = {
       solidity: "0.8.0",
       networks: {
           sepolia: {
               url: `https://sepolia.infura.io/v3/${process.env.INFURA_PROJECT_ID}`,
               accounts: [`0x${process.env.PRIVATE_KEY}`]
           }
       }
   };
   ```

### Deployment

1. **Deploy the Smart Contract**:

   ```bash
   npx hardhat run scripts/deploy.js --network sepolia
   ```

   This will deploy the `MultiPoolTransactionLogger` contract and output the deployed contract address.

### Interaction

1. **Log Transactions**:

   Update `scripts/interact.js` with the deployed contract address:

   ```javascript
   // scripts/interact.js
   const fs = require('fs');
   const path = require('path');

   async function main() {
       const [deployer] = await ethers.getSigners();
       const loggerAddress = "DEPLOYED_CONTRACT_ADDRESS"; // Replace with your deployed contract address

       const logger = await ethers.getContractAt("MultiPoolTransactionLogger", loggerAddress);

       console.log("Interacting with MultiPoolTransactionLogger at:", loggerAddress);

       // Log a manual transaction for testing
       const tx = await logger.postSwapHook(deployer.address, 1000, 2000, loggerAddress);
       const receipt = await tx.wait();

       console.log("Swap transaction logged");

       // Prepare the log entry
       const logEntry = {
           transactionHash: receipt.transactionHash,
           blockNumber: receipt.blockNumber,
           from: receipt.from,
           to: receipt.to,
           gasUsed: receipt.gasUsed.toString(),
           timestamp: new Date().toISOString()
       };

       // Read the existing log file or create a new one if it doesn't exist
       const logFilePath = path.join(__dirname, 'transaction_log.json');
       let logs = [];

       if (fs.existsSync(logFilePath)) {
           logs = JSON.parse(fs.readFileSync(logFilePath, 'utf8'));
       }

       // Add the new log entry
       logs.push(logEntry);

       // Write the updated logs to the file
       fs.writeFileSync(logFilePath, JSON.stringify(logs, null, 2), 'utf8');

       console.log("Transaction logged in transaction_log.json");
   }

   main()
       .then(() => process.exit(0))
       .catch((error) => {
           console.error(error);
           process.exit(1);
       });
   ```

2. **Run the Interaction Script**:

   ```bash
   npx hardhat run scripts/interact.js --network sepolia
   ```

   This will log the transaction data and save it to `transaction_log.json`.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

----

### Files Structure

Here's a quick overview of the files and directories in the project:

```
uniswap-hook/
├── contracts/
│   └── multi_pool.sol
├── scripts/
│   ├── deploy.js
│   └── interact.js
├── test/
│   └── sample-test.js
├── .env
├── .gitignore
├── hardhat.config.js
├── package-lock.json
├── package.json
└── README.md
```

This README should help you get started with using the Uniswap hook to pull pool data and log it using Hardhat.

---

# PancakeSwap Hook for Token Transaction Logging

This project leverages PancakeSwap's smart contracts to create a logging system for token transactions. The contract, deployed using Hardhat on the Sepolia testnet, interacts with PancakeSwap pools to fetch and log transaction data such as the token address, transaction hash, block number, sender, receiver, amount, gas used, and timestamp. The logged data is then exported to a JSON file for further analysis or integration into other DeFi applications.

## Features

- **PancakeSwap Integration**: Utilizes PancakeSwap's smart contracts to log token transactions.
- **Comprehensive Data Logging**: Captures detailed transaction data including token address, transaction hash, block number, sender, receiver, amount, gas used, and timestamp.
- **JSON Export**: Logs transaction data into a JSON file for easy access and analysis.

## Prerequisites

- [Node.js](https://nodejs.org/) (v14 or higher)
- [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)
- [Hardhat](https://hardhat.org/)
- [Infura](https://infura.io/) project ID
- Private key from a wallet with some testnet ETH

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/pancakeswap-hook.git
   cd pancakeswap-hook
   ```

2. **Install dependencies**:

   ```bash
   npm install
   ```

3. **Set up environment variables**:

   Create a `.env` file in the root directory with the following content:

   ```plaintext
   INFURA_PROJECT_ID=your_infura_project_id
   PRIVATE_KEY=your_private_key
   ```

## Configuration

Update `hardhat.config.js` with your network configuration:

```javascript
require("@nomiclabs/hardhat-waffle");
require("dotenv").config();

module.exports = {
  solidity: "0.8.24",
  networks: {
    sepolia: {
      url: `https://sepolia.infura.io/v3/${process.env.INFURA_PROJECT_ID}`,
      accounts: [`0x${process.env.PRIVATE_KEY}`],
    },
  },
};
```

## Smart Contract

The `PancakePoolData` contract logs token transactions for specified tokens:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

interface IPancakePair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function token0() external view returns (address);
    function token1() external view returns (address);
}

contract PancakePoolData {
    address public USDC = 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48;
    address public USDT = 0xdAC17F958D2ee523a2206206994597C13D831ec7;
    address public BTC = 0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599;
    address public ETH = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;
    address public CAKE = 0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82;
    address public UNI = 0x1f9837aB1F3C12239BCbdDeE0AEf2A03bD9A56b1;
    address public BNB = 0xB8c77482e45F1F44dE1745F52C74426C631bDD52;

    event TokenTransactionLogged(address indexed token, uint256 amount, uint256 timestamp);

    function logTokenTransaction(address token, uint256 amount) external {
        uint256 timestamp = block.timestamp;
        emit TokenTransactionLogged(token, amount, timestamp);
    }
}
```

## Deployment

1. **Deploy the Smart Contract**:

   ```bash
   npx hardhat run scripts/deploy.js --network sepolia
   ```

   This will deploy the `PancakePoolData` contract and output the deployed contract address.

## Interaction

1. **Log Token Transactions**:

   Update `scripts/logPoolData.js` with the deployed contract address:

   ```javascript
   const fs = require('fs');
   const path = require('path');
   const { ethers } = require('hardhat');

   async function main() {
     const [deployer] = await ethers.getSigners();
     const poolDataAddress = "0xYourDeployedContractAddress"; // Replace with your deployed contract address

     // Define the ABI directly within the script to avoid any potential ENS resolution
     const poolDataABI = [
       "function logTokenTransaction(address token, uint256 amount) external",
       "event TokenTransactionLogged(address indexed token, uint256 amount, uint256 timestamp)"
     ];

     // Directly create the contract instance using the ABI and address
     const poolData = new ethers.Contract(poolDataAddress, poolDataABI, deployer);

     const tokens = [
       { address: "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", name: "USDC" },
       { address: "0xdAC17F958D2ee523a2206206994597C13D831ec7", name: "USDT" },
       { address: "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599", name: "BTC" },
       { address: "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", name: "ETH" },
       { address: "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82", name: "CAKE" },
       { address: "0x1f9837aB1F3C12239BCbdDeE0AEf2A03bD9A56b1", name: "UNI" },
       { address: "0xB8c77482e45F1F44dE1745F52C74426C631bDD52", name: "BNB" },
     ];

     const logFilePath = path.join(__dirname, 'token_transactions_log.json');
     let logs = [];

     if (fs.existsSync(logFilePath)) {
       logs = JSON.parse(fs.readFileSync(logFilePath, 'utf8'));
     }

     for (let token of tokens) {
       const amount = Math.floor(Math.random() * 1000); // Simulate a random amount for the transaction
       const tx = await poolData.logTokenTransaction(token.address, amount);
       const receipt = await tx.wait();

       console.log(`${token.name} transaction logged`);

       const logEntry = {
         token: token.name,
         transactionHash: receipt.transactionHash,
         blockNumber: receipt.blockNumber,
         from: receipt.from,
         to: poolDataAddress,
         amount: amount.toString(),
         gasUsed: receipt.gasUsed.toString(),
         timestamp: new Date().toISOString(),
       };

       logs.push(logEntry);
     }

     fs.writeFileSync(logFilePath, JSON.stringify(logs, null, 2), 'utf8');
     console.log("Token transactions logged in token_transactions_log.json");
   }

   main()
     .then(() => process.exit(0))
     .catch((error) => {
       console.error(error);
       process.exit(1);
     });
   ```

2. **Run the Interaction Script**:

   ```bash
   npx hardhat run scripts/logPoolData.js --network sepolia
   ```

   This will log the token transactions and save the data to `token_transactions_log.json`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README provides a brief description of the project, emphasizing its key features and usage of PancakeSwap's smart contracts for data logging. 