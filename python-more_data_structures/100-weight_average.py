#!/usr/bin/python3
"""
This module provides a function to calculate the weighted average
of an integer tuple list.
"""


def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuples (<score>, <weight>)."""
    if not my_list:
        return 0

    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    return total_score / total_weight
    