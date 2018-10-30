import unittest
import numpy as np


def zero_matrix_one(matrix):
    matrix = np.array(matrix)
    row_arr = [key for key, row in enumerate(matrix) if 0 in row]
    col_arr = [key for key, col in enumerate(matrix.T) if 0 in col]

    for key in row_arr:
        matrix[key, :] = 0

    for key in col_arr:
        matrix[:, key] = 0

    return matrix.tolist()


# From CtCI GitHub
def zero_matrix_two(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = []
    cols = []

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.append(x)
                cols.append(y)

    for row in rows:
        nullify_row(matrix, row)

    for col in cols:
        nullify_col(matrix, col)

    return matrix


def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
         ],
         [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
         ])
    ]

    def test_zero_matrix_one(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix_one(test_matrix)
            self.assertEqual(actual, expected)

    def test_zero_matrix_two(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix_two(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
