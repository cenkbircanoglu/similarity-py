# coding=utf-8
from unittest import TestCase

from apps.measure.string_data.hamming_distance import HammingDistance
from tests import test_logger


__author__ = 'cenk'


class HammingDistanceTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("HammingDistanceTest - test_algorithm Starts")
        data = ["123", "246"]
        hamming_distance = HammingDistance(data)
        hamming_distance.process()
        result = hamming_distance.get_result()
        self.assertEquals(3, result)

        data = ["bccbbcb", "ccbbccb"]
        hamming_distance = HammingDistance(data)
        hamming_distance.process()
        result = hamming_distance.get_result()
        self.assertEquals(3, result)

        data = [[0, 1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1, 0]]
        hamming_distance = HammingDistance(data)
        hamming_distance.process()
        result = hamming_distance.get_result()
        self.assertEquals(3, result)

        data = ["123", "123"]
        hamming_distance = HammingDistance(data)
        hamming_distance.process()
        result = hamming_distance.get_result()
        self.assertEquals(0, result)

        data = ["abcde", "ABCDE"]
        hamming_distance = HammingDistance(data)
        hamming_distance.process()
        result = hamming_distance.get_result()
        self.assertEquals(0, result)

        data = ["abcde", "ABCDf"]
        hamming_distance = HammingDistance(data)
        hamming_distance.process()
        result = hamming_distance.get_result()
        self.assertEquals(1, result)

        data = [[3], [4]]
        hamming_distance = HammingDistance(data)
        hamming_distance.process()
        result = hamming_distance.get_result()
        self.assertEquals(1, result)

        data = [["a"], [4]]
        hamming_distance = HammingDistance(data)
        hamming_distance.process()
        result = hamming_distance.get_result()
        self.assertEquals(1, result)

        data = ["10011", "00101"]
        hamming_distance = HammingDistance(data)
        hamming_distance.process()
        result = hamming_distance.get_result()
        self.assertEquals(3, result)

        data = [[3], [4, 5, 6]]
        hamming_distance = HammingDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            hamming_distance.process()
        self.assertEqual('You cant calculate Hamming distance of array has different sizes.',
                         context.exception.message)

        data = []
        hamming_distance = HammingDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            hamming_distance.process()
        self.assertEqual('You must enter two array to find Hamming distance.',
                         context.exception.message)

        test_logger.debug("HammingDistanceTest - test_algorithm Ends")
