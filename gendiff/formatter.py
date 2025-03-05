from gendiff.formatters.stylish import generate_diff_stylish


def to_format(formatter, diff):
    if formatter == 'stylish':
        return generate_diff_stylish(diff)
