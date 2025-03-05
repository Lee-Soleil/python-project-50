START_INDENT = 4


def formatting_value(value, spaces_count, indent=' '):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        result = ["{"]
        for key, val in value.items():
            if isinstance(val, dict):
                new_value = formatting_value(val, spaces_count + START_INDENT)
                result.append(f"{indent * spaces_count}    {key}: {new_value}")
            else:
                result.append(f"{indent * spaces_count}    {key}: {val}")
        result.append(f'{indent * spaces_count}}}')
        return '\n'.join(result)
    return value


def generate_diff_stylish(diff, spaces_count=0):
    indent = ' ' * spaces_count
    lines = ['{']
    for key, value in diff.items():
        if value['operation'] == 'removed':
            lines.append(f"{indent}  - {key}: {formatting_value(value['old'], spaces_count + START_INDENT)}")
        elif value['operation'] == 'unchanged':
            lines.append(f"{indent}    {key}: {formatting_value(value['old'], spaces_count + START_INDENT)}")
        elif value['operation'] == 'changed':
            lines.append(f"{indent}  - {key}: {formatting_value(value['old'], spaces_count + START_INDENT)}")
            lines.append(f"{indent}  + {key}: {formatting_value(value['new'], spaces_count + START_INDENT)}")
        elif value['operation'] == 'added':
            lines.append(f"{indent}  + {key}: {formatting_value(value['new'], spaces_count + START_INDENT)}")
        elif value['operation'] == 'nested':
            lines.append(f"{indent}    {key}: {generate_diff_stylish(value['children'], spaces_count + START_INDENT)}")
    lines.append(f'{indent}}}')
    return "\n".join(lines)
