import json
import yaml
import os


def parse(file_path):
    _, format_file_name = os.path.splitext(file_path)
    if format_file_name == '.json':
        return json.load(open(file_path))
    elif format_file_name == '.yaml' or '.yml':
        return yaml.safe_load(open(file_path))
    else:
        raise ValueError(f'{format_file_name} - wrong format')
