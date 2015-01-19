from .two_math_set_comparence import TwoMathSetComparence

__author__ = 'cenk'


class MultipleMathSetComparence(object):
    @staticmethod
    def get_longest_sets(list_of_sets):
        longest_set_length = 0
        longest_set = []
        for math_set in list_of_sets:
            length_of_set = len(math_set.elements)
            if length_of_set > longest_set_length:
                longest_set_length = length_of_set
                longest_set = [math_set]
            elif length_of_set == longest_set_length:
                longest_set.append(math_set)
        return longest_set


    @classmethod
    def get_universal_set(self, list_of_sets):
        universal_set = None
        longest_sets = self.get_longest_sets(list_of_sets)
        for longest_set in longest_sets:
            if False not in map(lambda x: TwoMathSetComparence().is_subset(longest_set, x),
                                list_of_sets):
                universal_set = longest_set

        return universal_set

    @classmethod
    def has_universal_set(self, list_of_sets):
        boolean = False
        longest_sets = self.get_longest_sets(list_of_sets)
        for longest_set in longest_sets:
            if False not in map(lambda x: TwoMathSetComparence().is_subset(longest_set.elements, x),
                                list_of_sets.elements):
                boolean = True

        return boolean
