from scipy import stats
from wrapper import Wrapper

"""
Usage:
A salesman makes 10 calls. Each call is an independent event.
The probability that he will close an individual sale is 0.3.

>>> b = BinomialWrapper(10, 0.3)

# What is the probability of closing 3 or more sales?
>>> b.greater_than_or_equal_to(3)

# What is the probability of closing exactly 4 sales?
>>> b.equal_to(4)
"""

class BinomialWrapper(Wrapper):
    def __init__(self, n, p):
        # n: number of independent events
        # p: probability of success
        super().__init__(stats.binom, args=[n, p])