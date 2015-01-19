from unittest import TestCase

from apps.abstract_algebra.mf import mf
from tests import test_logger


__author__ = 'cenk'


class MfTest(TestCase):
    def setUp(self):
        pass

    def test_algorithm(self):
        test_logger.debug("MfTest - test_algorithm Starts")
        my_func = mf(lambda x: x * x)
        result = map(my_func, [1, 2, 34, 5, 6])
        expected_result = [1, 4, 1156, 25, 36]
        self.assertEquals(expected_result, result)

        my_func = mf(lambda x: x)
        result = map(my_func, [1, 2, 34, 5, 6])
        expected_result = [1, 2, 34, 5, 6]
        self.assertEquals(expected_result, result)

        my_func = mf()
        result = map(my_func, [1, 2, 34, 5, 6])
        expected_result = [1, 2, 34, 5, 6]
        self.assertEquals(expected_result, result)

        test_logger.debug("MfTest - test_algorithm Ends")
