import json
import os
import logging
from monitor import monitor_blockchain
from auditor import generate_audit_report

# Existing code...

def generate_report(blockchain):
    """Generate a report from historical data."""
    file_path = f'historical_data/{blockchain}_data.json'
    
    if not os.path.exists(file_path):
        print(f"No historical data found for {blockchain}.")
        return
    
    report_data = []
    with open(file_path, 'r') as f:
        for line in f:
            report_data.append(json.loads(line))

    # You can generate more sophisticated reports here
    report_file = f'historical_data/{blockchain}_report.json'
    with open(report_file, 'w') as f:
        json.dump(report_data, f, indent=4)

    logging.info(f"Report generated: {report_file}")
    print(f"Report generated: {report_file}")

# Update the CLI command to include the report generation option
if __name__ == "__main__":
    # CLI logic...
    import argparse

    parser = argparse.ArgumentParser(description='Blockchain Security and Auditing Tool')
    parser.add_argument('command', choices=['monitor', 'report'], help='Command to execute')
    parser.add_argument('blockchain_name', help='Name of the blockchain to monitor or generate report for')
    parser.add_argument('--config', default='config.yaml', help='Path to the configuration file')

    args = parser.parse_args()

    if args.command == 'monitor':
        monitor_blockchain(args.blockchain_name, args.config)
    elif args.command == 'report':
        generate_report(args.blockchain_name)