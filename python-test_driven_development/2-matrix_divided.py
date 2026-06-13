#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The module provides one function, matrix_divided(matrix, div), which handles
scalar division across a 2D grid matrix structure.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimal places.

    Args:
        matrix: A list of lists containing integers or floats.
        div: A number (integer or float) to divide the elements by.

    Returns:
        A completely new matrix containing the division results.

    Raises:
        TypeError: If matrix is malformed, contains non-numbers, or if rows
                   vary in size. Also raised if div is not a valid number.
        ZeroDivisionError: If div equals zero.
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Core structural validation for matrices
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_msg)

    # Validate that every element is a list and not empty
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_msg)

    # Establish reference size using the first inner row
    row_size = len(matrix[0])

    # Thorough value and type verification loop
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, (int, float)) or num != num:
                raise TypeError(err_msg)

    # Validate divisor structural types and boundaries
    if not isinstance(div, (int, float)) or div != div:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return structured multi-dimensional division matrix
    return [[round(num / div, 2) for num in row] for row in matrix]
