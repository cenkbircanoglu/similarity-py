# coding=utf-8
from unittest import TestCase

from apps.distances.boolean_data.jaccard_dissimilarity import JaccardDissimilarity
from tests import test_logger


__author__ = 'cenk'


class JaccardDissimilarityTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("JaccardDissimilarityTest - test_algorithm Starts")
        data = ["123", "246"]
        jaccard_dissimilarity = JaccardDissimilarity(data)
        jaccard_dissimilarity.process()
        result = jaccard_dissimilarity.get_result()
        self.assertEquals(0.2, result)

        data = ["123", "123"]
        jaccard_dissimilarity = JaccardDissimilarity(data)
        jaccard_dissimilarity.process()
        result = jaccard_dissimilarity.get_result()
        self.assertEquals(1.0, result)

        data = ["abcde", "ABCDE"]
        jaccard_dissimilarity = JaccardDissimilarity(data)
        jaccard_dissimilarity.process()
        result = jaccard_dissimilarity.get_result()
        self.assertEquals(1.0, result)

        data = ["abcde", "ABCDf"]
        jaccard_dissimilarity = JaccardDissimilarity(data)
        jaccard_dissimilarity.process()
        result = jaccard_dissimilarity.get_result()
        self.assertEquals(0.6666666666666666, result)

        data = [[3], [4]]
        jaccard_dissimilarity = JaccardDissimilarity(data)
        jaccard_dissimilarity.process()
        result = jaccard_dissimilarity.get_result()
        self.assertEquals(0, result)

        data = [["a"], [4]]
        jaccard_dissimilarity = JaccardDissimilarity(data)
        jaccard_dissimilarity.process()
        result = jaccard_dissimilarity.get_result()
        self.assertEquals(0.0, result)

        data = ["10011", "00101"]
        jaccard_dissimilarity = JaccardDissimilarity(data)
        jaccard_dissimilarity.process()
        result = jaccard_dissimilarity.get_result()
        self.assertEquals(1, result)

        data = [[3], [4, 5, 6]]
        jaccard_dissimilarity = JaccardDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            jaccard_dissimilarity.process()
        self.assertEqual('You cant calculate hamming distance of array has different sizes.',
                         context.exception.message)
        test_logger.debug("JaccardDissimilarityTest - test_algorithm Ends")