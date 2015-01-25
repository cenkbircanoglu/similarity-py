# coding=utf-8
"""
Created on 18 January 2014
@author: Cenk Bircanoglu
"""
import operator

from similarityPy.measure.similarity_measure import SimilarityMeasure
from similarityPy.measure.similarity_measure_type import SimilarityMeasureType


class ChessBoardDistance(SimilarityMeasure):
    similarity_measure_type = SimilarityMeasureType.DISTANCE_RATIO_ABBR

    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]

            if len(point_a) == len(point_b):
                try:
                    self._result = max(map(operator.sub, point_b, point_a))
                except ArithmeticError:
                    raise ArithmeticError("float division by zero")
            else:
                raise ArithmeticError("You cant calculate Chess Board distance of array has different sizes.")
        else:
            raise ArithmeticError("You must enter two array to find Chess Board distance.")