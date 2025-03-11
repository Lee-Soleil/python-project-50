from gendiff.formatters.stylish import format_to_stylish
from gendiff.formatters.plain import format_to_plain
from gendiff.formatters.json import format_to_json


def to_format(formatter, diff):
    if formatter == 'stylish':
        return format_to_stylish(diff)
    if formatter == 'plain':
        return format_to_plain(diff)
    if formatter == 'json':
        return format_to_json(diff)
