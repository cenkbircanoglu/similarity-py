from unittest import TestCase

from apps.algorithms.standart_deviation import StandartDeviation


__author__ = 'cenk'


class StandartDeviationTest(TestCase):
    def setUp(self):
        pass

    def test_algorithm_with_list(self):
        standart_deviation = StandartDeviation()
        data_list = [1, 2, 3, 4, 5]
        self.assertEquals(1.5811, standart_deviation.calculate(data_list))
        data_list = [1, 2, 3, 4]
        self.assertEquals(1.291, standart_deviation.calculate(data_list))

    def test_algorithm_with_tuple(self):
        standart_deviation = StandartDeviation()
        data_list = [("a", 1), ("b", 2), ("c", 3), ( "d", 4), ("e", 5)]
        self.assertEquals(1.5811, standart_deviation.calculate(data_list, is_tuple=True, index=1))

        data_list = [("a", "a", 1), ("b", "b", 2), ("c", "c", 3), ("d", "d", 4), ("e", "e", 5)]
        self.assertEquals(1.5811, standart_deviation.calculate(data_list, is_tuple=True, index=2))

        data_list = [("a", "a", 1), ("b", "b", 2), ("c", "c", 3), ("d", "d", 4)]
        self.assertEquals(1.291, standart_deviation.calculate(data_list, is_tuple=True, index=2))