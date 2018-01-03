import math as math
x = 0.7

def richardson(f, h):
    global x
    top = 8. * f(x + h) + f(x - 2 * h) - f(x + 2 * h) - 8 * f(x - h)
    return top / (12 * h)

def cosinus(x):
    return math.cos(x)

def main():
    h = 1.
    for i in range (10):

        print (h,richardson(cosinus, h))
        h/=10.0

if __name__ == '__main__':
    main()
