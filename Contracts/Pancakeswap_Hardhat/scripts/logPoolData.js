const fs = require('fs');
const path = require('path');
const { ethers } = require('hardhat');

async function main() {
  const [deployer] = await ethers.getSigners();
  const poolDataAddress = "0x5e63F2a20ba11793Ea53c810C7701175Cfd0dFA6"; // Deployed contract address

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