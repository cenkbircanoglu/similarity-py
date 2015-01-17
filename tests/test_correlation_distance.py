# coding=utf-8
import random
from unittest import TestCase
import time

from apps.distances.correlation_distance import CorrelationDistance


__author__ = 'cenk'


class CorrelationDistanceTest(TestCase):
    def test_algorithm(self):

        data = [(1, 2, 3), (3, 5, 10)]
        correlation_distance = CorrelationDistance(data)
        correlation_distance.process()
        result = correlation_distance.get_result()
        self.assertEquals(0.029274656605848937, result)

        data = [(1, 2, 3, 4), (1, 2, 3, 6)]
        correlation_distance = CorrelationDistance(data)
        correlation_distance.process()
        result = correlation_distance.get_result()
        self.assertEquals(0.0438171125324851, result)

        data = [(3, 1), (4, 1)]
        correlation_distance = CorrelationDistance(data)
        correlation_distance.process()
        result = correlation_distance.get_result()
        self.assertEquals(0.0, result)

        data = [[3], [4]]
        correlation_distance = CorrelationDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            correlation_distance.process()
        self.assertEqual('float division by zero', context.exception.message)

        data = [[3], [4, 5, 6]]
        correlation_distance = CorrelationDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            correlation_distance.process()
        self.assertEqual('You cant calculate euclidean distance of array has different sizes.',
                         context.exception.message)

        data = [["a"], [4]]
        correlation_distance = CorrelationDistance(data)
        with self.assertRaises(TypeError) as context:
            correlation_distance.process()
        self.assertEqual("unsupported operand type(s) for +: 'int' and 'str'",
                         context.exception.message)


    def test_stress(self):

        ## Ten thousand data test
        data = [[], []]
        a = 0
        limit = 1000
        while a < limit:
            data[0].append(random.randint(0, 10000))
            data[1].append(random.randint(0, 10000))
            a += 1
        t0 = time.clock()

        correlation_distance = CorrelationDistance(data)
        correlation_distance.process()
        result = correlation_distance.get_result()
        print result
        time_delta = time.clock() - t0
        expected_delta = 0.0006
        self.assertTrue(expected_delta > time_delta)
        print time_delta

        ## One hundred thousand data test
        data = [[], []]
        a = 0
        while a < limit * 100:
            data[0].append(random.randint(0, 10000))
            data[1].append(random.randint(0, 10000))
            a += 1
        t0 = time.clock()

        correlation_distance = CorrelationDistance(data)
        correlation_distance.process()
        result = correlation_distance.get_result()
        print result
        time_delta = time.clock() - t0
        self.assertTrue(expected_delta * 100 > time_delta)
        print time_delta

        ## One million data test
        data = [[], []]
        a = 0
        while a < limit * 1000:
            data[0].append(random.randint(0, 10000))
            data[1].append(random.randint(0, 10000))
            a += 1
        t0 = time.clock()

        correlation_distance = CorrelationDistance(data)
        correlation_distance.process()
        result = correlation_distance.get_result()
        print result
        time_delta = time.clock() - t0
        self.assertTrue(expected_delta * 1000 > time_delta)
        print time_delta


        ## Ten million data test
        data = [[], []]
        a = 0
        while a < limit * 10000:
            data[0].append(random.randint(0, 10000))
            data[1].append(random.randint(0, 10000))
            a += 1
        t0 = time.clock()

        correlation_distance = CorrelationDistance(data)
        correlation_distance.process()
        result = correlation_distance.get_result()
        print result
        time_delta = time.clock() - t0
        print expected_delta * 10000
        self.assertTrue(expected_delta * 10000 > time_delta)
        print time_delta

