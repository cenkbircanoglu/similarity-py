# coding=utf-8
from unittest import TestCase

from apps.distances.boolean_data.matching_dissimilarity import MatchingDissimilarity


__author__ = 'cenk'


class MatchingDissimilarityTest(TestCase):
    def test_algorithm(self):
        data = ["123", "246"]
        matching_dissimilarity = MatchingDissimilarity(data)
        matching_dissimilarity.process()
        result = matching_dissimilarity.get_result()
        self.assertEquals(0.0, result)

        data = ["123", "123"]
        matching_dissimilarity = MatchingDissimilarity(data)
        matching_dissimilarity.process()
        result = matching_dissimilarity.get_result()
        self.assertEquals(1, result)

        data = ["abcde", "ABCDE"]
        matching_dissimilarity = MatchingDissimilarity(data)
        matching_dissimilarity.process()
        result = matching_dissimilarity.get_result()
        self.assertEquals(1, result)

        data = ["abcde", "ABCDf"]
        matching_dissimilarity = MatchingDissimilarity(data)
        matching_dissimilarity.process()
        result = matching_dissimilarity.get_result()
        self.assertEquals(0.8, result)

        data = [[3], [4]]
        matching_dissimilarity = MatchingDissimilarity(data)
        matching_dissimilarity.process()
        result = matching_dissimilarity.get_result()
        self.assertEquals(0, result)

        data = [["a"], [4]]
        matching_dissimilarity = MatchingDissimilarity(data)
        matching_dissimilarity.process()
        result = matching_dissimilarity.get_result()
        self.assertEquals(0, result)

        data = ["10011", "00101"]
        matching_dissimilarity = MatchingDissimilarity(data)
        matching_dissimilarity.process()
        result = matching_dissimilarity.get_result()
        self.assertEquals(0.4, result)

        data = [[3], [4, 5, 6]]
        matching_dissimilarity = MatchingDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            matching_dissimilarity.process()
        self.assertEqual('You cant calculate matching dissimilarity of array has different sizes.',
                         context.exception.message)
