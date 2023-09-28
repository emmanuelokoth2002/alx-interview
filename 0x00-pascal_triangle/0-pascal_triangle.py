#!/usr/bin/python3
"""
Returns list of integers representing pascal triangle
"""


def pascal_triangle(n):
    """
    function that returns a list of lists of integers representing the
    Pascal’s triangle

    Returns an empty list if n <= 0
    You can assume n will be always an integer
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
