#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for it in row:
                if it != row[-1]:
                    print("{:d}".format(it), end=" ")
                else:
                    print("{:d}".format(it), end="")
            print()
