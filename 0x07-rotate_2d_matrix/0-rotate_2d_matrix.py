#!/usr/bin/python3
"""
rotates a matrix to 90degrees
"""


def rotate_2d_matrix(matrix):
    """ rotates given matrix into 90 degrees clockwise"""
    row = len(matrix)
    column = row - 1
    for j in range (0, int(row / 2)):
        for i in range(j, column - j):
            mat = matrix[j][i]
            matrix[j][i] = matrix[column - i][j]
            matrix[column - i][j] = matrix[column -j][column - i]
            matrix[column -j][column - i] = matrix[i][column - j]
            matrix[i][column - j] = mat
