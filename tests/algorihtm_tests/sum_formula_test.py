from unittest import TestCase

from apps.algorithms.sum_formula import SumFormula
from tests import test_logger


__author__ = 'cenk'


class SumFormulaTest(TestCase):
    def setUp(self):
        pass

    def test_formula(self):
        test_logger.debug("SumFormulaTest - test_formula Starts")
        sum_formula = SumFormula()
        data_list = [1, 2, 3, 4, 5]
        self.assertEquals(15, sum_formula.calculate(data_list))
        data_list = [1, 2, 3, 4]
        self.assertEquals(10, sum_formula.calculate(data_list))
        data_list = [2]
        self.assertEquals(4, sum_formula.calculate(data_list, power=2))
        data_list = [1, 2, 3, 4]
        self.assertEquals(30, sum_formula.calculate(data_list, power=2))
        test_logger.debug("SumFormulaTest - test_formula Ends")

    def test_algorithm_with_tuple(self):
        test_logger.debug("SumFormulaTest - test_algorithm_with_tuple Starts")
        sum_formula = SumFormula()
        data_list = [("a", 1), ("b", 2), ("c", 3), ( "d", 4), ("e", 5)]
        self.assertEquals(15, sum_formula.calculate(data_list, is_tuple=True, index=1))

        data_list = [("a", "a", 1), ("b", "b", 2), ("c", "c", 3), ("d", "d", 4), ("e", "e", 5)]
        self.assertEquals(15, sum_formula.calculate(data_list, is_tuple=True, index=2))

        data_list = [("a", "a", 1), ("e", "e", 5)]
        self.assertEquals(26, sum_formula.calculate(data_list, is_tuple=True, index=2, power=2))
        test_logger.debug("SumFormulaTest - test_algorithm_with_tuple Ends")