# coding=utf-8
from apps.distance.distance_type import DistanceType, DISSIMILARITY_ABBR, DISTANCE_ABBR, DISSIMILARITY_RATIO_ABBR, \
    SIMILARITY_RATIO_ABBR


__author__ = 'cenk'


class Distance:
    distance_type = DistanceType.DISSIMILARITY

    def __init__(self, data):

        if type(data) is list:
            self._data = data
            self._result = None
        else:
            raise TypeError("You must initialize array.")

    def _algorithm(self):
        raise NotImplementedError("Subclasses should implement this!")

    def process(self):
        self._algorithm()

    def clear_data(self):
        pass

    def get_result(self):
        return self._result

    @classmethod
    def calculate(cls, data):
        distance = cls(data)
        distance.process()
        return distance.get_result()

    @classmethod
    def min_max(cls, data):
        if cls.distance_type == DISTANCE_ABBR or cls.distance_type == DISSIMILARITY_ABBR or cls.distance_type == DISSIMILARITY_RATIO_ABBR:
            return min(data)
        elif cls.distance_type == SIMILARITY_RATIO_ABBR:
            return max(data)