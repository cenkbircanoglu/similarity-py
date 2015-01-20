# coding=utf-8
import math
import operator

from similarityPy.measure.similarity_measure import SimilarityMeasure
from similarityPy.measure.similarity_measure_type import SimilarityMeasureType


__author__ = 'cenk'


class EuclideanDistance(SimilarityMeasure):
    similarity_measure_type = SimilarityMeasureType.DISTANCE_ABBR

    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]

            if len(point_a) == len(point_b):
                try:
                    total = sum(float(c) ** 2 for c in map(operator.sub, point_b, point_a))
                    self._result = math.sqrt(total)
                except:
                    raise
            else:
                raise ArithmeticError("You cant calculate Euclidean distance of array has different sizes.")

        else:
            raise ArithmeticError("You must enter two array to find Euclidean distance.")