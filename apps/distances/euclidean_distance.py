import math
import operator

from apps.distances.distance import Distance


__author__ = 'cenk'


def sum_of_squares_of_digits(value):
    return


class EuclideanDistance(Distance):
    def _algorithm(self):
        point_a = self._data[0]
        point_b = self._data[1]
        total = sum(float(c) ** 2 for c in map(operator.sub, point_b, point_a))
        self._result = math.sqrt(total)
