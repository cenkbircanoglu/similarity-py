# coding=utf-8
from unittest import TestCase

from apps.measure.numerical_data.bray_curtis_distance import BrayCurtisDistance
from tests import test_logger


__author__ = 'cenk'


class BrayCurtisDistanceTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("BrayCurtisDistanceTest - test_algorithm Starts")
        data = [(1, 2, 3), (2, 4, 6)]
        bray_curtis_distance = BrayCurtisDistance(data)
        bray_curtis_distance.process()
        result = bray_curtis_distance.get_result()
        expected_result = float(1.0 / 3.0)
        self.assertEquals(expected_result, result)

        data = [(3, 1), (4, 1)]
        bray_curtis_distance = BrayCurtisDistance(data)
        bray_curtis_distance.process()
        result = bray_curtis_distance.get_result()
        expected_result = float(1.0 / 9.0)
        self.assertEquals(expected_result, result)

        data = [[3], [4]]
        bray_curtis_distance = BrayCurtisDistance(data)
        bray_curtis_distance.process()
        result = bray_curtis_distance.get_result()
        expected_result = 0.14285714285714285
        self.assertEquals(expected_result, result)

        data = [[3], [4, 5, 6]]
        bray_curtis_distance = BrayCurtisDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            bray_curtis_distance.process()
        self.assertEqual('You cant calculate Bray Curtis distance of array has different sizes.',
                         context.exception.message)

        data = [["a"], [4]]
        bray_curtis_distance = BrayCurtisDistance(data)
        with self.assertRaises(TypeError) as context:
            bray_curtis_distance.process()
        self.assertEqual("unsupported operand type(s) for -: 'int' and 'str'",
                         context.exception.message)

        data = []
        bray_curtis_distance = BrayCurtisDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            bray_curtis_distance.process()
        self.assertEqual('You must enter two array to find Bray Curtis distance.',
                         context.exception.message)

        test_logger.debug("BrayCurtisDistanceTest - test_algorithm Ends")