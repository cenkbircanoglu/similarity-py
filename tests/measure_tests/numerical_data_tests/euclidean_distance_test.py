# coding=utf-8
from unittest import TestCase

from apps.measure.numerical_data.euclidean_distance import EuclideanDistance
from tests import test_logger


__author__ = 'cenk'


class EuclideanDistanceTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("EuclideanDistanceTest - test_algorithm Starts")
        data = [(1, 2, 3, 4), (1, 2, 3, 6)]
        euclidean_distance = EuclideanDistance(data)
        euclidean_distance.process()
        result = euclidean_distance.get_result()
        self.assertEquals(2.0, result)

        data = [(3, 1), (4, 1)]
        euclidean_distance = EuclideanDistance(data)
        euclidean_distance.process()
        result = euclidean_distance.get_result()
        self.assertEquals(1.0, result)

        data = [[3], [4]]
        euclidean_distance = EuclideanDistance(data)
        euclidean_distance.process()
        result = euclidean_distance.get_result()
        self.assertEquals(1.0, result)

        data = [[3], [4, 5, 6]]
        euclidean_distance = EuclideanDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            euclidean_distance.process()
        self.assertEqual('You cant calculate Euclidean distance of array has different sizes.',
                         context.exception.message)

        data = [["a"], [4]]
        euclidean_distance = EuclideanDistance(data)
        with self.assertRaises(TypeError) as context:
            euclidean_distance.process()
        self.assertEqual("unsupported operand type(s) for -: 'int' and 'str'",
                         context.exception.message)

        data = []
        euclidean_distance = EuclideanDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            euclidean_distance.process()
        self.assertEqual('You must enter two array to find Euclidean distance.',
                         context.exception.message)

        test_logger.debug("EuclideanDistanceTest - test_algorithm Ends")
        #
        #
        # def test_stress(self):
        #
        # ## Ten thousand data test
        #     data = [[], []]
        #     a = 0
        #     limit = 1000
        #     while a < limit:
        #         data[0].append(random.randint(0, 10000))
        #         data[1].append(random.randint(0, 10000))
        #         a += 1
        #     t0 = time.clock()
        #
        #     euclidean_distance = EuclideanDistance(data)
        #     euclidean_distance.process()
        #     result = euclidean_distance.get_result()
        #     print result
        #     time_delta = time.clock() - t0
        #     expected_delta = 0.0006
        #     self.assertTrue(expected_delta > time_delta)
        #     print time_delta
        #
        #     ## One hundred thousand data test
        #     data = [[], []]
        #     a = 0
        #     while a < limit * 100:
        #         data[0].append(random.randint(0, 10000))
        #         data[1].append(random.randint(0, 10000))
        #         a += 1
        #     t0 = time.clock()
        #
        #     euclidean_distance = EuclideanDistance(data)
        #     euclidean_distance.process()
        #     result = euclidean_distance.get_result()
        #     print result
        #     time_delta = time.clock() - t0
        #     self.assertTrue(expected_delta * 100 > time_delta)
        #     print time_delta
        #
        #     ## One million data test
        #     data = [[], []]
        #     a = 0
        #     while a < limit * 1000:
        #         data[0].append(random.randint(0, 10000))
        #         data[1].append(random.randint(0, 10000))
        #         a += 1
        #     t0 = time.clock()
        #
        #     euclidean_distance = EuclideanDistance(data)
        #     euclidean_distance.process()
        #     result = euclidean_distance.get_result()
        #     print result
        #     time_delta = time.clock() - t0
        #     self.assertTrue(expected_delta * 1000 > time_delta)
        #     print time_delta
        #
        #
        #     ## Ten million data test
        #     data = [[], []]
        #     a = 0
        #     while a < limit * 10000:
        #         data[0].append(random.randint(0, 10000))
        #         data[1].append(random.randint(0, 10000))
        #         a += 1
        #     t0 = time.clock()
        #
        #     euclidean_distance = EuclideanDistance(data)
        #     euclidean_distance.process()
        #     result = euclidean_distance.get_result()
        #     print result
        #     time_delta = time.clock() - t0
        #     print expected_delta * 10000
        #     self.assertTrue(expected_delta * 10000 > time_delta)
        #     print time_delta
        #
