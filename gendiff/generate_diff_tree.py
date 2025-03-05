def generate_diff_tree(file1, file2):
    all_keys = sorted(list((set(file1)) | set(file2)))
    diff_tree = {}
    for key in all_keys:
        if key not in file1:
            diff_tree[key] = {
                'operation': 'added',
                'new': file2[key]
            }
        elif key not in file2:
            diff_tree[key] = {
                'operation': 'removed',
                'old': file1[key]
            }
        elif isinstance(file1[key], dict) and \
                isinstance(file2[key], dict):
            diff_tree[key] = {
                'operation': 'nested',
                'children': generate_diff_tree(file1[key], file2[key])
            }
        elif file1[key] != file2[key]:
            diff_tree[key] = {
                'operation': 'changed',
                'old': file1[key],
                'new': file2[key]
            }
        else:
            diff_tree[key] = {
                'operation': 'unchanged',
                'old': file1[key]
            }
    return diff_tree
