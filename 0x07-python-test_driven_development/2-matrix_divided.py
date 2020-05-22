#!/usr/bin/python3

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

    Returns:
        [type] -- [description]
    """
    new = []
    len_row = 0
    if matrix and type(matrix) == list:
        len_row = len(matrix[0])
        if type(div) not in (int, float):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        for row in matrix:
            if type(row) != list:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if len(row) == len_row:
                len_row = len(row)
                for i in row:
                    if type(i) not in (int, float):
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                raise TypeError("Each row of the matrix must have the same size")

        new = [[round(num/div, 2) for num in r] for r in matrix]
        return new

    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
