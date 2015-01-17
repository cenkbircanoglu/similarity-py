# coding=utf-8
from unittest import TestCase

from apps.distances.numerical_data.cosine_distance import CosineDistance


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