from unittest import TestCase
import time

from apps.algorithms.mean import Mean


__author__ = 'cenk'


class MeanTest(TestCase):
    def setUp(self):
        pass

    def test_algorithm_with_list(self):
        mean = Mean()
        data_list = [1, 2, 3, 4, 5]
        self.assertEquals(3, mean.calculate(data_list))
        data_list = [1, 2, 3, 4]
        self.assertEquals(2.5, mean.calculate(data_list))

    def test_algorithm_with_tuple(self):
        mean = Mean()
        data_list = [("a", 1), ("b", 2), ("c", 3), ( "d", 4), ("e", 5)]
        self.assertEquals(3, mean.calculate(data_list, is_tuple=True, index=1))

        data_list = [("a", "a", 1), ("b", "b", 2), ("c", "c", 3), ("d", "d", 4), ("e", "e", 5)]
        self.assertEquals(3.0, mean.calculate(data_list, is_tuple=True, index=2))
