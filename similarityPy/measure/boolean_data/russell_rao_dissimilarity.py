# coding=utf-8
import operator

from similarityPy.measure.similarity_measure import SimilarityMeasure
from similarityPy.measure.similarity_measure_type import SimilarityMeasureType


__author__ = 'cenk'


class RussellRaoDissimilarity(SimilarityMeasure):
    similarity_measure_type = SimilarityMeasureType.DISSIMILARITY_ABBR

    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]

            if len(point_a) == len(point_b):
                xor_list = map(operator.xor, point_b, point_a)
                nor_list = [not i for i in map(operator.or_, point_b, point_a)]

                xor_count = xor_list.count(True)
                nor_count = nor_list.count(True)

                try:
                    self._result = ((float(xor_count) + nor_count) / len(point_a))
                except:
                    raise
            else:
                raise ArithmeticError("You cant calculate Russell Rao dissimilarity of array has different sizes.")

        else:
            raise ArithmeticError("You must enter two array to find squared euclidean distance.")