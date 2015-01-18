# coding=utf-8
from unittest import TestCase

from apps.measure.numerical_data.normalized_squared_euclidean_distance import NormalizedSquaredEuclideanDistance
from tests import test_logger


__author__ = 'cenk'


class NormalizedSquaredEuclideanDistanceTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("NormalizedSquaredEuclideanDistanceTest - test_algorithm Starts")
        data = [(1, 2, 3), (3, 5, 10)]
        normalized_squared_euclidean_distance = NormalizedSquaredEuclideanDistance(data)
        normalized_squared_euclidean_distance.process()
        result = normalized_squared_euclidean_distance.get_result()
        self.assertEquals(1.0 / 4, result)

        data = [(1, 1, 4, 6, 1200, 3, 2, 3, 2, 8), (2, 1, 5, 6, 1300, 3, 2, 5, 3, 8)]
        normalized_squared_euclidean_distance = NormalizedSquaredEuclideanDistance(data)
        normalized_squared_euclidean_distance.process()
        result = normalized_squared_euclidean_distance.get_result()
        self.assertEquals(0.001589630279970944, result)

        data = [(3, 1), (4, 1)]
        normalized_squared_euclidean_distance = NormalizedSquaredEuclideanDistance(data)
        normalized_squared_euclidean_distance.process()
        result = normalized_squared_euclidean_distance.get_result()
        self.assertEquals(0.038461538461538464, result)

        data = [[3], [4]]
        normalized_squared_euclidean_distance = NormalizedSquaredEuclideanDistance(data)
        with self.assertRaises(ZeroDivisionError) as context:
            normalized_squared_euclidean_distance.process()
        self.assertEqual('float division by zero',
                         context.exception.message)

        data = [[3], [4, 5, 6]]
        normalized_squared_euclidean_distance = NormalizedSquaredEuclideanDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            normalized_squared_euclidean_distance.process()
        self.assertEqual('You cant calculate Normalized Squared Euclidean distance of array has different sizes.',
                         context.exception.message)

        data = [["a"], [4]]
        normalized_squared_euclidean_distance = NormalizedSquaredEuclideanDistance(data)
        with self.assertRaises(TypeError) as context:
            normalized_squared_euclidean_distance.process()
        self.assertEqual("unsupported operand type(s) for +: 'int' and 'str'",
                         context.exception.message)

        data = []
        normalized_squared_euclidean_distance = NormalizedSquaredEuclideanDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            normalized_squared_euclidean_distance.process()
        self.assertEqual('You must enter two array to find Normalized Squared Euclidean distance.',
                         context.exception.message)
        test_logger.debug("NormalizedSquaredEuclideanDistanceTest - test_algorithm Ends")