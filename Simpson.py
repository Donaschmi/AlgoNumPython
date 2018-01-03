import math as math
points = 2
def simpson_rule(f, a, b):
    c = (a + b) / 2.0
    h = (b - a) / 6.0
    return h * (f(a) + 4 * f(c) + f(b))

def simpson(f, a, b, EPS, whole):
    c = (a + b) / 2.0
    global points
    points += 1
    left = simpson_rule(f, a, c)
    right = simpson_rule(f, c, b)
    if math.fabs((left+right) - whole) < EPS:
        return left + right
    return simpson(f, a, c, EPS, left) + simpson(f, c, b, EPS,right)

def myFunction(x):
    left = 1 / (math.pow(x - 0.3 ,2) + 0.01)
    right = 1 / (math.pow(x - 0.9 ,2) + 0.04)
    return left + right - 6

def main():
    EPSILON = 1e-10
    interval = [0, 1]
    global points
    print simpson(myFunction, interval[0], interval[1], EPSILON, simpson_rule(myFunction, interval[0], interval[1])), points


if __name__ == '__main__':
    main()
