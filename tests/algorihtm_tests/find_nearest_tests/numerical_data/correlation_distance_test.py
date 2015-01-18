from unittest import TestCase

from apps.algorithms.find_nearest import FindNearest
from apps.measure.numerical_data.correlation_distance import CorrelationDistance
from tests import test_logger


__author__ = 'cenk'


class FindNearestTest(TestCase):
    def setUp(self):
        pass

    def test_correlation_distance(self):
        test_logger.debug("FindNearestTest - test_correlation_distance Starts")

        points = [(2, 3), (3, 4), (4, 5)]
        point = (2, 1)
        find_nearest = FindNearest(points, point, CorrelationDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals((2, 3), nearest)

        points = [(2, 3), (3, 4), (4, 5)]
        point = (3, 2)
        find_nearest = FindNearest(points, point, CorrelationDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals((2, 3), nearest)

        points = [(2, 3), (3, 4), (4, 5)]
        point = (3, 4)
        find_nearest = FindNearest(points, point, CorrelationDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals((2, 3), nearest)

        test_logger.debug("FindNearestTest - test_correlation_distance Ends")

    def test_correlation_distance_multiple(self):
        test_logger.debug("FindNearestTest - test_correlation_distance_multiple Starts")

        points = [(2, 3), (4, 6), (6, 5)]
        point = (2, 1)
        find_nearest = FindNearest(points, point, CorrelationDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([(6, 5), (2, 3)], nearest)

        points = [(2, 3), (4, 6), (6, 5)]
        point = (3, 2)
        find_nearest = FindNearest(points, point, CorrelationDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([(6, 5), (2, 3)], nearest)

        points = [(2, 3), (4, 6), (6, 5)]
        point = (3, 1)
        find_nearest = FindNearest(points, point, CorrelationDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([(6, 5), (2, 3)], nearest)

        test_logger.debug("FindNearestTest - test_correlation_distance_multiple Ends")