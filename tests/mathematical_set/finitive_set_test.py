from unittest import TestCase

from apps.mathematical_set.finitive_set import FinitiveMatSet
from apps.mathematical_set.mf import mf

from tests import test_logger


__author__ = 'cenk'


class FinitiveSetTest(TestCase):
    def setUp(self):
        pass

    def test_algorithm(self):
        test_logger.debug("FinitiveSetTest - test_algorithm Starts")

        kume1 = FinitiveMatSet(mf(lambda x: x ** 2), [1, 2, 3, 4, 5], 'A')
        kume2 = FinitiveMatSet(mf(lambda x: x ** 2), [1, 2, 3, 4, 5], 'B')
        kume3 = FinitiveMatSet(mf(lambda x: x), kume2.elements, 'C')
        kume4 = FinitiveMatSet(mf(lambda x: x + 5), kume1.elements, 'D')
        kume5 = FinitiveMatSet(mf(lambda x: x - 5), kume1.elements, 'E')
        kume6 = FinitiveMatSet(mf(lambda x: x),
                               [1, 2, 3, 4, 5, 9, 16, 25, 6, 4, 11, 20, 14, 21, 30, 7, 8, 9, 10, -4, -3, -2, -1, 0],
                               'F')
        kume7 = FinitiveMatSet(mf(lambda x: x), [1, 1, 1, 2, 5], 'G')

        kume8 = FinitiveMatSet(mf(), [1, 1, 1, 2, 5], 'G')

        print  'RESULT 1: %s' % kume1, kume1.elements, kume1.size
        print  'RESULT 2: %s' % kume2, kume2.elements, kume2.size
        print  'RESULT 3: %s' % kume3, kume3.elements, kume3.size
        print  'RESULT 4: %s' % kume4, kume4.elements, kume4.size
        print  'RESULT 5: %s' % kume5, kume5.elements, kume5.size
        print  'RESULT 6: %s' % kume6, kume6.elements, kume6.size
        print  'RESULT 7: %s' % kume7, kume7.elements, kume7.size
        test_logger.debug("FinitiveSetTest - test_algorithm Ends")