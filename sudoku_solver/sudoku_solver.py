#!/usr/bin/env python3

import argparse
import logging
import sys

format = '%(asctime)s - %(levelname)-2s - %(message)s'
logging.basicConfig(level=logging.INFO, format=format)

VERSION = "0.0.1"


def cli(ver):
    """
    All things command line args.

    :param ver: str, current version of app
    :return args: obj, argparse object of cli arguements
    """

    parser = argparse.ArgumentParser(description='Solve Sudoku Puzzles')
    parser.add_argument(
            '--puzzle',
            type=argparse.FileType('r'),
            metavar='[file.txt]',
            help='text file containing puzzle to solve'
            )
    parser.add_argument(
            '--version',
            action='version', version='%(prog)s {}'.format(ver)
            )
    parser.add_argument(
            '--generate',
            default='true',
            metavar='[true]',
            help='generate a blank puzzle')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    return args


def generate_blank():
    """
    Generate a blank sudoku game and stroe it within
    a text file.
    """

    blank_puzzle = ""
    f = open("blank-puzzle.txt", "w")
    for x in range(9):
        blank_puzzle += ' | | | | | | | | \n'
        if x == 2 or x == 5:
            blank_puzzle += '-----|-----|-----\n'

    logging.debug(blank_puzzle)
    f = open("blank-puzzle.txt", "w")
    f.write(blank_puzzle)
    f.close()


def in_row(poistion):
    """
    """

    return True


def in_coloumn(poistion):
    """
    """

    return True


def in_square(poistion):
    """
    """

    return True


def validate_input(puzzle):
    """
    Ensure puzzle provided meets the rules of
    the game.
    Rule 1: No duplicates in a row [done]
    Rule 2: No duplicates in a column
    Rule 3: No duplicates in a 3x3 square
    Rule 4: min 17 numbers to start with

    :param puzzle: list, puzzle provided to complete.
    """
    # min_num = 17
    row_number = 0
    for row in puzzle:
        if row == '-----|-----|-----\n':
            break
        logging.debug(row)

        row_number += 1
        remove_sep = row.replace('|', '')
        remove_whitespace = remove_sep.replace(' ', '')
        remaining_numbers = remove_whitespace
        logging.debug(remaining_numbers)
        try:
            count = {}
            for s in remaining_numbers:
                if s in count:
                    count[s] += 1
                else:
                    count[s] = 1

            for key in count:
                if count[key] > 1:
                    error_text = "found number {} {} times in row {}".format(key, count[key], row_number)  # noqa: E501
                    raise ValueError(error_text)
        except Exception as e:
            raise(e)
        else:
            return True


def main():
    """
    """

    args = cli(VERSION)
    if args.puzzle is not None:
        try:
            validate_input(args.puzzle.readlines())
        except Exception as e:
            logging.error(e)
            sys.exit(1)
        else:
            sys.exit(0)

    if args.generate is not None:
        if args.generate == 'true':
            generate_blank()
            logging.info('generated file')
            sys.exit(0)
        else:
            logging.error('incorrect value for --generate arg, correct value is: true')  # noqa: E501
            sys.exit(1)


if __name__ == "__main__":
    main()
