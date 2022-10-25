from scipy import stats
from wrapper import Wrapper

class PoissonWrapper(Wrapper):
    def __init__(self, mu):
        super().__init__(stats.poisson, args=[mu])
