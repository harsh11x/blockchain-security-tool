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

def detect_anomalies(blockchain_name):
    response = requests.get(f"{api_url}?token={api_token}")
    if response.status_code == 200:
        data = response.json()
        # Implement your anomaly detection logic here
        logging.info(f"Detecting anomalies in {blockchain_name}... Data: {data}")
        print(f"Detecting anomalies in {blockchain_name}... Data: {data}")
    else:
        logging.error(f"Error fetching data for anomaly detection: {response.status_code} - {response.text}")

if __name__ == "__main__":
    import sys
    detect_anomalies(sys.argv[1])
