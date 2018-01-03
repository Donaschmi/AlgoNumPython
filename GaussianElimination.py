import math as math

def GaussianElminiation(matrix, vector):
    """
    FS
    """
    for i in range(0, len(matrix)):
        index = findPivot(matrix, i)
        if index == 1000:
            # Swap columns
            matrix[i], matrix[index] = matrix[index], matrix[i]
            vector[i], vector[index] = vector[index], vector[i]
        value = matrix[i][i]

        for j in range(i, len(matrix)):
            matrix[i][j] = matrix[i][j] / value
        vector[i] = vector[i] / value

        for j in range(i+1, len(matrix)):
            val = matrix[j][i]
            for k in range(i, len(matrix)):

                matrix[j][k] = matrix[j][k] - val * matrix[i][k]
            print vector[i] * val
            vector[j] = vector[j] - vector[i] * val

        print matrix
        print vector

    """
    BS
    """
    for i in range(len(matrix)-1, -1, -1):
        valV = vector[i]
        for j in range(i-1, -1, -1):
            vector[j] = vector[j] - matrix[j][i] * valV
            matrix[j][i] = 0
    print vector
    print matrix







def findPivot(matrix, col):
    """
    OK
    """
    pivot = 0
    index = col
    for i in range(col, len(matrix)):
        if math.fabs(matrix[i][col])> pivot:
            index = i
            pivot = math.fabs(matrix[i][col])
    return index


def main():
    tab = [[10., -1., 2., .0], [-1., 11., -1., 3.], [2., -1., 10., -1.], [0., 3., -1., 8.]]
    vec = [6., 25., -11., 15.]
    #tab = [[1., 1., -2.], [0., 1., -1.], [3., -1., 1.]]
    #vec = [-3., -1., 4.]
    print tab

    GaussianElminiation(tab, vec)

if __name__ == '__main__':
    main()
