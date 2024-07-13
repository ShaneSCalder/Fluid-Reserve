
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

This README should help you get started with using the Uniswap hook to pull pool data and log it using Hardhat. You can customize and extend it as per your project's requirements. If you need further assistance, feel free to ask!