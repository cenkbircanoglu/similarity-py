# coding=utf-8
import operator

from apps.measure.similarity_measure import SimilarityMeasure
from apps.measure.similarity_measure_type import SimilarityMeasureType
from apps.utils import custom_operators


__author__ = 'cenk'


class YuleDissimilarity(SimilarityMeasure):
    similarity_measure_type = SimilarityMeasureType.DISSIMILARITY_ABBR

    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]

            if len(point_a) == len(point_b):
                and_list = map(operator.and_, point_b, point_a)
                nor_list = [not i for i in map(operator.or_, point_b, point_a)]

                and_count = and_list.count(True)
                true_false = map(custom_operators.true_false, point_a, point_b)
                false_true = map(custom_operators.false_true, point_a, point_b)

                nor_count = nor_list.count(True)
                true_false_count = true_false.count(True)
                false_true_count = false_true.count(True)
                if float(true_false_count * false_true_count) == 0:
                    self._result = 0.0
                else:
                    self._result = ((2 * float(true_false_count * false_true_count)) / (
                        (nor_count * and_count) + (true_false_count * false_true_count)))

            else:
                raise ArithmeticError("You cant calculate Yule dissimilarity of array has different sizes.")

        else:
            raise ArithmeticError("You must enter two array to find squared euclidean distance.")