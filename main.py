import sys
import re
import os

from time import time


def remove_comments(lines_list):
    # remove one line // comments
    for i, line in enumerate(lines_list):
        lines_list[i] = re.sub(r'(\/+\/+).*', '', line)

    string = "".join(lines_list)
    return string


def cut_whitespace_chars(list_of_chars, string):
    final_string = string

    for char in list_of_chars:
        pattern1 = re.compile(rf'[\s\t]+({char})')
        pattern2 = re.compile(rf'({char})[\s\t]+')

        final_char = char.replace('\\', '')

        final_string = re.sub(pattern1, final_char, final_string)
        final_string = re.sub(pattern2, final_char, final_string)

    return final_string


def minify(path):
    try:
        with open(path, mode='r') as file:
            lines_list = file.readlines()
            string_without_comments = remove_comments(lines_list)
            list_of_chars = list(string_without_comments)
            counter = list_of_chars.count('\n')

            for i in range(0, counter):
                list_of_chars.remove('\n')

            string = "".join(list_of_chars)

            list_of_chars = [r'\=', r'\(', r'\)', r'\{', r'\}', r'\,', r'\:', r'\+', r'\-', r'\*', r'\/',
                             r'\=\=', r'\=\=\=', r'\=\>', r'\<', r'\>', r'\<\=', r'\>\=', r'\+\+', r'\-\-',
                             r'\+\=', r'\-\=', r'\*\*', r'\*\=', r'\/\=', r'\%', r'\?', r'\;'
                             ]

            final_string = cut_whitespace_chars(list_of_chars, string)

            with open(f'./minified/{path}', mode='w') as minified_file:
                minified_file.write(final_string)
                print(f'File {path} minified successfully')

    except FileNotFoundError as error:
        print(f'I did not find file {path}')


def main():
    start = time()

    dir_path = './minified'
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    for i in range(1, len(sys.argv)):
        minify(sys.argv[i])

    stop = time()
    print(f'Took {round(stop - start, 4)}ms')


if __name__ == '__main__' and len(sys.argv) > 1:
    main()
