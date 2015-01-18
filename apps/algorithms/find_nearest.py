__author__ = 'cenk'


class FindNearest:
    def __init__(self, data, point, distance_algorithm):
        if type(data) is list and point:
            self._data = data
            self._point = point
            self._result = None
            self._distance = None
            self._distance_algorithm = distance_algorithm
        else:
            raise TypeError("You must initialize array and a point")

    def get_result(self):
        return self._result

    def process(self):
        try:
            distances = [self._distance_algorithm.calculate([self._point, x]) for x in self._data]
            # dice_dissimilarity = DiceDissimilarity(data)
            # dice_dissimilarity.process()
            # result = dice_dissimilarity.get_result()
            self._distance = min(distances)
            self._result = self._data[distances.index(self._distance)]
        except:
            raise