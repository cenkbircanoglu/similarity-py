# coding=utf-8
from unittest import TestCase

from apps.measure.string_data.edit_distance import EditDistance
from tests import test_logger


__author__ = 'cenk'


class EditDistanceTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("EditDistanceTest - test_algorithm Starts")

        data = ["bccbbcb", "ccbbccb"]
        edit_distance = EditDistance(data)
        edit_distance.process()
        result = edit_distance.get_result()
        self.assertEquals(2, result)

        data = ["123", "246"]
        edit_distance = EditDistance(data)
        edit_distance.process()
        result = edit_distance.get_result()
        self.assertEquals(3, result)

        data = [[0, 1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1, 0]]
        edit_distance = EditDistance(data)
        edit_distance.process()
        result = edit_distance.get_result()
        self.assertEquals(2, result)

        data = ["123", "123"]
        edit_distance = EditDistance(data)
        edit_distance.process()
        result = edit_distance.get_result()
        self.assertEquals(0, result)

        data = ["abcde", "ABCDE"]
        edit_distance = EditDistance(data)
        edit_distance.process()
        result = edit_distance.get_result()
        self.assertEquals(0, result)

        data = ["abcde", "ABCDf"]
        edit_distance = EditDistance(data)
        edit_distance.process()
        result = edit_distance.get_result()
        self.assertEquals(1, result)

        data = [[3], [4]]
        edit_distance = EditDistance(data)
        edit_distance.process()
        result = edit_distance.get_result()
        self.assertEquals(1, result)

        data = [["a"], [4]]
        edit_distance = EditDistance(data)
        edit_distance.process()
        result = edit_distance.get_result()
        self.assertEquals(1, result)

        data = ["10011", "00101"]
        edit_distance = EditDistance(data)
        edit_distance.process()
        result = edit_distance.get_result()
        self.assertEquals(2, result)

        data = [[3], [4, 5, 6]]
        edit_distance = EditDistance(data)
        edit_distance.process()
        result = edit_distance.get_result()
        self.assertEquals(3, result)

        data = []
        edit_distance = EditDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            edit_distance.process()
        self.assertEqual('You must enter two array to find Edit distance.',
                         context.exception.message)

        test_logger.debug("EditDistanceTest - test_algorithm Ends")
