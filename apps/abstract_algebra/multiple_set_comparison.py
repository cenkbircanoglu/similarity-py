from apps.abstract_algebra.finitive_set import FinitiveMatSet
from apps.abstract_algebra.mf import mf

__author__ = 'cenk'


class MultipleSetComparison:
    @staticmethod
    def get_longest_sets(list_of_sets, k=1):
        set_elements = [set_a.get_elements() for set_a in list_of_sets]
        index = max(map(len, set_elements))
        return list_of_sets[map(len, set_elements).index(index)]


    @staticmethod
    def universal_set(list_of_sets):
        set_elements = []
        for set_a in list_of_sets:
            set_elements += set_a.get_elements()
        return FinitiveMatSet(mf(), set_elements, 'X')

