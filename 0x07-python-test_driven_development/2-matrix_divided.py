#!/usr/bin/python3
"""Matrix_divide"""


def matrix_divided(matrix, div):
    """[summary]

    Arguments:
        matrix {[type]} -- [description]
        div {[type]} -- [description]

    Raises:
        TypeError: [description]
        ZeroDivisionError: [description]
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]

    Returns:
        [type] -- [description]
    """
    new = []
    len_row = 0
    must_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    row_size = "Each row of the matrix must have the same size"
    if matrix and type(matrix) == list:
        len_row = len(matrix[0])
        if type(div) not in (int, float):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        for row in matrix:
            if type(row) != list:
                raise TypeError(must_matrix)
            if len(row) == len_row:
                len_row = len(row)
                if len_row == 0:
                    raise TypeError(must_matrix)
                for i in row:
                    if type(i) not in (int, float):
                        raise TypeError(must_matrix)
            else:
                raise TypeError(row_size)

        new = [[round(num/div, 2) for num in r] for r in matrix]
        return new

    raise TypeError(must_matrix)
