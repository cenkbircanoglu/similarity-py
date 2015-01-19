# coding=utf-8
from functools import partial
from operator import is_not

from .finitive_set import FinitiveMatSet


__author__ = 'cenk'


class TwoMathSetComparence(object):
    def __init__(self):
        pass

    @staticmethod
    def has_same_value(obj1, obj2):
        boolean = False
        if obj1 == obj2:
            boolean = True
        return boolean

    @staticmethod
    def has_value(obj1, obj2):
        boolean = False
        if obj2 in obj1:
            boolean = True
        return boolean

    @classmethod
    def is_identical(self, first_set, second_set):
        return self.has_same_value(first_set.elements, second_set.elements)

    @classmethod
    def is_subset(self, parent_set, child_set):
        boolean = False
        if False not in map(lambda x: self.has_value(parent_set.get_elements(), x), child_set.get_elements()):
            boolean = True

        return boolean

    @staticmethod
    def get_intersect_value(obj1, obj2):
        if obj2 in obj1:
            return obj2
        return None

    @classmethod
    def get_intersection(self, list_of_sets):
        intersection = list_of_sets[0].elements
        name = ""
        for math_set in list_of_sets:
            intersection = map(lambda x: self.get_intersect_value(intersection, x), math_set.elements)
            intersection = filter(partial(is_not, None), intersection)
            name += math_set.name + '∩'

        return FinitiveMatSet(None, intersection, name[:name.rfind('∩')])

    @classmethod
    def intersection_size(self, list_of_sets):
        intersection_set = TwoMathSetComparence().get_intersection(list_of_sets)
        return intersection_set.size

    @classmethod
    def association_size(self, list_of_sets):
        association_set = TwoMathSetComparence().get_association(list_of_sets)
        return association_set.size


    @classmethod
    def get_association(self, list_of_sets):
        association = []
        name = ""
        for math_set in list_of_sets:
            association += math_set.elements
            name += math_set.name + 'U'
        return FinitiveMatSet(None, association, name[:name.rfind('U')])

    @staticmethod
    def get_unmatch_value(value, math_set):
        if value not in math_set:
            return value

    @classmethod
    def get_difference(self, first_set, second_set):
        difference = map(lambda x: self.get_unmatch_value(x, second_set.elements), first_set.elements)
        difference = filter(partial(is_not, None), difference)
        name = first_set.name + '\\' + second_set.name
        return FinitiveMatSet(None, difference, name)

    @classmethod
    def is_disjoint_sets(self, first_set, second_set):
        boolean = False
        if True not in map(lambda x: self.has_value(first_set.elements, x), second_set.elements):
            boolean = True

        return boolean

    @classmethod
    def get_complement_set(self, math_set, universal_set):
        complement_of_set = map(lambda x: self.get_unmatch_value(x, math_set.elements), universal_set.elements)
        complement_of_set = filter(partial(is_not, None), complement_of_set)
        name = math_set.name + '\''
        return FinitiveMatSet(None, complement_of_set, name)