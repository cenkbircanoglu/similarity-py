from unittest import TestCase

from apps.abstract_algebra.finitive_set import FinitiveMatSet
from apps.abstract_algebra.mf import mf

from tests import test_logger


__author__ = 'cenk'


class FinitiveSetTest(TestCase):
    def setUp(self):
        pass

    def test_algorithm(self):
        test_logger.debug("FinitiveSetTest - test_algorithm Starts")

        set1 = FinitiveMatSet(mf(lambda x: x ** 2), [1, 2, 3, 4, 5], 'A')
        set1.process()
        elements = set1.get_elements()
        size = set1.get_size()
        name = set1.get_name()
        expected_elements = [1, 4, 9, 16, 25]
        expected_size = 5

        self.assertEquals("A", name)
        self.assertEquals(expected_elements, elements)
        self.assertEquals(expected_size, size)

        set2 = FinitiveMatSet(mf(lambda x: x ** 2), [1, 2, 3, 4, 5], 'B')
        set2.process()
        elements = set2.get_elements()
        size = set2.get_size()
        name = set2.get_name()
        expected_elements = [1, 4, 9, 16, 25]
        expected_size = 5

        self.assertEquals("B", name)
        self.assertEquals(expected_elements, elements)
        self.assertEquals(expected_size, size)

        set3 = FinitiveMatSet(mf(lambda x: x), set2.get_elements(), 'C')
        set3.process()
        elements = set3.get_elements()
        size = set3.get_size()
        name = set3.get_name()
        expected_elements = [1, 4, 9, 16, 25]
        expected_size = 5

        self.assertEquals("C", name)
        self.assertEquals(expected_elements, elements)
        self.assertEquals(expected_size, size)

        set4 = FinitiveMatSet(mf(lambda x: x + 5), set2.get_elements(), 'D')
        set4.process()
        elements = set4.get_elements()
        size = set4.get_size()
        name = set4.get_name()
        expected_elements = [6, 9, 14, 21, 30]
        expected_size = 5

        self.assertEquals("D", name)
        self.assertEquals(expected_elements, elements)
        self.assertEquals(expected_size, size)

        set5 = FinitiveMatSet(mf(lambda x: x - 5), set2.get_elements(), 'E')
        set5.process()
        elements = set5.get_elements()
        size = set5.get_size()
        name = set5.get_name()
        expected_elements = [-4, -1, 4, 11, 20]
        expected_size = 5

        self.assertEquals("E", name)
        self.assertEquals(expected_elements, elements)
        self.assertEquals(expected_size, size)

        set6 = FinitiveMatSet(mf(lambda x: x),
                              [1, 2, 3, 4, 5, 9, 16, 25, 6, 4, 11, 20, 14, 21, 30, 7, 8, 9, 10, -4, -3, -2, -1, 0], 'F')
        set6.process()
        elements = set6.get_elements()
        size = set6.get_size()
        name = set6.get_name()
        expected_elements = [1, 2, 3, 4, 5, 9, 16, 25, 6, 11, 20, 14, 21, 30, 7, 8, 10, -4, -3, -2, -1, 0]
        expected_size = 22

        self.assertEquals("F", name)
        self.assertEquals(expected_elements, elements)
        self.assertEquals(expected_size, size)

        set7 = FinitiveMatSet(mf(lambda x: x), [1, 1, 1, 2, 5], 'G')

        elements = set7.get_elements()
        size = set7.get_size()
        name = set7.get_name()
        expected_elements = [1, 2, 5]
        expected_size = 3

        self.assertEquals("G", name)
        self.assertEquals(expected_elements, elements)
        self.assertEquals(expected_size, size)

        set8 = FinitiveMatSet(mf(), [1, 1, 1, 2, 5], 'G')
        set8.process()
        elements = set8.get_elements()
        size = set8.get_size()
        name = set8.get_name()
        expected_elements = [1, 2, 5]
        expected_size = 3

        self.assertEquals("G", name)
        self.assertEquals(expected_elements, elements)
        self.assertEquals(expected_size, size)

        test_logger.debug("FinitiveSetTest - test_algorithm Ends")