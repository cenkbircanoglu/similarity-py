# coding=utf-8
from unittest import TestCase

from apps.measure.boolean_data.rogers_tanimoto_dissimilarity import RogersTanimotoDissimilarity
from tests import test_logger


__author__ = 'cenk'


class RogersTanimotoDissimilarityTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("RogersTanimotoDissimilarityTest - test_algorithm Starts")
        data = [[1, 0, 1, 1, 0], [1, 1, 0, 1, 1]]
        rogers_tanimoto_dissimilarity = RogersTanimotoDissimilarity(data)
        rogers_tanimoto_dissimilarity.process()
        result = rogers_tanimoto_dissimilarity.get_result()
        self.assertEquals(0.75, result)

        data = [[True, False, True], [True, True, False]]
        rogers_tanimoto_dissimilarity = RogersTanimotoDissimilarity(data)
        rogers_tanimoto_dissimilarity.process()
        result = rogers_tanimoto_dissimilarity.get_result()
        self.assertEquals(0.8, result)

        data = [[1, 1, 1, 1], [1, 1, 1, 1]]
        rogers_tanimoto_dissimilarity = RogersTanimotoDissimilarity(data)
        rogers_tanimoto_dissimilarity.process()
        result = rogers_tanimoto_dissimilarity.get_result()
        self.assertEquals(0.0, result)

        data = [[0, 0, 0, 0], [1, 1, 1, 1]]
        rogers_tanimoto_dissimilarity = RogersTanimotoDissimilarity(data)
        rogers_tanimoto_dissimilarity.process()
        result = rogers_tanimoto_dissimilarity.get_result()
        self.assertEquals(1.0, result)

        data = [[3], [4, 5, 6]]
        rogers_tanimoto_dissimilarity = RogersTanimotoDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            rogers_tanimoto_dissimilarity.process()
        self.assertEqual('You cant calculate Rogers Tanimoto dissimilarity of array has different sizes.',
                         context.exception.message)

        data = [[], []]
        rogers_tanimoto_dissimilarity = RogersTanimotoDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            rogers_tanimoto_dissimilarity.process()
        self.assertEqual('float division by zero',
                         context.exception.message)
        data = []
        rogers_tanimoto_dissimilarity = RogersTanimotoDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            rogers_tanimoto_dissimilarity.process()
        self.assertEqual('You must enter two array to find squared euclidean distance.',
                         context.exception.message)
        test_logger.debug("RogersTanimotoDissimilarityTest - test_algorithm Ends")
