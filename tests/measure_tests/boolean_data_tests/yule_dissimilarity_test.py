# coding=utf-8
from unittest import TestCase

from apps.measure.boolean_data.yule_dissimilarity import YuleDissimilarity
from tests import test_logger


__author__ = 'cenk'


class YuleDissimilarityTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("YuleDissimilarityTest - test_algorithm Starts")
        data = [[1, 0, 1, 1, 0], [1, 1, 0, 1, 1]]
        yule_dissimilarity = YuleDissimilarity(data)
        yule_dissimilarity.process()
        result = yule_dissimilarity.get_result()
        self.assertEquals(2.0, result)

        data = [[True, False, True], [True, True, False]]
        yule_dissimilarity = YuleDissimilarity(data)
        yule_dissimilarity.process()
        result = yule_dissimilarity.get_result()
        self.assertEquals(2, result)

        data = [[0, 0, 0, 0], [0, 0, 0, 0]]
        yule_dissimilarity = YuleDissimilarity(data)
        yule_dissimilarity.process()
        result = yule_dissimilarity.get_result()
        self.assertEquals(0.0, result)

        data = [[0, 1, 0, 1], [1, 0, 1, 0]]
        yule_dissimilarity = YuleDissimilarity(data)
        yule_dissimilarity.process()
        result = yule_dissimilarity.get_result()
        self.assertEquals(2.0, result)

        data = [[3], [4, 5, 6]]
        yule_dissimilarity = YuleDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            yule_dissimilarity.process()
        self.assertEqual('You cant calculate Yule dissimilarity of array has different sizes.',
                         context.exception.message)
        data = []
        yule_dissimilarity = YuleDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            yule_dissimilarity.process()
        self.assertEqual('You must enter two array to find squared euclidean distance.',
                         context.exception.message)
        test_logger.debug("YuleDissimilarityTest - test_algorithm Ends")
