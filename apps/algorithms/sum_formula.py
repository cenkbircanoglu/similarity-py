import math

__author__ = 'cenk'


class SumFormula:
    def __init__(self):
        self._data = []

    def exponential(self, x, power):
        return math.pow(x, power)

    def calculate(self, data, is_tuple=False, index=None, power=1):
        if is_tuple:
            self._data = [obj[index] for obj in data]
        else:
            self._data = data
        self.power = power
        return self.__algorithm()

    def __algorithm(self):
        total = 0.0
        for num in self._data:
            total += self.exponential(float(num), self.power)
        return total
