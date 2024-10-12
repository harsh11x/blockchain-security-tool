import requests
import yaml
import logging
import time
import sys

# Setup logging configuration
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Load configuration from YAML file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

def monitor_blockchain(blockchain_name):
    api_token = config['api_token']
    api_url = config['api_urls'][blockchain_name]
    
    print(f"Monitoring {blockchain_name}... Press Ctrl+C to stop.")
    
    while True:
        try:
            # Construct the full API URL with token
            response = requests.get(f"{api_url}?token={api_token}")

            if response.status_code == 200:
                data = response.json()
                logging.info(f"Monitoring {blockchain_name}... Data: {data}")
                
                # Alert logic based on data
                unconfirmed_count = data['unconfirmed_count']
                # Use '\r' to overwrite the current line in the terminal
                sys.stdout.write(f"\rCurrent Unconfirmed Transactions: {unconfirmed_count} ")
                sys.stdout.flush()  # Flush the output buffer

                if unconfirmed_count > 30000:  # Example threshold
                    print(f"\nAlert: High unconfirmed transaction count: {unconfirmed_count}")
            else:
                logging.error(f"Failed to fetch data: {response.status_code}")
                print(f"Failed to fetch data: {response.status_code}")
            
            # Wait before the next request
            time.sleep(3)  # Check every 10 seconds
            
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")
            break
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            print(f"An error occurred: {e}")
            time.sleep(2)  # Wait before retrying in case of error