# coding=utf-8

from similarityPy.measure.similarity_measure import SimilarityMeasure
from similarityPy.measure.similarity_measure_type import SimilarityMeasureType


__author__ = 'cenk'


class EditDistance(SimilarityMeasure):
    similarity_measure_type = SimilarityMeasureType.DISTANCE_ABBR

    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]

            try:
                point_a = point_a.lower()
                point_b = point_b.lower()
            except:
                pass
            len_1 = len(point_a)
            len_2 = len(point_b)
            x = [[0] * (len_2 + 1) for _ in range(len_1 + 1)]

            for i in range(0, len_1 + 1):  # initialization of base case values
                x[i][0] = i
            for j in range(0, len_2 + 1):
                x[0][j] = j
            for i in range(1, len_1 + 1):

                for j in range(1, len_2 + 1):

                    if point_a[i - 1] == point_b[j - 1]:
                        x[i][j] = x[i - 1][j - 1]

                    else:
                        x[i][j] = min(x[i][j - 1], x[i - 1][j], x[i - 1][j - 1]) + 1

            self._result = x[i][j]


        else:
            raise ArithmeticError("You must enter two array to find Edit distance.")