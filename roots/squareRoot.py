def squareRoot(v):
    guess = 1.
    EPSILON = 1e-10
    while abs(guess*guess - v) > EPSILON:
        newGuess = (guess + v / guess) / 2.
        guess = newGuess
    return guess

print squareRoot(2)
