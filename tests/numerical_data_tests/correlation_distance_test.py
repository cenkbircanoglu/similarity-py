# coding=utf-8
from unittest import TestCase

from apps.distances.numerical_data.correlation_distance import CorrelationDistance


__author__ = 'cenk'


class CorrelationDistanceTest(TestCase):
    def test_algorithm(self):
        data = [(1, 2, 3), (3, 5, 10)]
        correlation_distance = CorrelationDistance(data)
        correlation_distance.process()
        result = correlation_distance.get_result()
        self.assertEquals(0.029274656605848937, result)

        data = [(1, 2, 3, 4), (1, 2, 3, 6)]
        correlation_distance = CorrelationDistance(data)
        correlation_distance.process()
        result = correlation_distance.get_result()
        self.assertEquals(0.0438171125324851, result)

        data = [(3, 1), (4, 1)]
        correlation_distance = CorrelationDistance(data)
        correlation_distance.process()
        result = correlation_distance.get_result()
        self.assertEquals(0.0, result)

        data = [[3], [4]]
        correlation_distance = CorrelationDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            correlation_distance.process()
        self.assertEqual('float division by zero', context.exception.message)

        data = [[3], [4, 5, 6]]
        correlation_distance = CorrelationDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            correlation_distance.process()
        self.assertEqual('You cant calculate euclidean distance of array has different sizes.',
                         context.exception.message)

        data = [["a"], [4]]
        correlation_distance = CorrelationDistance(data)
        with self.assertRaises(TypeError) as context:
            correlation_distance.process()
        self.assertEqual("unsupported operand type(s) for +: 'int' and 'str'",
                         context.exception.message)