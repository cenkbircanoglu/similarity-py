# coding=utf-8
from unittest import TestCase

from apps.distances.boolean_data.jaccard_distance import JaccardDistance


__author__ = 'cenk'


class JaccardDistanceTest(TestCase):
    def test_algorithm(self):
        data = ["123", "246"]
        jaccard_distance = JaccardDistance(data)
        jaccard_distance.process()
        result = jaccard_distance.get_result()
        self.assertEquals(0.2, result)

        data = ["123", "123"]
        jaccard_distance = JaccardDistance(data)
        jaccard_distance.process()
        result = jaccard_distance.get_result()
        self.assertEquals(1.0, result)

        data = ["abcde", "ABCDE"]
        jaccard_distance = JaccardDistance(data)
        jaccard_distance.process()
        result = jaccard_distance.get_result()
        self.assertEquals(1.0, result)

        data = ["abcde", "ABCDf"]
        jaccard_distance = JaccardDistance(data)
        jaccard_distance.process()
        result = jaccard_distance.get_result()
        self.assertEquals(0.6666666666666666, result)

        data = [[3], [4]]
        jaccard_distance = JaccardDistance(data)
        jaccard_distance.process()
        result = jaccard_distance.get_result()
        self.assertEquals(0, result)

        data = [["a"], [4]]
        jaccard_distance = JaccardDistance(data)
        jaccard_distance.process()
        result = jaccard_distance.get_result()
        self.assertEquals(0.0, result)

        data = ["10011", "00101"]
        jaccard_distance = JaccardDistance(data)
        jaccard_distance.process()
        result = jaccard_distance.get_result()
        self.assertEquals(1, result)

        data = [[3], [4, 5, 6]]
        jaccard_distance = JaccardDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            jaccard_distance.process()
        self.assertEqual('You cant calculate hamming distance of array has different sizes.',
                         context.exception.message)
