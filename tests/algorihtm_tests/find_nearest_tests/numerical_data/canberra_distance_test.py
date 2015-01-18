from unittest import TestCase

from apps.algorithms.find_nearest import FindNearest
from apps.measure.numerical_data.canberra_distance import CanberraDistance
from tests import test_logger


__author__ = 'cenk'


class FindNearestTest(TestCase):
    def setUp(self):
        pass

    def test_canberra_distance(self):
        test_logger.debug("FindNearestTest - test_canberra_distance Starts")

        points = [(2, 3), (3, 4), (4, 5)]
        point = (0, 0)
        find_nearest = FindNearest(points, point, CanberraDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals((2, 3), nearest)

        points = [(2, 3), (3, 4), (4, 5)]
        point = (3, 3)
        find_nearest = FindNearest(points, point, CanberraDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals((2, 3), nearest)

        points = [(2, 3), (3, 4), (4, 5)]
        point = (3, 4)
        find_nearest = FindNearest(points, point, CanberraDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals((2, 3), nearest)

        points = [[1], [5], [10]]
        point = [8]
        find_nearest = FindNearest(points, point, CanberraDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([1], nearest)

        points = [[1], [5], [10]]
        point = [17]
        find_nearest = FindNearest(points, point, CanberraDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([1], nearest)

        test_logger.debug("FindNearestTest - test_canberra_distance Ends")

    def test_canberra_distance_multiple(self):
        test_logger.debug("FindNearestTest - test_canberra_distance_multiple Starts")

        points = [(2, 3), (3, 4), (4, 5)]
        point = (0, 0)
        find_nearest = FindNearest(points, point, CanberraDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([(2, 3), (2, 3)], nearest)

        points = [(2, 3), (3, 4), (4, 5)]
        point = (3, 3)
        find_nearest = FindNearest(points, point, CanberraDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([(2, 3), (3, 4)], nearest)

        points = [(2, 3), (3, 4), (4, 5)]
        point = (3, 4)
        find_nearest = FindNearest(points, point, CanberraDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([(2, 3), (3, 4)], nearest)

        points = [[1], [5], [10]]
        point = [8]
        find_nearest = FindNearest(points, point, CanberraDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([[1], [5]], nearest)

        points = [[1], [5], [10]]
        point = [17]
        find_nearest = FindNearest(points, point, CanberraDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([[1], [5]], nearest)

        test_logger.debug("FindNearestTest - test_canberra_distance_multiple Ends")