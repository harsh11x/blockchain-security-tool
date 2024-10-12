import yaml

def load_config(config_file):
    """Load configuration settings from a YAML file."""
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config