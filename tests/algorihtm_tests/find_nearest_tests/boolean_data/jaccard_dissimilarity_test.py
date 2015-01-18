from unittest import TestCase

from apps.algorithms.find_nearest import FindNearest
from apps.measure.boolean_data.jaccard_dissimilarity import JaccardDissimilarity
from tests import test_logger


__author__ = 'cenk'


class FindNearestTest(TestCase):
    def setUp(self):
        pass

    def test_jaccard_dissimilarity(self):
        test_logger.debug("FindNearestTest - test_jaccard_dissimilarity Starts")

        points = [(1, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 1), (1, 0, 1, 1, 1, 0)]
        point = (1, 0, 0, 0, 0, 0)
        find_nearest = FindNearest(points, point, JaccardDissimilarity)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals((1, 0, 1, 0, 1, 0), nearest)

        points = [(1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1), (1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1)]
        point = (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1)
        find_nearest = FindNearest(points, point, JaccardDissimilarity)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals((0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1), nearest)

        test_logger.debug("FindNearestTest - test_jaccard_dissimilarity Ends")

    def test_jaccard_dissimilarity_multiple(self):
        test_logger.debug("FindNearestTest - test_jaccard_dissimilarity_multiple Starts")

        points = [(1, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 1), (1, 0, 1, 1, 1, 0)]
        point = (1, 0, 0, 0, 0, 0)
        find_nearest = FindNearest(points, point, JaccardDissimilarity, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([(1, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 1)], nearest)

        points = [(1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1), (1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1)]
        point = (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1)
        find_nearest = FindNearest(points, point, JaccardDissimilarity, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals([(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1), (1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)]
                          , nearest)

        test_logger.debug("FindNearestTest - test_jaccard_dissimilarity_multiple Ends")