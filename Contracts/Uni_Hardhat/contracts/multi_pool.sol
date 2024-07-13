// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

interface IUniswapV4Hook {
    function preSwapHook(address user, uint256 amountIn, address pool) external returns (uint256);
    function postSwapHook(address user, uint256 amountIn, uint256 amountOut, address pool) external;
}

contract MultiPoolTransactionLogger is IUniswapV4Hook {
    address public USDC = 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48;
    address public USDT = 0xdAC17F958D2ee523a2206206994597C13D831ec7;
    address public BTC = 0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599;
    address public ETH = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;
    address public CAKE = 0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82;
    address public UNI = 0x1f9837aB1F3C12239BCbdDeE0AEf2A03bD9A56b1;
    address public BNB = 0xB8c77482e45F1F44dE1745F52C74426C631bDD52;

    event SwapLogged(
        address indexed user,
        address indexed pool,
        uint256 amountIn,
        uint256 amountOut,
        uint256 timestamp
    );

    function preSwapHook(address user, uint256 amountIn, address pool) external override returns (uint256) {
        return amountIn;
    }

    function postSwapHook(address user, uint256 amountIn, uint256 amountOut, address pool) external override {
        uint256 timestamp = block.timestamp;
        emit SwapLogged(user, pool, amountIn, amountOut, timestamp);
    }
}