# coding=utf-8
import operator

from similarityPy.measure.similarity_measure import SimilarityMeasure
from similarityPy.measure.similarity_measure_type import SimilarityMeasureType


__author__ = 'cenk'


class CanberraDistance(SimilarityMeasure):
    similarity_measure_type = SimilarityMeasureType.DISTANCE_ABBR

    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]

            if len(point_a) == len(point_b):
                try:
                    dividend_list = map(operator.sub, point_b, point_a)
                    divider_list = map(operator.add, [float(abs(i)) for i in point_b], [float(abs(i)) for i in point_a])
                    self._result = sum(float(c) for c in map(operator.div, dividend_list, divider_list))
                except:
                    raise
            else:
                raise ArithmeticError("You cant calculate Canberra distance of array has different sizes.")
        else:
            raise ArithmeticError("You must enter two array to find squared Canberra distance.")