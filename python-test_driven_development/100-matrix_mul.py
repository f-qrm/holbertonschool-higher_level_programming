#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list)for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list)for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for ii in row:
            if not isinstance(ii, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    row_length_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_length_a:
            raise TypeError("each row of m_a must be of the same size")
    row_length_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_length_b:
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    nombre_lignes = len(m_a)
    nombre_colonnes = len(m_b[0])
    new_matrix = [[0 for _ in range(nombre_colonnes)]for _ in range(nombre_lignes)]
    for i in range(nombre_lignes):
        for j in range(nombre_colonnes):
            for k in range(len(m_b)):
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]
    return new_matrix
