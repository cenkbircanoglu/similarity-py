from unittest import TestCase

from apps.abstract_algebra.finitive_set import FinitiveMatSet
from apps.abstract_algebra.mf import mf
from apps.abstract_algebra.multiple_set_comparison import MultipleSetComparison

from tests import test_logger


__author__ = 'cenk'


class MultipleSetComparisonTest(TestCase):
    def setUp(self):
        self.set1 = FinitiveMatSet(mf(lambda x: x ** 2), [1, 2, 3, 4, 5], 'A')
        self.set2 = FinitiveMatSet(mf(lambda x: x ** 2), [1, 2, 3, 4, 5], 'B')
        self.set3 = FinitiveMatSet(mf(lambda x: x), self.set2.get_elements(), 'C')
        self.set4 = FinitiveMatSet(mf(lambda x: x + 5), self.set2.get_elements(), 'D')
        self.set5 = FinitiveMatSet(mf(lambda x: x - 5), self.set2.get_elements(), 'E')
        self.set6 = FinitiveMatSet(mf(lambda x: x),
                                   [1, 2, 3, 4, 5, 9, 16, 25, 6, 4, 11, 20, 14, 21, 30, 7, 8, 9, 10, -4, -3, -2, -1, 0],
                                   'F')
        self.set7 = FinitiveMatSet(mf(lambda x: x), [1, 1, 1, 2, 5], 'G')
        self.set8 = FinitiveMatSet(mf(), [1, 1, 1, 2, 5], 'G')

    def test_longest_set(self):
        test_logger.debug("MultipleSetComparisonTest - test_longest_set Starts")

        longest_set = MultipleSetComparison.get_longest_sets(
            [self.set1, self.set2, self.set3, self.set4, self.set5, self.set6, self.set7, self.set8])
        expected_elements = [1, 2, 3, 4, 5, 9, 16, 25, 6, 11, 20, 14, 21, 30, 7, 8, 10, -4, -3, -2, -1, 0]
        self.assertEquals(expected_elements, longest_set.get_elements())

        longest_set = MultipleSetComparison.get_longest_sets([self.set1, self.set2, self.set3, self.set4, self.set5])
        expected_elements = [1, 4, 9, 16, 25]
        self.assertEquals(expected_elements, longest_set.get_elements())

        test_logger.debug("MultipleSetComparisonTest - test_longest_set Ends")

    def test_universal_set(self):
        test_logger.debug("MultipleSetComparisonTest - test_universal_set Starts")
        universal_set = MultipleSetComparison.universal_set(
            [self.set1, self.set2, self.set3, self.set4, self.set5, self.set6, self.set7, self.set8])
        expected_elements = [1, 4, 9, 16, 25, 6, 14, 21, 30, -4, -1, 11, 20, 2, 3, 5, 7, 8, 10, -3, -2, 0]
        self.assertEquals(expected_elements, universal_set.get_elements())

        universal_set = MultipleSetComparison.universal_set([self.set1, self.set2, self.set3, self.set4, self.set5])
        expected_elements = [1, 4, 9, 16, 25, 6, 14, 21, 30, -4, -1, 11, 20]
        self.assertEquals(expected_elements, universal_set.get_elements())
        test_logger.debug("MultipleSetComparisonTest - test_universal_set Ends")