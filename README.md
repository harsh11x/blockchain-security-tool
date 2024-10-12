
<img width="926" alt="Screenshot 2024-10-13 at 2 52 28 AM" src="https://github.com/user-attachments/assets/e75650b4-4ced-4243-ac0d-d9732f5d0561">


# ChainEYE

## Overview

The **ChainEYE** is an easy-to-use command-line application that helps businesses monitor and analyze their blockchain networks. It provides real-time insights into blockchain activity, ensuring security and compliance.

## Purpose

This tool is designed to:

- **Monitor Blockchain Activity**: Keep track of transactions and blocks happening in the blockchain.
- **Detect Security Issues**: Identify any suspicious activities that could indicate a security problem.
- **Store Historical Data**: Save information about blockchain activity over time, making it easier to see trends and patterns.
- **Generate Reports**: Create summaries of blockchain activity to help with decision-making and regulatory compliance.

## Features

- **Real-Time Monitoring**: Get live updates on the status of the blockchain you’re monitoring.
- **Audit Transactions**: Check that all transactions are legitimate and secure.
- **Save Historical Data**: Store monitoring data in JSON files for future analysis.
- **Create Alerts**: Set up notifications for important events, like high transaction counts.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/blockchain-security-tool.git
   cd blockchain-security-tool

2. **Install Required Packages**:
Make sure you have Python and pip installed. Then, install the necessary libraries:

       pip install requests pyyaml


3. **Configuration**:
Create a config.yaml file in the root directory and add the API URLs for the blockchains you want to monitor. Here’s an example:

       api_urls:
       bitcoin: https://api.blockcypher.com/v1/btc/main

## Usage

### Monitor Blockchain

To monitor a blockchain, run the following command:

    python3 cli.py monitor <blockchain_name> [--config <config_file>]



Example:

    python3 cli.py monitor bitcoin




Generate Reports

To create a report from the historical data collected, use:

    python3 cli.py report <blockchain_name>


Example: 

    python3 cli.py report bitcoin


### Logging

 All monitoring activities and alerts are logged into an app.log file in the root directory. You can check this log file for detailed information about the monitoring process.

### Future Enhancements

#### Future improvements for this tool may include:

 •	Building a web dashboard for real-time visualizations of blockchain metrics.

 •	Integrating advanced analytics and machine learning for better insights.	

 •	Supporting more blockchain networks and customizable options.



## Acknowledgements

•	(BlockCypher API)[https://www.blockcypher.com] for providing blockchain data.

•	Python for its powerful scripting capabilities.
