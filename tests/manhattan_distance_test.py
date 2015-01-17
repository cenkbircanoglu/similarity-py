# coding=utf-8
from unittest import TestCase

from apps.distances.manhattan_distance import ManhattanDistance


__author__ = 'cenk'


class ManhattanDistanceTest(TestCase):
    def test_algorithm(self):
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
        self.assertEqual('You cant calculate euclidean distance of array has different sizes.',
                         context.exception.message)

        data = [["a"], [4]]
        manhattan_distance = ManhattanDistance(data)
        with self.assertRaises(TypeError) as context:
            manhattan_distance.process()
        self.assertEqual("unsupported operand type(s) for -: 'int' and 'str'",
                         context.exception.message)