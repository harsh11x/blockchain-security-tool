import requests
import yaml
import logging

# Setup logging configuration
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Load configuration from config.yaml
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

api_url = config['api_urls']['bitcoin']
api_token = config['api_token']

def monitor_blockchain():
    response = requests.get(f"{api_url}?token={api_token}")
    if response.status_code == 200:
        data = response.json()
        logging.info(f"Monitoring bitcoin... Data: {data}")
        print(f"Monitoring bitcoin... Data: {data}")
    else:
        logging.error(f"Error fetching data: {response.status_code} - {response.text}")

if __name__ == "__main__":
    monitor_blockchain()
