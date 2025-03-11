def formatting_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return value
    

def format_to_plain(diff, path=''):
    result = []
    for key, val in diff.items():
        current_path = f"{path}.{key}" if path else key
        if val['operation'] == 'added':
            result.append(f"Property '{current_path}' was added "
                          f"with value: {formatting_value(val['new'])}")
        elif val['operation'] == 'removed':
            result.append(f"Property '{current_path}' was removed")
        elif val['operation'] == 'changed':
            result.append(f"Property '{current_path}' was updated. "
                          f"From {formatting_value(val['old'])} "
                          f"to {formatting_value(val['new'])}")
        elif val['operation'] == 'nested':
            new_val = format_to_plain(val['children'], current_path)
            result.append(new_val)
    return "\n".join(result)
