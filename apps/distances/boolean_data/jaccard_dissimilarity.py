# coding=utf-8

from apps.distances.distance import Distance
from apps.mathematical_set.finitive_set import FinitiveMatSet
from apps.mathematical_set.math_function import MathFunction
from apps.mathematical_set.two_math_set_comparence import TwoMathSetComparence


__author__ = 'cenk'


class JaccardDissimilarity(Distance):
    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]

            if len(point_a) == len(point_b):

                try:
                    point_a = point_a.lower()
                    point_b = point_b.lower()
                except:
                    pass
                set_a = FinitiveMatSet(MathFunction(lambda x: x), point_a, 'A')
                set_b = FinitiveMatSet(MathFunction(lambda x: x), point_b, 'B')

                two_math_set_comparence = TwoMathSetComparence()
                intersection_size = two_math_set_comparence.intersection_size([set_a, set_b])
                association_size = two_math_set_comparence.association_size([set_a, set_b])

                try:
                    self._result = (float(intersection_size) / association_size)
                except:
                    raise
            else:
                raise ArithmeticError("You cant calculate hamming distance of array has different sizes.")

        else:
            raise ArithmeticError("You must enter two array to find squared euclidean distance.")