from apps.permutation_combination.factorial import Factorial

__author__ = 'cenk'


class Permutation(object):
    @classmethod
    def simple(self, number, r):
        if number > r:
            self.result = number * Permutation.simple(number - 1, r)
        if number == r:
            self.result = 1
        return self.result

    @classmethod
    def without_repeating(self, number, r):
        delta = number - r
        return self.simple(number, delta)

    @classmethod
    def same_k_object(self, number, k):
        if type(k) == int:
            divide = number / k
            if divide >= 1 & divide % 1 == 0:
                return self.simple(number, divide) / ((k - 1) * Factorial(divide).result)
            return 'Error, Divide is not a natural number!!!'
        elif type(k) == list:
            factorial = Factorial(number).result
            for value in k:
                factorial = factorial / Factorial(value).result
            return factorial