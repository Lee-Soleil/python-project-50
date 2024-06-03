import gendiff.parser
import itertools


def stringify(value, replacer=' ', spaces_count=2):
    def iter_(current_value, depth):
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key in current_value:
            if current_value[key]['operation'] == 'removed':
                lines.append(f'{deep_indent}- {key}: '
                             f'{current_value[key]["old"]}')
            elif current_value[key]['operation'] == 'added':
                lines.append(f'{deep_indent}+ {key}: '
                             f'{current_value[key]["new"]}')
            elif current_value[key]['operation'] == 'changed':
                lines.append(f'{deep_indent}- {key}: '
                             f'{current_value[key]["old"]}')
                lines.append(f'{deep_indent}+ {key}: '
                             f'{current_value[key]["new"]}')
            else:
                lines.append(f'{deep_indent}  {key}: '
                             f'{current_value[key]["old"]}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(value, 0)


def generate_diff(file_path1, file_path2):
    file1 = gendiff.parser.parse(file_path1)
    file2 = gendiff.parser.parse(file_path2)
#    file1 = yaml.safe_load(open(file_path1))
#    file2 = yaml.safe_load(open(file_path2))
#    file1 = json.load(open(file_path1))
#    file2 = json.load(open(file_path2))
    all_keys = sorted(list((set(file1)) | set(file2)))
    diff = {}
    for key in all_keys:
        if key not in file1:
            diff[key] = {'operation': 'added', 'new': str(file2[key]).lower()}
        elif key not in file2:
            diff[key] = {'operation': 'removed', 'old': str(file1[key]).lower()}
        elif file1[key] != file2[key]:
            diff[key] = {
                'operation': 'changed',
                'old': str(file1[key]).lower(),
                'new': str(file2[key]).lower()
            }
        else:
            diff[key] = {'operation': 'unchanged',
                         'old': str(file1[key]).lower()}
    return stringify(diff)
