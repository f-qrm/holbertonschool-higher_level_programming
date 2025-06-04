#!/usr/bin/python3
"""
pascal_triangle module

Provides a function to generate Pascal's triangle of a given size.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.

    Each row of Pascal's triangle contains the sum of the two numbers
    directly above it in the previous row, starting and ending with 1.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list of list of int: A list of lists, where each inner list
        represents a row of Pascal's triangle.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    new_list = [[1]]
    for i in range(1, n):
        prec_row = new_list[-1]
        row = [1]
        for j in range(1, len(prec_row)):
            row.append(prec_row[j - 1] + prec_row[j])
        row.append(1)
        new_list.append(row)

    return new_list
