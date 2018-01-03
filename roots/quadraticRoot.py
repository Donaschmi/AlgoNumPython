def squareRoot(v):
    guess = 1.
    EPSILON = 1e-10
    while abs(guess*guess*guess*guess - v) > EPSILON:
        newGuess = (3 *guess + v / (guess*guess*guess)) / 4.
        guess = newGuess
    return guess

print squareRoot(81)
