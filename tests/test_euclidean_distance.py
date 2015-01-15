from unittest import TestCase

from apps.distances.euclidean_distance import EuclideanDistance


__author__ = 'cenk'


class EuclideanDistanceTest(TestCase):
    def test_algorithm(self):
        data = [(1, 2, 3, 4), (1, 2, 3, 6)]

        euclidean_distance = EuclideanDistance(data)
        euclidean_distance.process()
        result = euclidean_distance.get_result()

        print result