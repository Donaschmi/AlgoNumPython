def cubicRoot(v):
    EPSILON = 1e-10
    guess = 1.
    while abs((guess * guess * guess) - v) > EPSILON:
        newGuess = ((2 * guess) + (v / (guess * guess))) / 3.
        guess = newGuess
    return guess

print cubicRoot(27)
