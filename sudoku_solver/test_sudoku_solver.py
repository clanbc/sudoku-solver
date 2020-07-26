import pytest
from sudoku_solver.sudoku_solver import validate_input


def test_validate_input_good():
    good_puzzle = [
            '1| |3| | | | | | \n',
            ' | | |2| |4| | | \n',
            ' | | | | | | | | \n',
            '-----|-----|-----\n',
            ' | | | | | | | | \n',
            ' | | | | | | | | \n',
            ' | | | | | | | | \n',
            '-----|-----|-----\n',
            ' | | | | | | | | \n',
            ' | | | | | | | | \n',
            ' | | | | | | | | \n',
            ]
    assert validate_input(good_puzzle)


def test_validate_input_bad():
    bad_puzzle = [
            '1|1| | | | | | | \n',
            ' | | | | | | | | \n',
            ' | | | | | | | | \n',
            '-----|-----|-----\n',
            ' | | | | | | | | \n',
            ' | | | | | | | | \n',
            ' | | | | | | | | \n',
            '-----|-----|-----\n',
            ' | | | | | | | | \n',
            ' | | | | | | | | \n',
            ' | | | | | | | | \n'
            ]

    with pytest.raises(ValueError):
        validate_input(bad_puzzle)
