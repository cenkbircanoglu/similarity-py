# coding=utf-8
from unittest import TestCase

from apps.distances.boolean_data.hamming_distance import HammingDistance


__author__ = 'cenk'


class HammingDistanceTest(TestCase):
    def test_algorithm(self):
        data = ["123", "246"]
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
        self.assertEqual('You cant calculate hamming distance of array has different sizes.',
                         context.exception.message)
