# coding=utf-8
from unittest import TestCase

from apps.distances.boolean_data.rogers_tanimoto_dissimilarity import RogersTanimotoDissimilarity
from tests import test_logger


__author__ = 'cenk'


class RogersTanimotoDissimilarityTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("RogersTanimotoDissimilarityTest - test_algorithm Starts")
        data = [[1, 0, 1, 1, 0], [1, 1, 0, 1, 1]]
        dice_dissimilarity = RogersTanimotoDissimilarity(data)
        dice_dissimilarity.process()
        result = dice_dissimilarity.get_result()
        self.assertEquals(0.75, result)

        data = [[True, False, True], [True, True, False]]
        dice_dissimilarity = RogersTanimotoDissimilarity(data)
        dice_dissimilarity.process()
        result = dice_dissimilarity.get_result()
        self.assertEquals(0.8, result)

        data = [[1, 1, 1, 1], [1, 1, 1, 1]]
        dice_dissimilarity = RogersTanimotoDissimilarity(data)
        dice_dissimilarity.process()
        result = dice_dissimilarity.get_result()
        self.assertEquals(0.0, result)

        data = [[0, 0, 0, 0], [1, 1, 1, 1]]
        dice_dissimilarity = RogersTanimotoDissimilarity(data)
        dice_dissimilarity.process()
        result = dice_dissimilarity.get_result()
        self.assertEquals(1.0, result)

        data = [[3], [4, 5, 6]]
        dice_dissimilarity = RogersTanimotoDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            dice_dissimilarity.process()
        self.assertEqual('You cant calculate Rogers Tanimoto dissimilarity of array has different sizes.',
                         context.exception.message)
        test_logger.debug("RogersTanimotoDissimilarityTest - test_algorithm Ends")
