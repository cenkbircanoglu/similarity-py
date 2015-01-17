# coding=utf-8

from apps.distances.distance import Distance


__author__ = 'cenk'


class DamerauLevenshteinDistance(Distance):
    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]
            try:
                point_a = point_a.lower()
                point_b = point_b.lower()
            except:
                pass
            if len(point_a) < len(point_b):
                pointb = point_b
                pointa = point_a
                point_a = pointb
                point_b = pointa

            if len(point_b) == 0:
                return len(point_a)

            previous_row = range(len(point_b) + 1)
            for i, c1 in enumerate(point_a):
                current_row = [i + 1]
                for j, c2 in enumerate(point_b):
                    insertions = previous_row[j + 1] + 1
                    deletions = current_row[j] + 1
                    substitutions = previous_row[j] + (c1 != c2)
                    current_row.append(min(insertions, deletions, substitutions))
                previous_row = current_row

            self._result = previous_row[-1]

        else:
            raise ArithmeticError("You must enter two array to find squared euclidean distance.")