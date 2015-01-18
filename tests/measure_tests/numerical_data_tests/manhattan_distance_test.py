# coding=utf-8
from unittest import TestCase

from apps.measure.numerical_data.manhattan_distance import ManhattanDistance
from tests import test_logger


__author__ = 'cenk'


class ManhattanDistanceTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("ManhattanDistanceTest - test_algorithm Starts")
        data = [(1, 2, 3, 4), (1, 2, 3, 6)]
        manhattan_distance = ManhattanDistance(data)
        manhattan_distance.process()
        result = manhattan_distance.get_result()
        self.assertEquals(2.0, result)

        data = [(1, 2, 3, 4), (5, 6, 7, 8)]
        manhattan_distance = ManhattanDistance(data)
        manhattan_distance.process()
        result = manhattan_distance.get_result()
        self.assertEquals(16.0, result)

        data = [(3, 1), (4, 1)]
        manhattan_distance = ManhattanDistance(data)
        manhattan_distance.process()
        result = manhattan_distance.get_result()
        self.assertEquals(1.0, result)

        data = [(3, 1, 5), (5, 5, 3)]
        manhattan_distance = ManhattanDistance(data)
        manhattan_distance.process()
        result = manhattan_distance.get_result()
        self.assertEquals(8.0, result)

        data = [[3], [4]]
        manhattan_distance = ManhattanDistance(data)
        manhattan_distance.process()
        result = manhattan_distance.get_result()
        self.assertEquals(1.0, result)

        data = [[3], [4, 5, 6]]
        manhattan_distance = ManhattanDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            manhattan_distance.process()
        self.assertEqual('You cant calculate Manhattan distance of array has different sizes.',
                         context.exception.message)

        data = [["a"], [4]]
        manhattan_distance = ManhattanDistance(data)
        with self.assertRaises(TypeError) as context:
            manhattan_distance.process()
        self.assertEqual("unsupported operand type(s) for -: 'int' and 'str'",
                         context.exception.message)

        data = []
        manhattan_distance = ManhattanDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            manhattan_distance.process()
        self.assertEqual('You must enter two array to find Manhattan distance.',
                         context.exception.message)

        test_logger.debug("ManhattanDistanceTest - test_algorithm Ends")