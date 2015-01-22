# coding=utf-8
"""
Created on 18 January 2014
@author: Cenk Bircanoglu
"""
import heapq

from similarityPy.measure.similarity_measure_type import SimilarityMeasureType, SIMILARITY_RATIO, DISTANCE, \
    DISSIMILARITY, \
    DISSIMILARITY_RATIO, DISTANCE_RATIO


class SimilarityMeasure:
    """
    This class is super class for distance calculation.
    :param data (list of list): [ {"abcd", "efgh", "ijkl" }, {"abdc", "efhg", "lkmn"} ]
    """
    similarity_measure_type = SimilarityMeasureType.DISTANCE_ABBR

    def __init__(self, data):
        """
        :param data (list of list): [ {"abcd", "efgh", "ijkl" }, {"abdc", "efhg", "lkmn"} ]
        :return:None
        """
        if type(data) is list:
            self._data = data
            self._result = None
        else:
            raise TypeError("You must initialize array.")

    def _algorithm(self):
        """
        Raise NotImplementedError.
        :return:None
        """
        raise NotImplementedError("Subclasses should implement this!")

    def process(self):
        """
        Call the algorithm and calculate the distance.
        :return:None
        """
        self._algorithm()

    def get_result(self):
        """
        Get function of result.
        :return: result (list)
        """
        return self._result

    @classmethod
    def calculate(cls, data):
        """
        This is a method that simplfy calling and accessing the result. Set data, then process and then return the result.
        :param data:
        :return: result (list)
        """
        distance = cls(data)
        distance.process()
        return distance.get_result()

    @classmethod
    def min_max(cls, data, k=1):
        """
        This method returns the smallest k or highest k value in the array (that given as data param).
        :param data: (list)
        :param k: (number) count of requested array size.
        :return: list of n highest or smallest (list)
        """
        if cls.similarity_measure_type == DISTANCE or cls.similarity_measure_type == DISSIMILARITY or cls.similarity_measure_type == DISSIMILARITY_RATIO or cls.similarity_measure_type == DISTANCE_RATIO:
            return heapq.nsmallest(k, data)
        elif cls.similarity_measure_type == SIMILARITY_RATIO:
            return heapq.nlargest(k, data)