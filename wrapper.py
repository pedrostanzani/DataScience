class Wrapper:
    def __init__(self, module, args=[]):
        self.module = module
        self.args = args

    def equal_to(self, y):
        return self.module.pmf(y, *self.args)
    
    def less_than_or_equal_to(self, y):
        return self.module.cdf(y, *self.args)
    
    def greater_than(self, y):
        return self.module.sf(y, *self.args)
    
    def less_than(self, y):
        return self.module.cdf(y, *self.args) - self.module.pmf(y, *self.args)
    
    def greater_than_or_equal_to(self, y):
        return self.module.sf(y, *self.args) + self.module.pmf(y, *self.args)
