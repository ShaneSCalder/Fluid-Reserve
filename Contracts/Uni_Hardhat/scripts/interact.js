// scripts/interact.js
const fs = require('fs');
const path = require('path');

async function main() {
    const [deployer] = await ethers.getSigners();
    const loggerAddress = "0xd78a245C2F902a95b8CfE83FB13983b2829818dA"; // Replace with your deployed contract address

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




