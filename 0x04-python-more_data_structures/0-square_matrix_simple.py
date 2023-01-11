#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # a function that computes the square value of all integers of a matrix.
    return ([list(map(lambda x: x * x, loop)) for loop in matrix])
