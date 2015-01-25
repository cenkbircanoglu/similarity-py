# coding=utf-8
"""
Created on 18 January 2014
@author: Cenk Bircanoglu
"""
import operator
import math

from similarityPy.algorithms.mean import Mean
from similarityPy.measure.similarity_measure import SimilarityMeasure
from similarityPy.measure.similarity_measure_type import SimilarityMeasureType


class CorrelationDistance(SimilarityMeasure):
    similarity_measure_type = SimilarityMeasureType.DISTANCE_RATIO_ABBR

    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]

            if len(point_a) == len(point_b):
                mean = Mean()
                mean_b = mean.calculate(point_b)
                mean_a = mean.calculate(point_a)
                try:
                    point_b_normalized = [(float(c) - mean_b) for c in point_b]
                    point_a_normalized = [(float(c) - mean_a) for c in point_a]
                    dividend = sum(map(operator.mul, point_a_normalized, point_b_normalized))
                    point_b_squared_normalized = sum([(float(c) - mean_b) ** 2 for c in point_b])
                    point_a_squared_normalized = sum([(float(c) - mean_a) ** 2 for c in point_a])
                    divider = math.sqrt(point_b_squared_normalized) * math.sqrt(point_a_squared_normalized)
                    self._result = 1 - (dividend / divider)
                except ArithmeticError:
                    raise ArithmeticError("float division by zero")

            else:
                raise ArithmeticError("You cant calculate Correlation distance of array has different sizes.")

        else:
            raise ArithmeticError("You must enter two array to find Correlation distance.")