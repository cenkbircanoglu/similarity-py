from unittest import TestCase

from apps.algorithms.find_nearest import FindNearest
from apps.measure.string_data.hamming_distance import HammingDistance
from tests import test_logger


__author__ = 'cenk'


class FindNearestTest(TestCase):
    def setUp(self):
        pass

    def test_hamming_distance(self):
        test_logger.debug("FindNearestTest - test_hamming_distance Starts")

        points = ["abcdef", "abcefg", "abcdeg"]
        point = "abcdef"
        find_nearest = FindNearest(points, point, HammingDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals("abcdef", nearest)

        points = ["abcXdef", "abcXefg", "abcXdeg"]
        point = "abcdefg"
        find_nearest = FindNearest(points, point, HammingDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals("abcXefg", nearest)

        points = ["abcXdef", "abcXefg", "abcXdeg"]
        point = "1234567"
        find_nearest = FindNearest(points, point, HammingDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals("abcXdef", nearest)

        points = ["abcXdef", "abcXefg", "abcXdeg"]
        point = "123456 "
        find_nearest = FindNearest(points, point, HammingDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals("abcXdef", nearest)

        test_logger.debug("FindNearestTest - test_hamming_distance Ends")

    def test_hamming_distance_multiple(self):
        test_logger.debug("FindNearestTest - test_hamming_distance_multiple Starts")

        points = ["abcdef", "abcefg", "abcdeg"]
        point = "abcdef"
        find_nearest = FindNearest(points, point, HammingDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals(['abcdef', 'abcdeg'], nearest)

        points = ["abcXdef", "abcXefg", "abcXdeg"]
        point = "abcdefg"
        find_nearest = FindNearest(points, point, HammingDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals(['abcXefg', 'abcXdeg'], nearest)

        points = ["abcXdef", "abcXefg", "abcXdeg"]
        point = "1234567"
        find_nearest = FindNearest(points, point, HammingDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals(['abcXdef', 'abcXdef'], nearest)

        points = ["abcXdef", "abcXefg", "abcXdeg"]
        point = "123456 "
        find_nearest = FindNearest(points, point, HammingDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals(['abcXdef', 'abcXdef'], nearest)

        test_logger.debug("FindNearestTest - test_hamming_distance_multiple Ends")