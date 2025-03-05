from gendiff.parse import parse
from gendiff.generate_diff_tree import generate_diff_tree
from gendiff.formatter import to_format


def generate_diff(file_path1, file_path2, formatter='stylish'):
    file1 = parse(file_path1)
    file2 = parse(file_path2)
    diff = generate_diff_tree(file1, file2)
    result = to_format(formatter, diff)
    return result
