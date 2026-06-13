#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list and returns a list of booleans."""
    result_list = []
    for num in my_list:
        if num % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list
