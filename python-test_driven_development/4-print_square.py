#!/usr/bin/python3
"""
This is the "4-print_square" module.
The module provides one function, print_square(size), which outputs a visual
square using the hash symbol '#' safely after size validation checks.
"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size: An integer representing the size length of the square.

    Raises:
        TypeError: If size is not an integer, or is a float.
        ValueError: If size is less than 0.
    """
    if isinstance(size, float):
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
