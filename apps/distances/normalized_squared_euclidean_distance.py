# coding=utf-8
import operator

from apps.distances.distance import Distance


__author__ = 'cenk'

##TODO
class NormalizedSquaredEuclideanDistance(Distance):
    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]
            if len(point_a) == len(point_b):
                total_a = sum(point_a)
                total_b = sum(point_b)
                try:
                    dividend = sum(
                        (float(c) + (total_b / 2) - (total_a / 2)) ** 2 for c in map(operator.sub, point_a, point_b))
                    divider = 2 * (sum((float(c) - (total_a / 2)) ** 2 for c in point_a) + sum(
                        (float(c) - (total_b / 2) ) ** 2 for c in point_b))
                    self._result = (dividend / divider)
                except:
                    raise
            else:
                raise ArithmeticError("You cant calculate euclidean distance of array has different sizes.")
        else:
            raise ArithmeticError("You must enter two array to find squared euclidean distance.")