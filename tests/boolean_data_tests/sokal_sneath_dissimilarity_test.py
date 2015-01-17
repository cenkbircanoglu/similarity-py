# coding=utf-8
from unittest import TestCase

from apps.distances.boolean_data.sokal_sneath_dissimilarity import SokalSneathDissimilarity
from tests import test_logger


__author__ = 'cenk'


class SokalSneathDissimilarityTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("SokalSneathDissimilarityTest - test_algorithm Starts")
        data = ["10110", "11011"]
        sokal_sneath_dissimilarity = SokalSneathDissimilarity(data)
        sokal_sneath_dissimilarity.process()
        result = sokal_sneath_dissimilarity.get_result()
        self.assertEquals(0.75, result)

        data = ["123", "123"]
        sokal_sneath_dissimilarity = SokalSneathDissimilarity(data)
        sokal_sneath_dissimilarity.process()
        result = sokal_sneath_dissimilarity.get_result()
        self.assertEquals(0.0, result)

        data = ["abcde", "ABCDE"]
        sokal_sneath_dissimilarity = SokalSneathDissimilarity(data)
        sokal_sneath_dissimilarity.process()
        result = sokal_sneath_dissimilarity.get_result()
        self.assertEquals(0, result)

        data = ["abcde", "ABCDf"]
        sokal_sneath_dissimilarity = SokalSneathDissimilarity(data)
        sokal_sneath_dissimilarity.process()
        result = sokal_sneath_dissimilarity.get_result()
        self.assertEquals(0.3333333333333333, result)

        data = [[3], [4]]
        sokal_sneath_dissimilarity = SokalSneathDissimilarity(data)
        sokal_sneath_dissimilarity.process()
        result = sokal_sneath_dissimilarity.get_result()
        self.assertEquals(1, result)

        data = [["a"], [4]]
        sokal_sneath_dissimilarity = SokalSneathDissimilarity(data)
        sokal_sneath_dissimilarity.process()
        result = sokal_sneath_dissimilarity.get_result()
        self.assertEquals(1, result)

        data = ["10011", "00101"]
        sokal_sneath_dissimilarity = SokalSneathDissimilarity(data)
        sokal_sneath_dissimilarity.process()
        result = sokal_sneath_dissimilarity.get_result()
        self.assertEquals(0.75, result)

        data = [(True, False, True), (True, True, False)]
        sokal_sneath_dissimilarity = SokalSneathDissimilarity(data)
        sokal_sneath_dissimilarity.process()
        result = sokal_sneath_dissimilarity.get_result()
        self.assertEquals(0.8, result)

        data = [[3], [4, 5, 6]]
        sokal_sneath_dissimilarity = SokalSneathDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            sokal_sneath_dissimilarity.process()
        self.assertEqual('You cant calculate matching dissimilarity of array has different sizes.',
                         context.exception.message)

        test_logger.debug("SokalSneathDissimilarityTest - test_algorithm Ends")
