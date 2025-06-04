#!/usr/bin/python3
def pascal_triangle(n):
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
