# coding=utf-8
import math

__author__ = 'cenk'


class Norm:
    @staticmethod
    def calculate(data):
        try:
            return math.sqrt(sum(float(c) ** 2 for c in data))
        except:
            raise