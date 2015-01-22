# coding=utf-8
"""
Created on 18 January 2014
@author: Cenk Bircanoglu
"""


def true_false(a, b):
    return a and not b


def false_true(a, b):
    return true_false(b, a)