from scipy import stats

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

class BinomialWrapper:
    def __init__(self, n, p):
        self.n = n  # number of independent events
        self.p = p  # probability of success
    
    def equal_to(self, y):
        return stats.binom.pmf(y, self.n, self.p)
    
    def less_than_or_equal_to(self, y):
        return stats.binom.cdf(y, self.n, self.p)
    
    def greater_than(self, y):
        return stats.binom.sf(y, self.n, self.p)
    
    def less_than(self, y):
        return stats.binom.cdf(y, self.n, self.p) - stats.binom.pmf(y, self.n, self.p)
    
    def greater_than_or_equal_to(self, y):
        return stats.binom.sf(y, self.n, self.p) + stats.binom.pmf(y, self.n, self.p)

class PoissonWrapper:
    def __init__(self, mu):
        self.mu = mu
    
    def equal_to(self, y):
        return stats.poisson.pmf(y, self.mu)
    
    def less_than_or_equal_to(self, y):
        return stats.poisson.cdf(y, self.mu)
    
    def greater_than(self, y):
        return stats.poisson.sf(y, self.mu)
    
    def less_than(self, y):
        return stats.poisson.cdf(y, self.mu) - stats.poisson.pmf(y, self.mu)
    
    def greater_than_or_equal_to(self, y):
        return stats.poisson.sf(y, self.mu) + stats.poisson.pmf(y, self.mu)
