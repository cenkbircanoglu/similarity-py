# coding=utf-8
from unittest import TestCase

from apps.measure.numerical_data.chessboard_distance import ChessBoardDistance
from tests import test_logger


__author__ = 'cenk'


class ChessBoardDistanceTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("ChessBoardDistanceTest - test_algorithm Starts")
        data = [(1, 2, 3, 4), (1, 2, 3, 8)]
        chessboard_distance = ChessBoardDistance(data)
        chessboard_distance.process()
        result = chessboard_distance.get_result()
        self.assertEquals(4.0, result)

        data = [(3, 1), (4, 1)]
        chessboard_distance = ChessBoardDistance(data)
        chessboard_distance.process()
        result = chessboard_distance.get_result()
        self.assertEquals(1.0, result)

        data = [(-3, 1), (4, 1)]
        chessboard_distance = ChessBoardDistance(data)
        chessboard_distance.process()
        result = chessboard_distance.get_result()
        self.assertEquals(7.0, result)

        data = [[3], [4]]
        chessboard_distance = ChessBoardDistance(data)
        chessboard_distance.process()
        result = chessboard_distance.get_result()
        self.assertEquals(1.0, result)

        data = [[3], [4, 5, 6]]
        chessboard_distance = ChessBoardDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            chessboard_distance.process()
        self.assertEqual('You cant calculate Chess Board distance of array has different sizes.',
                         context.exception.message)

        data = [["a"], [4]]
        chessboard_distance = ChessBoardDistance(data)
        with self.assertRaises(TypeError) as context:
            chessboard_distance.process()
        self.assertEqual("unsupported operand type(s) for -: 'int' and 'str'",
                         context.exception.message)

        data = []
        chessboard_distance = ChessBoardDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            chessboard_distance.process()
        self.assertEqual('You must enter two array to find Chess Board distance.',
                         context.exception.message)

        test_logger.debug("ChessBoardDistanceTest - test_algorithm Ends")