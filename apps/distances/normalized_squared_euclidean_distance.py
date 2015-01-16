# coding=utf-8
import operator

from apps.distances.distance import Distance


__author__ = 'cenk'

# TODO

##   1/2 * Norm[(u-Mean[u])-(v-Mean[v])] ^2 / (Norm[u-Mean[u]]^2+Norm[v-Mean[v]]^2)
class NormalizedSquaredEuclideanDistance(Distance):
    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]

            if len(point_a) == len(point_b):
                try:
                    self._result = sum(float(c) ** 2 for c in map(operator.sub, point_b, point_a))
                except:
                    raise
            else:
                raise ArithmeticError("You cant calculate euclidean distance of array has different sizes.")
        else:
            raise ArithmeticError("You must enter two array to find squared euclidean distance.")