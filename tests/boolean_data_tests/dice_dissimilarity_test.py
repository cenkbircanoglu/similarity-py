# coding=utf-8
from unittest import TestCase

from apps.distances.boolean_data.dice_dissimilarity import DiceDissimilarity
from tests import test_logger


__author__ = 'cenk'


class DiceDissimilarityTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("DiceDissimilarityTest - test_algorithm Starts")
        data = ["10110", "11011"]
        dice_dissimilarity = DiceDissimilarity(data)
        dice_dissimilarity.process()
        result = dice_dissimilarity.get_result()
        self.assertEquals(3.0 / 7, result)

        data = ["123", "123"]
        dice_dissimilarity = DiceDissimilarity(data)
        dice_dissimilarity.process()
        result = dice_dissimilarity.get_result()
        self.assertEquals(0.0, result)

        data = ["abcde", "ABCDE"]
        dice_dissimilarity = DiceDissimilarity(data)
        dice_dissimilarity.process()
        result = dice_dissimilarity.get_result()
        self.assertEquals(0, result)

        data = ["abcde", "ABCDf"]
        dice_dissimilarity = DiceDissimilarity(data)
        dice_dissimilarity.process()
        result = dice_dissimilarity.get_result()
        self.assertEquals(0.1111111111111111, result)

        data = [[3], [4]]
        dice_dissimilarity = DiceDissimilarity(data)
        dice_dissimilarity.process()
        result = dice_dissimilarity.get_result()
        self.assertEquals(1, result)

        data = [["a"], [4]]
        dice_dissimilarity = DiceDissimilarity(data)
        dice_dissimilarity.process()
        result = dice_dissimilarity.get_result()
        self.assertEquals(1, result)

        data = ["10011", "00101"]
        dice_dissimilarity = DiceDissimilarity(data)
        dice_dissimilarity.process()
        result = dice_dissimilarity.get_result()
        self.assertEquals(0.42857142857142855, result)

        data = [(True, False, True), (True, True, False)]
        dice_dissimilarity = DiceDissimilarity(data)
        dice_dissimilarity.process()
        result = dice_dissimilarity.get_result()
        self.assertEquals(0.5, result)

        data = [[3], [4, 5, 6]]
        dice_dissimilarity = DiceDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            dice_dissimilarity.process()
        self.assertEqual('You cant calculate hamming distance of array has different sizes.',
                         context.exception.message)
        test_logger.debug("DiceDissimilarityTest - test_algorithm Ends")