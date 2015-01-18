# coding=utf-8
import operator

from apps.measure.similarity_measure import SimilarityMeasure
from apps.measure.similarity_measure_type import SimilarityMeasureType


__author__ = 'cenk'


class ManhattanDistance(SimilarityMeasure):
    similarity_measure_type = SimilarityMeasureType.DISTANCE_ABBR

    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]

            if len(point_a) == len(point_b):
                try:
                    self._result = sum(abs(float(c)) for c in map(operator.sub, point_b, point_a))
                except:
                    raise
            else:
                raise ArithmeticError("You cant calculate Manhattan distance of array has different sizes.")
        else:
            raise ArithmeticError("You must enter two array to find Manhattan distance.")