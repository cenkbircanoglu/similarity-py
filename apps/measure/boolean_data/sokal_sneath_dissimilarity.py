# coding=utf-8
import operator

from apps.measure.similarity_measure import SimilarityMeasure
from apps.measure.similarity_measure_type import SimilarityMeasureType


__author__ = 'cenk'


class SokalSneathDissimilarity(SimilarityMeasure):
    similarity_measure_type = SimilarityMeasureType.DISSIMILARITY_ABBR

    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]

            if len(point_a) == len(point_b):
                and_list = map(operator.and_, point_b, point_a)
                xor_list = map(operator.xor, point_b, point_a)

                and_count = and_list.count(True)
                xor_count = xor_list.count(True)

                try:
                    self._result = ((2 * float(xor_count)) / (and_count + (2 * xor_count)))
                except:
                    raise
            else:
                raise ArithmeticError("You cant calculate Sokal Sneath dissimilarity of array has different sizes.")

        else:
            raise ArithmeticError("You must enter two array to find squared euclidean distance.")