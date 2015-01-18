# coding=utf-8
from unittest import TestCase

from apps.measure.string_data.needleman_wunsch_similarity import NeedlemanWunschSimilarity
from tests import test_logger


__author__ = 'cenk'

## TODO
class NeedlemanWunschSimilarityTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("NeedlemanWunschSimilarityTest - test_algorithm Starts")

        test_logger.debug("THIS IS NOT IMPLEMENTED")
        # data = ["123", "246"]
        # needleman_wunsch_similarity = NeedlemanWunschSimilarity(data)
        # needleman_wunsch_similarity.process()
        # result = needleman_wunsch_similarity.get_result()
        # self.assertEquals(3, result)
        #
        # data = ["bccbbcb", "ccbbccb"]
        # needleman_wunsch_similarity = NeedlemanWunschSimilarity(data)
        # needleman_wunsch_similarity.process()
        # result = needleman_wunsch_similarity.get_result()
        # self.assertEquals(3, result)
        #
        # data = [[0, 1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1, 0]]
        # needleman_wunsch_similarity = NeedlemanWunschSimilarity(data)
        # needleman_wunsch_similarity.process()
        # result = needleman_wunsch_similarity.get_result()
        # self.assertEquals(3, result)
        #
        # data = ["123", "123"]
        # needleman_wunsch_similarity = NeedlemanWunschSimilarity(data)
        # needleman_wunsch_similarity.process()
        # result = needleman_wunsch_similarity.get_result()
        # self.assertEquals(0, result)
        #
        # data = ["abcde", "ABCDE"]
        # needleman_wunsch_similarity = NeedlemanWunschSimilarity(data)
        # needleman_wunsch_similarity.process()
        # result = needleman_wunsch_similarity.get_result()
        # self.assertEquals(0, result)
        #
        # data = ["abcde", "ABCDf"]
        # needleman_wunsch_similarity = NeedlemanWunschSimilarity(data)
        # needleman_wunsch_similarity.process()
        # result = needleman_wunsch_similarity.get_result()
        # self.assertEquals(1, result)
        #
        # data = [[3], [4]]
        # needleman_wunsch_similarity = NeedlemanWunschSimilarity(data)
        # needleman_wunsch_similarity.process()
        # result = needleman_wunsch_similarity.get_result()
        # self.assertEquals(1, result)
        #
        # data = [["a"], [4]]
        # needleman_wunsch_similarity = NeedlemanWunschSimilarity(data)
        # needleman_wunsch_similarity.process()
        # result = needleman_wunsch_similarity.get_result()
        # self.assertEquals(1, result)
        #
        # data = ["10011", "00101"]
        # needleman_wunsch_similarity = NeedlemanWunschSimilarity(data)
        # needleman_wunsch_similarity.process()
        # result = needleman_wunsch_similarity.get_result()
        # self.assertEquals(3, result)
        #
        # data = [[3], [4, 5, 6]]
        # needleman_wunsch_similarity = NeedlemanWunschSimilarity(data)
        # with self.assertRaises(ArithmeticError) as context:
        #     needleman_wunsch_similarity.process()
        # self.assertEqual('You cant calculate hamming distance of array has different sizes.',
        #                  context.exception.message)
        test_logger.debug("NeedlemanWunschSimilarityTest - test_algorithm Ends")
