from apps.permutation_combination.factorial import Factorial
from apps.permutation_combination.permutation.permutation import Permutation

__author__ = 'cenk'


class Combination(object):
    @classmethod
    def simple(self, number, r):
        delta = number - r
        if delta >= r:
            self.result = Permutation.simple(number, delta) / Factorial(r).result
        elif r > delta:
            self.result = Permutation.simple(number, r) / Factorial(delta).result
        return self.result

    """
    :k repeat time
    """

    @classmethod
    def repeating(self, number, r, k):
        return self.simple(number + k - 1, number - 1)