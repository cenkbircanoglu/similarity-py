from unittest import TestCase

from similarityPy.derivate.function_derivate import FunctionDerivate
from tests import test_logger


__author__ = 'cenk'


class FunctionDerivateTest(TestCase):
    def setUp(self):
        pass

    def test_algorithm(self):
        test_logger.debug("FunctionDerivateTest - test_algorithm Starts")

        def g(x):
            return x * x * x

        dg = FunctionDerivate.calculate(g)
        self.assertEqual(27.0, dg(3))

        data = [1, 2, 3, 4, 5]
        dg = FunctionDerivate.calculate(data)

        self.assertEqual(184.0, dg(3))

        self.assertEqual(20.0, dg(1))

        self.assertEqual(4.0, dg(0))

        test_logger.debug("FunctionDerivateTest - test_algorithm Ends")