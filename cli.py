import argparse
from monitor import monitor_blockchain
from auditor import audit_transactions
from detector import detect_anomalies

def main():
    parser = argparse.ArgumentParser(description='Advanced Blockchain Security and Auditing Tool')
    subparsers = parser.add_subparsers(dest='command')

    # Monitor command
    monitor_parser = subparsers.add_parser('monitor', help='Monitor a blockchain')
    monitor_parser.add_argument('blockchain_name', type=str, help='Name of the blockchain to monitor')

    # Audit command
    audit_parser = subparsers.add_parser('audit', help='Audit transactions of a blockchain')
    audit_parser.add_argument('blockchain_name', type=str, help='Name of the blockchain to audit')

    # Detect command
    detect_parser = subparsers.add_parser('detect', help='Detect anomalies in blockchain data')
    detect_parser.add_argument('blockchain_name', type=str, help='Name of the blockchain to check')

    args = parser.parse_args()

    if args.command == 'monitor':
        monitor_blockchain(args.blockchain_name)
    elif args.command == 'audit':
        audit_transactions(args.blockchain_name)
    elif args.command == 'detect':
        detect_anomalies(args.blockchain_name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
