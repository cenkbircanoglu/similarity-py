# coding=utf-8

from apps.measure.similarity_measure import SimilarityMeasure
from apps.measure.similarity_measure_type import SimilarityMeasureType


__author__ = 'cenk'


class DamerauLevenshteinDistance(SimilarityMeasure):
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
            d = {}
            len_a = len(point_a)
            len_b = len(point_b)
            for i in xrange(-1, len_a + 1):
                d[(i, -1)] = i + 1
            for j in xrange(-1, len_b + 1):
                d[(-1, j)] = j + 1

            for i in xrange(len_a):
                for j in xrange(len_b):
                    if point_a[i] == point_b[j]:
                        cost = 0
                    else:
                        cost = 1
                    d[(i, j)] = min(
                        d[(i - 1, j)] + 1,  # deletion
                        d[(i, j - 1)] + 1,  # insertion
                        d[(i - 1, j - 1)] + cost,  # substitution
                    )
                    if i and j and point_a[i] == point_b[j - 1] and point_a[i - 1] == point_b[j]:
                        d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)  # transposition

            self._result = d[len_a - 1, len_b - 1]

        else:
            raise ArithmeticError("You must enter two array to find Demerau Levenshtein distance.")