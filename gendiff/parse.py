import json
import os

import yaml


def parse(file_path):
    _, extension = os.path.splitext(file_path)
    if extension == '.json':
        return json.load(open(file_path))
    elif extension == '.yaml' or '.yml':
        with open(file_path) as fh:
            return yaml.safe_load(fh)
    raise ValueError(f"{extension} - wrong format")
