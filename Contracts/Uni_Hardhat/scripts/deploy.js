// scripts/deploy.js
async function main() {
    const [deployer] = await ethers.getSigners();
    console.log("Deploying contracts with the account:", deployer.address);

    const MultiPoolTransactionLogger = await ethers.getContractFactory("MultiPoolTransactionLogger");
    const logger = await MultiPoolTransactionLogger.deploy();

    console.log("MultiPoolTransactionLogger deployed to:", logger.address);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
