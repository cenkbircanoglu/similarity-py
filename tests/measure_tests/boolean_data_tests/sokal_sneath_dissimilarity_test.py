# coding=utf-8
from unittest import TestCase

from apps.measure.boolean_data.sokal_sneath_dissimilarity import SokalSneathDissimilarity

from tests import test_logger


__author__ = 'cenk'


class SokalSneathDissimilarityTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("SokalSneathDissimilarityTest - test_algorithm Starts")
        data = [[1, 0, 1, 1, 0], [1, 1, 0, 1, 1]]
        sokal_sneath_dissimilarity = SokalSneathDissimilarity(data)
        sokal_sneath_dissimilarity.process()
        result = sokal_sneath_dissimilarity.get_result()
        self.assertEquals(0.75, result)

        data = [[True, False, True], [True, True, False]]
        sokal_sneath_dissimilarity = SokalSneathDissimilarity(data)
        sokal_sneath_dissimilarity.process()
        result = sokal_sneath_dissimilarity.get_result()
        self.assertEquals(0.8, result)

        data = [[1, 1, 1, 1], [1, 1, 1, 1]]
        sokal_sneath_dissimilarity = SokalSneathDissimilarity(data)
        sokal_sneath_dissimilarity.process()
        result = sokal_sneath_dissimilarity.get_result()
        self.assertEquals(0.0, result)

        data = [[0, 0, 0, 0], [1, 1, 1, 1]]
        sokal_sneath_dissimilarity = SokalSneathDissimilarity(data)
        sokal_sneath_dissimilarity.process()
        result = sokal_sneath_dissimilarity.get_result()
        self.assertEquals(1.0, result)

        data = [[3], [4, 5, 6]]
        sokal_sneath_dissimilarity = SokalSneathDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            sokal_sneath_dissimilarity.process()
        self.assertEqual('You cant calculate Sokal Sneath dissimilarity of array has different sizes.',
                         context.exception.message)

        data = [[], []]
        sokal_sneath_dissimilarity = SokalSneathDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            sokal_sneath_dissimilarity.process()
        self.assertEqual('float division by zero',
                         context.exception.message)
        data = []
        sokal_sneath_dissimilarity = SokalSneathDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            sokal_sneath_dissimilarity.process()
        self.assertEqual('You must enter two array to find squared euclidean distance.',
                         context.exception.message)
        test_logger.debug("SokalSneathDissimilarityTest - test_algorithm Ends")
