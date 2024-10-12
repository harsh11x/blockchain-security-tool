import requests
import logging
import json
import os
from config import load_config

# Setup logging configuration
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def monitor_blockchain(blockchain, config_file):
    """Monitor the specified blockchain for transactions."""
    config = load_config(config_file)
    
    api_url = config.get('api_urls', {}).get(blockchain.lower())
    if not api_url:
        logging.error(f"No API URL configured for {blockchain}. Please check your config file.")
        print(f"No API URL configured for {blockchain}. Please check your config file.")
        return

    # Create a directory to store historical data
    if not os.path.exists('historical_data'):
        os.makedirs('historical_data')

    # Placeholder for actual API call
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            logging.info(f"Monitoring {blockchain}... Data: {data}")
            print(f"Monitoring {blockchain}... Data: {data}")

            # Save data to a JSON file
            with open(f'historical_data/{blockchain}_data.json', 'a') as f:
                f.write(json.dumps(data) + "\n")
                
            # Alerting system (for example, high unconfirmed transaction count)
            unconfirmed_count = data.get('unconfirmed_count', 0)
            if unconfirmed_count > 20000:  # Threshold example
                logging.warning(f"High unconfirmed transaction count: {unconfirmed_count}")
                print(f"Alert: High unconfirmed transaction count: {unconfirmed_count}")

        else:
            logging.error(f"Failed to fetch data for {blockchain}: {response.status_code}")
            print(f"Failed to fetch data for {blockchain}: {response.status_code}")
    except Exception as e:
        logging.error(f"An error occurred while monitoring {blockchain}: {str(e)}")
        print(f"An error occurred while monitoring {blockchain}: {str(e)}")