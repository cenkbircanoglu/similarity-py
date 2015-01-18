# coding=utf-8
from unittest import TestCase

from apps.measure.boolean_data.russell_rao_dissimilarity import RussellRaoDissimilarity
from tests import test_logger


__author__ = 'cenk'


class RussellRaoDissimilarityTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("RussellRaoDissimilarityTest - test_algorithm Starts")
        data = [[1, 0, 1, 1, 0], [1, 1, 0, 1, 1]]
        russell_rao_dissimilarity = RussellRaoDissimilarity(data)
        russell_rao_dissimilarity.process()
        result = russell_rao_dissimilarity.get_result()
        self.assertEquals(0.6, result)

        data = [[True, False, True], [True, True, False]]
        russell_rao_dissimilarity = RussellRaoDissimilarity(data)
        russell_rao_dissimilarity.process()
        result = russell_rao_dissimilarity.get_result()
        self.assertEquals(0.6666666666666666, result)

        data = [[1, 1, 1, 1], [1, 1, 1, 1]]
        russell_rao_dissimilarity = RussellRaoDissimilarity(data)
        russell_rao_dissimilarity.process()
        result = russell_rao_dissimilarity.get_result()
        self.assertEquals(0.0, result)

        data = [[0, 0, 0, 0], [1, 1, 1, 1]]
        russell_rao_dissimilarity = RussellRaoDissimilarity(data)
        russell_rao_dissimilarity.process()
        result = russell_rao_dissimilarity.get_result()
        self.assertEquals(1.0, result)

        data = [[3], [4, 5, 6]]
        russell_rao_dissimilarity = RussellRaoDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            russell_rao_dissimilarity.process()
        self.assertEqual('You cant calculate Russell Rao dissimilarity of array has different sizes.',
                         context.exception.message)

        data = [[], []]
        russell_rao_dissimilarity = RussellRaoDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            russell_rao_dissimilarity.process()
        self.assertEqual('float division by zero',
                         context.exception.message)
        data = []
        russell_rao_dissimilarity = RussellRaoDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            russell_rao_dissimilarity.process()
        self.assertEqual('You must enter two array to find squared euclidean distance.',
                         context.exception.message)
        test_logger.debug("RussellRaoDissimilarityTest - test_algorithm Ends")
