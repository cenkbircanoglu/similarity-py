from unittest import TestCase

from apps.algorithms.find_nearest import FindNearest
from apps.measure.numerical_data.normalized_squared_euclidean_distance import NormalizedSquaredEuclideanDistance
from tests import test_logger


__author__ = 'cenk'


class FindNearestTest(TestCase):
    def setUp(self):
        pass

    def test_normalized_squared_euclidean_distance(self):
        test_logger.debug("FindNearestTest - test_normalized_squared_euclidean_distance Starts")

        points = [(1, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 1), (1, 0, 1, 1, 1, 0)]
        point = (1, 0, 0, 0, 0, 0)
        find_nearest = FindNearest(points, point, NormalizedSquaredEuclideanDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals((1, 0, 1, 0, 1, 0), nearest)

        points = [(1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1), (1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1)]
        point = (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1)
        find_nearest = FindNearest(points, point, NormalizedSquaredEuclideanDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals((0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1), nearest)

        points = [(2, 3), (3, 4), (4, 5)]
        point = (0, 1)
        find_nearest = FindNearest(points, point, NormalizedSquaredEuclideanDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals((2, 3), nearest)

        points = [(2, 3), (3, 4), (4, 5)]
        point = (3, 3)
        find_nearest = FindNearest(points, point, NormalizedSquaredEuclideanDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals((2, 3), nearest)

        points = [(2, 3), (3, 4), (4, 5)]
        point = (3, 4)
        find_nearest = FindNearest(points, point, NormalizedSquaredEuclideanDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals((2, 3), nearest)

        test_logger.debug("FindNearestTest - test_normalized_squared_euclidean_distance Ends")

    def test_normalized_squared_euclidean_distance_multiple(self):
        test_logger.debug("FindNearestTest - test_normalized_squared_euclidean_distance_multiple Starts")

        points = [(1, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 1), (1, 0, 1, 1, 1, 0)]
        point = (1, 0, 0, 0, 0, 0)
        find_nearest = FindNearest(points, point, NormalizedSquaredEuclideanDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([(1, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 1)], nearest)

        points = [(1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1), (1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1)]
        point = (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1)
        find_nearest = FindNearest(points, point, NormalizedSquaredEuclideanDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1), (1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)]
                          , nearest)

        points = [(2, 3), (3, 4), (4, 5)]
        point = (0, 1)
        find_nearest = FindNearest(points, point, NormalizedSquaredEuclideanDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([(2, 3), (2, 3)], nearest)

        points = [(2, 3), (3, 4), (4, 5)]
        point = (3, 3)
        find_nearest = FindNearest(points, point, NormalizedSquaredEuclideanDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([(2, 3), (2, 3)], nearest)

        points = [(2, 3), (3, 4), (4, 5)]
        point = (3, 4)
        find_nearest = FindNearest(points, point, NormalizedSquaredEuclideanDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([(2, 3), (2, 3)], nearest)

        test_logger.debug("FindNearestTest - test_normalized_squared_euclidean_distance_multiple Ends")
