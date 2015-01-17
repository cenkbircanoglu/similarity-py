from unittest import TestCase

from apps.algorithms.median import Median


__author__ = 'cenk'


class MedianTest(TestCase):
    def setUp(self):
        pass

    def test_algorithm_with_list(self):
        median = Median()
        data_list = [1, 2, 3, 4, 5]
        self.assertEquals(3, median.calculate(data_list))
        data_list = [1, 2, 3, 4]
        self.assertEquals(2, median.calculate(data_list))

    def test_algorithm_with_tuple(self):
        median = Median()
        data_list = [("a", 1), ("b", 2), ("c", 3), ( "d", 4), ("e", 5)]
        self.assertEquals(3, median.calculate(data_list, is_tuple=True, index=1))

        data_list = [("a", "a", 1), ("b", "b", 2), ("c", "c", 3), ("d", "d", 4), ("e", "e", 5)]
        self.assertEquals(3.0, median.calculate(data_list, is_tuple=True, index=2))

        data_list = [("a", "a", 1), ("b", "b", 2), ("c", "c", 3), ("d", "d", 4)]
        self.assertEquals(2.0, median.calculate(data_list, is_tuple=True, index=2))