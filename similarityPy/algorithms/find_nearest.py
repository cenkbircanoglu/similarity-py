__author__ = 'cenk'


class FindNearest:
    def __init__(self, data, point, distance_algorithm, k=1):
        if type(data) is list and point:
            self._data = data
            self._point = point
            self._result = None
            self._distance = None
            self._distance_algorithm = distance_algorithm
            self.k = k
        else:
            raise TypeError("You must initialize array and a point")

    def get_result(self):
        return self._result

    def process(self):
        distances = [self._distance_algorithm.calculate([self._point, x]) for x in self._data]
        self._distance = self._distance_algorithm.min_max(distances, self.k)
        self._result = []
        if len(self._distance) == 1:
            self._result = self._data[distances.index(self._distance[0])]
        else:
            for i in self._distance:
                self._result.append(self._data[distances.index(i)])