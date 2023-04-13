#!/usr/bin/python3

"""
Module that defines a function that returns a list of
lists of integers representing the Pascal's triangle for a
given number of rows.
"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers representing
    Pascal's triangle for a given number of rows.
    Parameters:
    n (int): The number of rows in Pascal's triangle to be returned.
    Returns:
    list: A list of lists of integers representing
    Pascal's triangle for the n number of rows.
          Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
