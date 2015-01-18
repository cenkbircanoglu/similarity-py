# coding=utf-8
from unittest import TestCase

from apps.measure.numerical_data.correlation_distance import CorrelationDistance
from tests import test_logger


__author__ = 'cenk'


class CorrelationDistanceTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("CorrelationDistanceTest - test_algorithm Starts")
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
        self.assertEqual('You cant calculate Correlation distance of array has different sizes.',
                         context.exception.message)

        data = [["a"], [4]]
        correlation_distance = CorrelationDistance(data)
        with self.assertRaises(TypeError) as context:
            correlation_distance.process()
        self.assertEqual("unsupported operand type(s) for +: 'int' and 'str'",
                         context.exception.message)

        data = []
        correlation_distance = CorrelationDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            correlation_distance.process()
        self.assertEqual('You must enter two array to find Correlation distance.',
                         context.exception.message)

        test_logger.debug("CorrelationDistanceTest - test_algorithm Ends")