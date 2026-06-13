#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The module provides one function, add_integer(a, b), which adds two numbers
together after checking their types and casting floats to integers.
"""


def add_integer(a, b=98):
    """Adds 2 integers or floats after casting them to integers.

    Args:
        a: The first number (integer or float).
        b: The second number (integer or float, defaults to 98).

    Returns:
        The integer addition result of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
