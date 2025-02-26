#!/usr/bin/env python3


import argparse
from gendiff.generate_diff import parse, generate_diff, generate_list


#def cli_parser():
parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()

#    return args.first_file, args.second_file, args.format


def main():
    file1 = parse(args.first_file)
    file2 = parse(args.second_file)
    file3 = generate_diff(file1, file2)
    print(generate_list(file3))


if __name__ == '__main__':
    main()
