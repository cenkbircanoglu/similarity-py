# coding=utf-8
from unittest import TestCase

from apps.measure.string_data.damerau_levenshtein_distance import DamerauLevenshteinDistance
from tests import test_logger


__author__ = 'cenk'


class DamerauLevenshteinDistanceTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("DamerauLevenshteinDistanceTest - test_algorithm Starts")
        data = ["abc", "cba"]
        damerau_levenshtein_distance = DamerauLevenshteinDistance(data)
        damerau_levenshtein_distance.process()
        result = damerau_levenshtein_distance.get_result()
        self.assertEquals(2, result)

        data = [[1, 0, 0, 1, 1], [0, 0, 1, 0, 1]]
        damerau_levenshtein_distance = DamerauLevenshteinDistance(data)
        damerau_levenshtein_distance.process()
        result = damerau_levenshtein_distance.get_result()
        self.assertEquals(2, result)

        data = ["bccbbcb", "ccbbccb"]
        damerau_levenshtein_distance = DamerauLevenshteinDistance(data)
        damerau_levenshtein_distance.process()
        result = damerau_levenshtein_distance.get_result()
        self.assertEquals(2, result)

        data = ["123", "123"]
        damerau_levenshtein_distance = DamerauLevenshteinDistance(data)
        damerau_levenshtein_distance.process()
        result = damerau_levenshtein_distance.get_result()
        self.assertEquals(0, result)

        data = [[0, 1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1, 0]]
        damerau_levenshtein_distance = DamerauLevenshteinDistance(data)
        damerau_levenshtein_distance.process()
        result = damerau_levenshtein_distance.get_result()
        self.assertEquals(2, result)

        data = ["ac", "ca"]
        damerau_levenshtein_distance = DamerauLevenshteinDistance(data)
        damerau_levenshtein_distance.process()
        result = damerau_levenshtein_distance.get_result()
        self.assertEquals(1, result)

        data = ["abcde", "ABCDf"]
        damerau_levenshtein_distance = DamerauLevenshteinDistance(data)
        damerau_levenshtein_distance.process()
        result = damerau_levenshtein_distance.get_result()
        self.assertEquals(1, result)

        data = [[3], [4]]
        damerau_levenshtein_distance = DamerauLevenshteinDistance(data)
        damerau_levenshtein_distance.process()
        result = damerau_levenshtein_distance.get_result()
        self.assertEquals(1, result)

        data = [["a"], [4]]
        damerau_levenshtein_distance = DamerauLevenshteinDistance(data)
        damerau_levenshtein_distance.process()
        result = damerau_levenshtein_distance.get_result()
        self.assertEquals(1, result)

        data = ["10011", "00101"]
        damerau_levenshtein_distance = DamerauLevenshteinDistance(data)
        damerau_levenshtein_distance.process()
        result = damerau_levenshtein_distance.get_result()
        self.assertEquals(2, result)

        data = []
        damerau_levenshtein_distance = DamerauLevenshteinDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            damerau_levenshtein_distance.process()
        self.assertEqual('You must enter two array to find Demerau Levenshtein distance.',
                         context.exception.message)

        test_logger.debug("DamerauLevenshteinDistanceTest - test_algorithm Ends")
