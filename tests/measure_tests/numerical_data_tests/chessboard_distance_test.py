# coding=utf-8
from unittest import TestCase

from apps.measure.numerical_data.chessboard_distance import ChessBoardDistance
from tests import test_logger


__author__ = 'cenk'


class ChessBoardDistanceTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("ChessBoardDistanceTest - test_algorithm Starts")
        data = [(1, 2, 3, 4), (1, 2, 3, 8)]
        euclidean_distance = ChessBoardDistance(data)
        euclidean_distance.process()
        result = euclidean_distance.get_result()
        self.assertEquals(4.0, result)

        data = [(3, 1), (4, 1)]
        euclidean_distance = ChessBoardDistance(data)
        euclidean_distance.process()
        result = euclidean_distance.get_result()
        self.assertEquals(1.0, result)

        data = [(-3, 1), (4, 1)]
        euclidean_distance = ChessBoardDistance(data)
        euclidean_distance.process()
        result = euclidean_distance.get_result()
        self.assertEquals(7.0, result)

        data = [[3], [4]]
        euclidean_distance = ChessBoardDistance(data)
        euclidean_distance.process()
        result = euclidean_distance.get_result()
        self.assertEquals(1.0, result)

        data = [[3], [4, 5, 6]]
        euclidean_distance = ChessBoardDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            euclidean_distance.process()
        self.assertEqual('You cant calculate euclidean distance of array has different sizes.',
                         context.exception.message)

        data = [["a"], [4]]
        euclidean_distance = ChessBoardDistance(data)
        with self.assertRaises(TypeError) as context:
            euclidean_distance.process()
        self.assertEqual("unsupported operand type(s) for -: 'int' and 'str'",
                         context.exception.message)
        test_logger.debug("ChessBoardDistanceTest - test_algorithm Ends")