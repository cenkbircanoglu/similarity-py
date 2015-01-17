# coding=utf-8
import random
from unittest import TestCase
import time

from apps.distances.cosine_distance import CosineDistance


__author__ = 'cenk'


class CosineDistanceTest(TestCase):
    def test_algorithm(self):
        data = [(1, 2, 3), (3, 5, 7)]
        cosine_distance = CosineDistance(data)
        cosine_distance.process()
        result = cosine_distance.get_result()
        self.assertEquals(0.002585096956942312, result)

        data = [(1, 2, 3, 4), (1, 2, 3, 6)]
        cosine_distance = CosineDistance(data)
        cosine_distance.process()
        result = cosine_distance.get_result()
        self.assertEquals(0.018844218960787695, result)

        data = [(3, 1), (4, 1)]
        cosine_distance = CosineDistance(data)
        cosine_distance.process()
        result = cosine_distance.get_result()
        self.assertEquals(0.002945514498418511, result)

        data = [[3], [4]]
        cosine_distance = CosineDistance(data)
        cosine_distance.process()
        result = cosine_distance.get_result()
        self.assertEquals(0.0, result)

        data = [[3, 4], [6, 8]]
        cosine_distance = CosineDistance(data)
        cosine_distance.process()
        result = cosine_distance.get_result()
        self.assertEquals(0.0, result)

        data = [[3], [4, 5, 6]]
        cosine_distance = CosineDistance(data)
        with self.assertRaises(ArithmeticError) as context:
            cosine_distance.process()
        self.assertEqual('You cant calculate euclidean distance of array has different sizes.',
                         context.exception.message)

        data = [["a"], [4]]
        cosine_distance = CosineDistance(data)
        with self.assertRaises(TypeError) as context:
            cosine_distance.process()
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

        cosine_distance = CosineDistance(data)
        cosine_distance.process()
        result = cosine_distance.get_result()
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

        cosine_distance = CosineDistance(data)
        cosine_distance.process()
        result = cosine_distance.get_result()
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

        cosine_distance = CosineDistance(data)
        cosine_distance.process()
        result = cosine_distance.get_result()
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

        cosine_distance = CosineDistance(data)
        cosine_distance.process()
        result = cosine_distance.get_result()
        print result
        time_delta = time.clock() - t0
        print expected_delta * 10000
        self.assertTrue(expected_delta * 10000 > time_delta)
        print time_delta

