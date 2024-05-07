import json
import itertools


def stringify(value, replacer=' ', spaces_count=2):

  def iter_(current_value, depth):
    deep_indent_size = depth + spaces_count
    deep_indent = replacer * deep_indent_size
    current_indent = replacer * depth
    lines = []
    for key in current_value:
      if current_value[key]['operation'] == 'removed':
        lines.append(f'{deep_indent}- {key}: {current_value[key]["old"]}')
      elif current_value[key]['operation'] == 'added':
        lines.append(f'{deep_indent}+ {key}: {current_value[key]["new"]}')
      elif current_value[key]['operation'] == 'changed':
        lines.append(f'{deep_indent}- {key}: {current_value[key]["old"]}')
        lines.append(f'{deep_indent}+ {key}: {current_value[key]["new"]}')
      else:
        lines.append(f'{deep_indent}  {key}: {current_value[key]["old"]}')
    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


  return iter_(value, 0)


def generate_diff(file_path1, file_path2):
  file1 = json.load(open(file_path1))
  file2 = json.load(open(file_path2))
  all_keys = sorted(list((set(file1)) | set(file2)))
  diff = {}
  for key in all_keys:
    if key not in file1:
      diff[key] = {'operation': 'added', 'new': file2[key]}
    elif key not in file2:
      diff[key] = {'operation': 'removed', 'old': file1[key]}
    elif file1[key] != file2[key]:
      diff[key] = {
          'operation': 'changed',
          'old': file1[key],
          'new': file2[key]
      }
    else:
      diff[key] = {'operation': 'unchanged', 'old': file1[key]}
  return stringify(diff)
