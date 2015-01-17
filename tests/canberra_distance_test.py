# coding=utf-8
from unittest import TestCase

from apps.distances.canberra_distance import CanberraDistance


__author__ = 'cenk'


class CanberraDistanceTest(TestCase):
    def test_algorithm(self):
        data = [(1, 2, 3), (2, 4, 6)]
        canberra_distance = CanberraDistance(data)
        canberra_distance.process()
        result = canberra_distance.get_result()
        self.assertEquals(1.0, result)

        data = [(3, 1), (4, 1)]
        canberra_distance = CanberraDistance(data)
        canberra_distance.process()
        result = canberra_distance.get_result()
        self.assertEquals(0.14285714285714285, result)

        data = [[3], [4]]
        canberra_distance = CanberraDistance(data)
        canberra_distance.process()
        result = canberra_distance.get_result()
        self.assertEquals(0.14285714285714285, result)

        data = [[3], [4, 5, 6]]
        canberra_distance = CanberraDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            canberra_distance.process()
        self.assertEqual('You cant calculate euclidean distance of array has different sizes.',
                         context.exception.message)

        data = [["a"], [4]]
        canberra_distance = CanberraDistance(data)
        with self.assertRaises(TypeError) as context:
            canberra_distance.process()
        self.assertEqual("unsupported operand type(s) for -: 'int' and 'str'",
                         context.exception.message)