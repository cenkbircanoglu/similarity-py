# coding=utf-8
from functools import partial

from mathematical_set.finitive_set import FinitiveMatSet
from mathematical_set.math_function import MathFunction
from operator import is_not


__author__ = 'cenk'


class NaturalNumbers(FinitiveMatSet):
    # TODO infinite values didn't implement.
    def __init__(self, till=None, start=None):
        name = str(till) + ' - ' + str(start) if start else str(till)
        arguments = []
        for i in reversed(xrange(till)):
            if i is not start:
                arguments.append(i)
        super(NaturalNumbers, self).__init__(MathFunction(lambda x: x), arguments=arguments, name=name)

    @staticmethod
    def zero():
        return NaturalNumbers(0)

    def is_set_odd(self):
        if len(self.elements) == 0:
            return None
        if (len(self.elements) % 2) is 0:
            return False
        return True

    def is_set_even(self):
        if len(self.elements) == 0:
            return None
        return not self.is_set_odd()

    def is_odd(self, number):
        if number == 0 or (number % 2) is 0:
            return False
        return True

    def is_even(self, number):
        if self.is_odd(number) or number == 0:
            return False
        return True

    def get_if_odd(self, number):
        if self.is_odd(number):
            return number

    def get_if_even(self, number):
        if self.is_even(number):
            return number

    def get_odd_numbers(self):
        odd_number_elements = []
        for element in self.elements:
            odd_number_elements.append(self.get_if_odd(element))
        odd_number_elements = filter(partial(is_not, None), odd_number_elements)
        return odd_number_elements

    def get_even_numbers(self):
        even_number_elements = []
        for element in self.elements:
            even_number_elements.append(self.get_if_even(element))
        even_number_elements = filter(partial(is_not, None), even_number_elements)
        return even_number_elements

