import math

from similarityPy.algorithms.variance import Variance


__author__ = 'cenk'


class StandartDeviation:
    def __init__(self):
        self._data = []

    def calculate(self, data, is_tuple=False, index=None):
        if is_tuple:
            self._data = sorted([float(obj[index]) for obj in data])
        else:
            self._data = sorted(data)

        return self.__algorithm()

    def __algorithm(self):
        variance = Variance()
        return round(math.pow(variance.calculate(self._data), 0.5), 4)