# coding=utf-8
from unittest import TestCase

from apps.measure.boolean_data.jaccard_dissimilarity import JaccardDissimilarity
from tests import test_logger


__author__ = 'cenk'


class JaccardDissimilarityTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("JaccardDissimilarityTest - test_algorithm Starts")
        data = [[1, 0, 1, 1, 0], [1, 1, 0, 1, 1]]
        jaccard_dissimilarity = JaccardDissimilarity(data)
        jaccard_dissimilarity.process()
        result = jaccard_dissimilarity.get_result()
        self.assertEquals(0.6, result)

        data = [[True, False, True], [True, True, False]]
        jaccard_dissimilarity = JaccardDissimilarity(data)
        jaccard_dissimilarity.process()
        result = jaccard_dissimilarity.get_result()
        self.assertEquals(0.6666666666666666, result)

        data = [[1, 1, 1, 1], [1, 1, 1, 1]]
        jaccard_dissimilarity = JaccardDissimilarity(data)
        jaccard_dissimilarity.process()
        result = jaccard_dissimilarity.get_result()
        self.assertEquals(0.0, result)

        data = [[0, 0, 0, 0], [1, 1, 1, 1]]
        jaccard_dissimilarity = JaccardDissimilarity(data)
        jaccard_dissimilarity.process()
        result = jaccard_dissimilarity.get_result()
        self.assertEquals(1.0, result)

        data = [[3], [4, 5, 6]]
        jaccard_dissimilarity = JaccardDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            jaccard_dissimilarity.process()
        self.assertEqual('You cant calculate hamming distance of array has different sizes.',
                         context.exception.message)

        data = [[0, 0, 0, 0], [0, 0, 0, 0]]
        jaccard_dissimilarity = JaccardDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            jaccard_dissimilarity.process()
        self.assertEqual('float division by zero',
                         context.exception.message)

        data = []
        jaccard_dissimilarity = JaccardDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            jaccard_dissimilarity.process()
        self.assertEqual('You must enter two array to find squared euclidean distance.',
                         context.exception.message)
        test_logger.debug("JaccardDissimilarityTest - test_algorithm Ends")