import math as math
import numpy as np


def Cholesky(matrix):
    length = matrix.shape[0]
    result = np.zeros((length, length))
    for i in range(length):
        for j in range(length):
            print result
            if i == j:
                sumK = 0.
                for k in range(i):
                    sumK += result[i][k] * result[i][k]
                result[i][j] = math.sqrt(matrix[i][i] - sumK)
            elif i > j:
                sumK = 0.
                for k in range(j):
                    sumK += result[i][k] * result[j][k]
                result[i][j] = (matrix[i][j] - sumK) / result[j][j]
            else:
                result[i][j] = 0
    return result

def main():
    tab = np.array([[25., 15., -5.], [15., 18., 0.], [-5., 0., 11.]])
    result = Cholesky(tab)
    print result

if __name__ == '__main__':
    main()
