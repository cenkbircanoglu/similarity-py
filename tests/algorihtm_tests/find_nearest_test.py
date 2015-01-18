from unittest import TestCase

from apps.algorithms.find_nearest import FindNearest

from tests import test_logger


__author__ = 'cenk'


class FindNearestTest(TestCase):
    def setUp(self):
        pass

    def test_algorithm(self):
        test_logger.debug("FindNearestTest - test_algorithm Starts")

        points = "abcdef"
        point = "abcdefg"
        with self.assertRaises(TypeError) as context:
            FindNearest(points, point, "")
        self.assertEqual("You must initialize array and a point",
                         context.exception.message)

        test_logger.debug("FindNearestTest - test_algorithm Starts")