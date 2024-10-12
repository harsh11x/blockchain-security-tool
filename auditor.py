import logging

# Setup logging configuration
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def generate_audit_report(output_format, config_file):
    """Generate and export an audit report in the specified format."""
    # Placeholder for audit logic
    audit_data = {
        "transactions": [
            {"id": 1, "amount": 100, "status": "confirmed"},
            {"id": 2, "amount": 50, "status": "pending"},
        ]
    }

    try:
        if output_format.lower() == 'json':
            import json
            with open('audit_report.json', 'w') as f:
                json.dump(audit_data, f)
            logging.info("Audit report generated: audit_report.json")
            print("Audit report generated: audit_report.json")

        elif output_format.lower() == 'csv':
            import csv
            with open('audit_report.csv', 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=audit_data['transactions'][0].keys())
                writer.writeheader()
                writer.writerows(audit_data['transactions'])
            logging.info("Audit report generated: audit_report.csv")
            print("Audit report generated: audit_report.csv")

        else:
            logging.warning("Unsupported format. Please choose 'json' or 'csv'.")
            print("Unsupported format. Please choose 'json' or 'csv'.")
    except Exception as e:
        logging.error(f"An error occurred while generating the audit report: {str(e)}")
        print(f"An error occurred while generating the audit report: {str(e)}")