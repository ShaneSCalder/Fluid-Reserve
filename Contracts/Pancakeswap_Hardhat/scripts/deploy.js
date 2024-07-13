async function main() {
    const [deployer] = await ethers.getSigners();
    console.log("Deploying contracts with the account:", deployer.address);
  
    const PancakePoolData = await ethers.getContractFactory("PancakePoolData");
    const poolData = await PancakePoolData.deploy();
  
    console.log("PancakePoolData deployed to:", poolData.address);
  }
  
  main()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error(error);
      process.exit(1);
    });