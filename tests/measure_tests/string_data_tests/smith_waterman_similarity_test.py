# coding=utf-8
from unittest import TestCase

from tests import test_logger


__author__ = 'cenk'

## TODO
class SmithWatermanSimilarityTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("SmithWatermanSimilarityTest - test_algorithm Starts")
        test_logger.debug("THIS IS NOT IMPLEMENTED")
        # data = ["123", "246"]
        # smith_waterman_similarity = SmithWatermanSimilarity(data)
        # smith_waterman_similarity.process()
        # result = smith_waterman_similarity.get_result()
        # self.assertEquals(3, result)
        #
        # data = ["bccbbcb", "ccbbccb"]
        # smith_waterman_similarity = SmithWatermanSimilarity(data)
        # smith_waterman_similarity.process()
        # result = smith_waterman_similarity.get_result()
        # self.assertEquals(3, result)
        #
        # data = [[0, 1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1, 0]]
        # smith_waterman_similarity = SmithWatermanSimilarity(data)
        # smith_waterman_similarity.process()
        # result = smith_waterman_similarity.get_result()
        # self.assertEquals(3, result)
        #
        # data = ["123", "123"]
        # smith_waterman_similarity = SmithWatermanSimilarity(data)
        # smith_waterman_similarity.process()
        # result = smith_waterman_similarity.get_result()
        # self.assertEquals(0, result)
        #
        # data = ["abcde", "ABCDE"]
        # smith_waterman_similarity = SmithWatermanSimilarity(data)
        # smith_waterman_similarity.process()
        # result = smith_waterman_similarity.get_result()
        # self.assertEquals(0, result)
        #
        # data = ["abcde", "ABCDf"]
        # smith_waterman_similarity = SmithWatermanSimilarity(data)
        # smith_waterman_similarity.process()
        # result = smith_waterman_similarity.get_result()
        # self.assertEquals(1, result)
        #
        # data = [[3], [4]]
        # smith_waterman_similarity = SmithWatermanSimilarity(data)
        # smith_waterman_similarity.process()
        # result = smith_waterman_similarity.get_result()
        # self.assertEquals(1, result)
        #
        # data = [["a"], [4]]
        # smith_waterman_similarity = SmithWatermanSimilarity(data)
        # smith_waterman_similarity.process()
        # result = smith_waterman_similarity.get_result()
        # self.assertEquals(1, result)
        #
        # data = ["10011", "00101"]
        # smith_waterman_similarity = SmithWatermanSimilarity(data)
        # smith_waterman_similarity.process()
        # result = smith_waterman_similarity.get_result()
        # self.assertEquals(3, result)
        #
        # data = [[3], [4, 5, 6]]
        # smith_waterman_similarity = SmithWatermanSimilarity(data)
        # with self.assertRaises(ArithmeticError) as context:
        # smith_waterman_similarity.process()
        # self.assertEqual('You cant calculate hamming distance of array has different sizes.',
        # context.exception.message)
        test_logger.debug("SmithWatermanSimilarityTest - test_algorithm Ends")
