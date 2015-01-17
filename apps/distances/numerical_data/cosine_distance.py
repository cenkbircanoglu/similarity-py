# coding=utf-8
import operator

from apps.distances.distance import Distance
from apps.algorithms.norm import Norm


__author__ = 'cenk'


class CosineDistance(Distance):
    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]

            if len(point_a) == len(point_b):
                try:
                    dividend = sum(map(operator.mul, point_b, point_a))
                    divider = Norm.calculate(point_b) * Norm.calculate(point_a)
                    self._result = 1 - (dividend / divider)
                except:
                    raise
            else:
                raise ArithmeticError("You cant calculate euclidean distance of array has different sizes.")
        else:
            raise ArithmeticError("You must enter two array to find squared euclidean distance.")