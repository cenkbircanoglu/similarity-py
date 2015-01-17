# coding=utf-8
from unittest import TestCase

from apps.distances.boolean_data.rogers_tanimoto_dissimilarity import RogersTanimotoDissimilarity
from tests import test_logger


__author__ = 'cenk'


class RogersTanimotoDissimilarityTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("RogersTanimotoDissimilarityTest - test_algorithm Starts")
        data = ["10110", "11011"]
        rogers_tanimoto_dissimilarity = RogersTanimotoDissimilarity(data)
        rogers_tanimoto_dissimilarity.process()
        result = rogers_tanimoto_dissimilarity.get_result()
        self.assertEquals(3.0 / 4, result)

        data = ["123", "123"]
        rogers_tanimoto_dissimilarity = RogersTanimotoDissimilarity(data)
        rogers_tanimoto_dissimilarity.process()
        result = rogers_tanimoto_dissimilarity.get_result()
        self.assertEquals(0.0, result)

        data = ["abcde", "ABCDE"]
        rogers_tanimoto_dissimilarity = RogersTanimotoDissimilarity(data)
        rogers_tanimoto_dissimilarity.process()
        result = rogers_tanimoto_dissimilarity.get_result()
        self.assertEquals(0, result)

        data = ["abcde", "ABCDf"]
        rogers_tanimoto_dissimilarity = RogersTanimotoDissimilarity(data)
        rogers_tanimoto_dissimilarity.process()
        result = rogers_tanimoto_dissimilarity.get_result()
        self.assertEquals(0.3333333333333333, result)

        data = [[3], [4]]
        rogers_tanimoto_dissimilarity = RogersTanimotoDissimilarity(data)
        rogers_tanimoto_dissimilarity.process()
        result = rogers_tanimoto_dissimilarity.get_result()
        self.assertEquals(1, result)

        data = [["a"], [4]]
        rogers_tanimoto_dissimilarity = RogersTanimotoDissimilarity(data)
        rogers_tanimoto_dissimilarity.process()
        result = rogers_tanimoto_dissimilarity.get_result()
        self.assertEquals(1, result)

        data = ["10011", "00101"]
        rogers_tanimoto_dissimilarity = RogersTanimotoDissimilarity(data)
        rogers_tanimoto_dissimilarity.process()
        result = rogers_tanimoto_dissimilarity.get_result()
        self.assertEquals(0.75, result)

        data = [(True, False, True), (True, True, False)]
        rogers_tanimoto_dissimilarity = RogersTanimotoDissimilarity(data)
        rogers_tanimoto_dissimilarity.process()
        result = rogers_tanimoto_dissimilarity.get_result()
        self.assertEquals(0.8, result)

        data = [[3], [4, 5, 6]]
        rogers_tanimoto_dissimilarity = RogersTanimotoDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            rogers_tanimoto_dissimilarity.process()
        self.assertEqual('You cant calculate matching dissimilarity of array has different sizes.',
                         context.exception.message)

        test_logger.debug("RogersTanimotoDissimilarityTest - test_algorithm Ends")
