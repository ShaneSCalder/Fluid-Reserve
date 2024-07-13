# output data

## transaction for test net for hackathon

- npx hardhat run scripts/deploy.js --network sepolia
- Private Key Length: 64
- Private Key Length: 64
- Deploying contracts with the account: 0xF023E5ddddD79c247240372fd2A8D0600dE7433d
- MultiPoolTransactionLogger deployed to: 0xd78a245C2F902a95b8CfE83FB13983b2829818dA

## Transaction Log should be exported when interact.js is used 

example data if on main net. 

``` 
[
  {
    "transactionHash": "0xd41b0752292eefe01735f49b3234c679dba944618581bdb74704dd177d1137e7",
    "blockNumber": 8429868,
    "from": "0x8d15420FF8313Ed53A486Af0AA0485Af648b68e8",
    "to": "0x6b6881AfD87Fd97dd06C7442C2e38452c539eE14",
    "gasUsed": "69328",
    "timestamp": "2024-07-07T05:34:48.879Z"
  },
  {
    "transactionHash": "0x2bbf365b3d2ae5802ac1030ec5664a88e3e26077cc943a234551056a8ccee854",
    "blockNumber": 9526836,
    "from": "0xC1517a2643B2670557f8e56A94c72B421DB7401c",
    "to": "0x6FD30eE552A405291c9325E1c95299EE91534333",
    "gasUsed": "31887",
    "timestamp": "2024-07-09T11:35:20.712Z"
  }
  ]
   ```