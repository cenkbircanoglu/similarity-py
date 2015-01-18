from unittest import TestCase

from apps.algorithms.variance import Variance
from tests import test_logger


__author__ = 'cenk'


class VarianceTest(TestCase):
    def setUp(self):
        pass

    def test_algorithm_with_list(self):
        test_logger.debug("VarianceTest - test_algorithm_with_list Starts")
        variance = Variance()
        data_list = [1, 2, 3, 4, 5]
        self.assertEquals(2.5, variance.calculate(data_list))
        data_list = [1, 2, 3, 4]
        self.assertEquals(1.6667, variance.calculate(data_list))
        data_list = []
        with self.assertRaises(ZeroDivisionError) as context:
            variance.calculate(data_list)
        self.assertEqual("integer division or modulo by zero",
                         context.exception.message)
        test_logger.debug("VarianceTest - test_algorithm_with_list Ends")

    def test_algorithm_with_tuple(self):
        test_logger.debug("VarianceTest - test_algorithm_with_tuple Starts")
        variance = Variance()
        data_list = [("a", 1), ("b", 2), ("c", 3), ( "d", 4), ("e", 5)]
        self.assertEquals(2.5, variance.calculate(data_list, is_tuple=True, index=1))

        data_list = [("a", "a", 1), ("b", "b", 2), ("c", "c", 3), ("d", "d", 4), ("e", "e", 5)]
        self.assertEquals(2.5, variance.calculate(data_list, is_tuple=True, index=2))

        data_list = [("a", "a", 1), ("b", "b", 2), ("c", "c", 3), ("d", "d", 4)]
        self.assertEquals(1.6667, variance.calculate(data_list, is_tuple=True, index=2))
        test_logger.debug("VarianceTest - test_algorithm_with_tuple Ends")