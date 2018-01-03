import math as math
import numpy as np

EPSILON = 2.22e-10
MAX_ITE = 0
def Jacobi(matrix, vector, guess):
    global MAX_ITE
    guessIte = guess.copy()
    while not difference(matrix, vector, guess) and not MAX_ITE == 100:
        for i in range(matrix.shape[0]):
            sumJ = 0.
            for j in range(matrix.shape[0]):
                if not i == j:
                    sumJ += matrix[i][j] * guess[j]
            guessIte[i] = (vector[i] - sumJ) / matrix[i][i]
        MAX_ITE+=1
        guess = guessIte.copy()

    return guessIte, MAX_ITE


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

    print Jacobi(tab, vec, guess)

if __name__ == '__main__':
    main()
