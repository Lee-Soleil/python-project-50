import json

def parse(file_path):
    return json.load(open(file_path))


def generate_diff(file1, file2):
    all_keys = sorted(list((set(file1)) | set(file2)))
    diff = {}
    for key in all_keys:
        if key not in file1:
            diff[key] = {
                'operation': 'added',
                'new': file2[key]
            }
        elif key not in file2:
            diff[key] = {
                'operation': 'removed',
                'old': file1[key]
            }
        elif isinstance(file1[key], dict) and \
                isinstance(file2[key], dict):
            diff[key] = {
                'operation': 'nested',
                'children': generate_diff(file1[key], file2[key])
            }
        elif file1[key] != file2[key]:
            diff[key] = {
                'operation': 'changed',
                'old': file1[key],
                'new': file2[key]
            }
        else:
            diff[key] = {
                'operation': 'unchanged',
                'old': file1[key]
            }
    return diff

def if_dict(key):
    return isinstance(key, dict)
    

def get_info(directory):
    return directory.get('information', [])


def formatter_bool(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_list(diff):
    lines = ['{']
    for key, value in diff.items():
        if if_dict(value):
            information = value
            if value['operation'] == 'removed':
                lines.append(f"  - {key}: {formatter_bool(value['old'])}")
            elif value['operation'] == 'unchanged':
                lines.append(f"    {key}: {formatter_bool(value['old'])}")
            elif value['operation'] == 'changed':
                lines.append(f"  - {key}: {formatter_bool(value['old'])}")
                lines.append(f"  + {key}: {formatter_bool(value['new'])}")
            elif value['operation'] == 'added':
                lines.append(f"  + {key}: {formatter_bool(value['new'])}")
    lines.append('}')
    return lines
    

def gen_diff(diff):
    lst = generate_list(diff)
    for l in lst:
        print(l)
