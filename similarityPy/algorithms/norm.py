# coding=utf-8
"""
Created on 18 January 2014
@author: Cenk Bircanoglu
"""
import math


class Norm:
    @staticmethod
    def calculate(data):
        try:
            return math.sqrt(sum(float(c) ** 2 for c in data))
        except:
            raise