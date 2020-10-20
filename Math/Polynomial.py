# ======================================================================================================================
#        File:  Math/Polynomial.py
#     Project:  AlphaBrew
# Description:  Provides a generic implementation of a polynomial function to be used in polynomial regression maths.
#      Author:  Jared Julien <jaredjulien@exsystems.net>
#   Copyright:  (c) 2020 Jared Julien, eX Systems
# ---------------------------------------------------------------------------------------------------------------------
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================
# Polynomial Class
# ----------------------------------------------------------------------------------------------------------------------
class Polynomial:
    def __init__(self, *coefficients):
        self.coefficients = list(coefficients)



# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def order(self):
        return len(self) - 1



# ======================================================================================================================
# Overridden Methods
# ----------------------------------------------------------------------------------------------------------------------
    def __len__(self):
        return len(self.coefficients)


# ----------------------------------------------------------------------------------------------------------------------
    def __getitem__(self, index: int):
        return self.coefficients[index]


# ----------------------------------------------------------------------------------------------------------------------
    def __setitem__(self, index: int, value: float):
        self.coefficients[index] = value



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def append(self, coefficient):
        """Add a new coefficient to the list."""
        self.coefficients.append(coefficient)


# ----------------------------------------------------------------------------------------------------------------------
    def copy(self):
        """Create a new copy of this Polynomial with a copy of the coefficients, making it safe to alter them."""
        return Polynomial(*list(self.coefficients))


# ----------------------------------------------------------------------------------------------------------------------
    def eval(self, point):
        output = 0

        for index, coefficient in enumerate(self.coefficients):
            if index == 0:
                output += coefficient
            else:
                output += coefficient * (point ** index)

        return output


# ----------------------------------------------------------------------------------------------------------------------
    def root(self, guessA, guessB, precision=0.0000001):
        nextGuess = guessA
        maxSeparation = abs(guessA - guessB) * 1000
        while abs(guessA - guessB) > precision:
            nextGuess = guessB - ((guessB - guessA) * self.eval(guessB) / (self.eval(guessB) - self.eval(guessA)))
            guessA = guessB
            guessB = nextGuess
            if abs(guessA - guessB) > maxSeparation:
                raise ValueError('Failed to find root of polynomial')
        return nextGuess




# End of File
