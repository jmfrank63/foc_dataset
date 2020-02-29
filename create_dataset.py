#!/usr/bin/env python3
# Read in a file and place it into a dictionary

from typing import Tuple
import argparse

FILE = 'TEXTC.txt'


def read_to_dict(file_name: str = FILE) -> dict:
    """ Read the text file into a dictionary"""
    with open(file_name, 'r') as tfile:
        text_dict = {
            num: tuple(line.strip('\n').split(' ')[1:])
            for num, line in enumerate(tfile)
        }
    return text_dict


def encode_letter(letter: str) -> int:
    """ Return the number code for a letter starting with A = 1"""
    return ord(letter.upper()) - 64


def encode_name(name: str) -> int:
    """ Encode a name to numbers and sum up the numbers """
    return sum([encode_letter(letter) for letter in name])


def get_position_and_line_number(encode_number: int) -> Tuple[int, int]:
    """ Calculate the line number for the encoded number """
    line: int = encode_number % 100 + 1
    pos: int = encode_number // 100
    if pos == 1:
        pos = 4
    elif pos >= 2:
        pos = 9
    return pos, line


def make_data_set(pos: int, line: int, text_dict: dict, num: int = 15) -> list:
    """ Create a unique data set with four letter words from 
    the given dictionary of words"""
    word_list: list = []
    i = pos
    while (True):
        if len(word_list) >= num:
            break
        try:
            word = text_dict[line][i].lower()
        except IndexError:
            line += 1
            i = 0
            continue
        word = ''.join(filter(str.isalpha, word))
        if len(word) >= 4 and word not in word_list:
            word_list.append(word[:4])
        i += 1
    return word_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help="Name for your dataset")
    args = parser.parse_args()

    td = read_to_dict()
    enum = encode_name(args.name)
    pos, line = get_position_and_line_number(enum)
    print(make_data_set(pos, line, td, 15))


if __name__ == '__main__':
    main()
