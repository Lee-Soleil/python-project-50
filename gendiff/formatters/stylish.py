START_INDENT = 4


def formatting_value(value, depth, indent=' '):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        result = ["{"]
        for key, val in value.items():
            if isinstance(val, dict):
                new_value = formatting_value(val, depth + START_INDENT)
                result.append(f"{indent * depth}    {key}: {new_value}")
            else:
                result.append(f"{indent * depth}    {key}: {val}")
        result.append(f'{indent * depth}}}')
        return '\n'.join(result)
    return value


def format_to_stylish(diff, depth=0):
    indent = ' ' * depth
    lines = ['{']
    for key, value in diff.items():
        if value['operation'] == 'removed':
            lines.append(
                f"{indent}  - {key}: "
                f"{formatting_value(value['old'], depth + START_INDENT)}")
        elif value['operation'] == 'unchanged':
            lines.append(
                f"{indent}    {key}: "
                f"{formatting_value(value['old'], depth + START_INDENT)}")
        elif value['operation'] == 'changed':
            lines.append(
                f"{indent}  - {key}: "
                f"{formatting_value(value['old'], depth + START_INDENT)}")
            lines.append(
                f"{indent}  + {key}: "
                f"{formatting_value(value['new'], depth + START_INDENT)}")
        elif value['operation'] == 'added':
            lines.append(
                f"{indent}  + {key}: "
                f"{formatting_value(value['new'], depth + START_INDENT)}")
        elif value['operation'] == 'nested':
            lines.append(
                f"{indent}    {key}: "
                f"{format_to_stylish(value['children'], depth + START_INDENT)}")
    lines.append(f'{indent}}}')
    return "\n".join(lines)
