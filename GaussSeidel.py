import math as math
import numpy as np

EPSILON = 2.22e-16
MAX_ITE = 0

def GaussSeidel(matrix, vector, guess):
    global MAX_ITE
    while not difference(matrix, vector, guess) and not MAX_ITE == 20:
        for i in range(matrix.shape[0]):
            sum1 = 0.
            for j in range(0, i):
                sum1 += matrix[i][j] * guess[j]
            sum2 = 0.
            for j in range(i+1, matrix.shape[0]):
                sum2 += matrix[i][j] * guess[j]
            guess[i] = (vector[i] - sum1 - sum2) / matrix[i][i]
        MAX_ITE+=1
    return guess, MAX_ITE


def difference(matrix, vector, guess):
    global EPSILON
    mult = np.dot(matrix, guess)
    delta = np.absolute(mult - vector)
    boolean = True
    for i in range(delta.shape[0]):
        if delta[i] > EPSILON:
            boolean = False
    return boolean

def main():
    tab = np.array([[10., -1., 2., .0], [-1., 11., -1., 3.], [2., -1., 10., -1.], [0., 3., -1., 8.]])
    vec = np.array([6., 25., -11., 15.])
    #tab = np.array([[1., 1., -2.], [0., 1., -1.], [3., -1., 1.]])
    #vec = np.array([-3., -1., 4.])
    guess = np.array([0., 0., 0., 0.])
    result = GaussSeidel(tab, vec, guess)
    print result[0], result[1]

if __name__ == '__main__':
    main()
