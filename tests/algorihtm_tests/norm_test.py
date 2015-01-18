# coding=utf-8
from unittest import TestCase
import math

from apps.algorithms.norm import Norm
from tests import test_logger


__author__ = 'cenk'


class NormTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("NormTest - test_algorithm Starts")
        data = [1, -2]
        norm = Norm.calculate(data)
        result = math.sqrt(5)
        self.assertEquals(result, norm)

        data = [1, 2, 3, 4]
        norm = Norm.calculate(data)
        self.assertEquals(5.477225575051661, norm)

        data = (5, 6, 7, 8)
        norm = Norm.calculate(data)
        self.assertEquals(13.19090595827292, norm)

        data = [3, 1, 4, 1]
        norm = Norm.calculate(data)
        self.assertEquals(5.196152422706632, norm)

        data = [3, 1, 5, 5, 5, 3]
        norm = Norm.calculate(data)
        self.assertEquals(9.695359714832659, norm)

        data = [3]
        norm = Norm.calculate(data)
        self.assertEquals(3.0, norm)

        data = [[3], [4, 5, 6]]
        with self.assertRaises(TypeError) as context:
            norm = Norm.calculate(data)
        self.assertEqual('float() argument must be a string or a number',
                         context.exception.message)

        data = [["a"], [4]]
        with self.assertRaises(TypeError) as context:
            norm = Norm.calculate(data)
        self.assertEqual("float() argument must be a string or a number",
                         context.exception.message)
        test_logger.debug("NormTest - test_algorithm Ends")
