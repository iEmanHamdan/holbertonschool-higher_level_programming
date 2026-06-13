#!/usr/bin/python3


def safe_print_integer(value):
    """Prints an integer safely using try/except."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
