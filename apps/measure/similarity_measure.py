# coding=utf-8
import heapq

from apps.measure.similarity_measure_type import SimilarityMeasureType, SIMILARITY_RATIO, DISTANCE, DISSIMILARITY, \
    DISSIMILARITY_RATIO, DISTANCE_RATIO


__author__ = 'cenk'


class SimilarityMeasure:
    similarity_measure_type = SimilarityMeasureType.DISTANCE_ABBR

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

    def get_result(self):
        return self._result

    @classmethod
    def calculate(cls, data):
        distance = cls(data)
        distance.process()
        return distance.get_result()

    @classmethod
    def min_max(cls, data, k=1):
        if cls.similarity_measure_type == DISTANCE or cls.similarity_measure_type == DISSIMILARITY or cls.similarity_measure_type == DISSIMILARITY_RATIO or cls.similarity_measure_type == DISTANCE_RATIO:
            return heapq.nsmallest(k, data)
        elif cls.similarity_measure_type == SIMILARITY_RATIO:
            return heapq.nlargest(k, data)