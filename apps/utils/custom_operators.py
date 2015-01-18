__author__ = 'cenk'


def true_false(a, b):
    return a and not b


def false_true(a, b):
    return true_false(b, a)