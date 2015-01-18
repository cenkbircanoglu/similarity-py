# coding=utf-8
from unittest import TestCase

from apps.measure.string_data.edit_distance import SimilarityMeasure

from tests import test_logger


__author__ = 'cenk'


class SimilarityMeasureTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("SimilarityMeasureTest - test_algorithm Starts")

        data = []
        similarity_measure = SimilarityMeasure(data)
        with self.assertRaises(NotImplementedError) as context:
            similarity_measure.process()
        self.assertEqual('Subclasses should implement this!',
                         context.exception.message)

        data = ""
        with self.assertRaises(TypeError) as context:
            similarity_measure = SimilarityMeasure(data)
        self.assertEqual('You must initialize array.',
                         context.exception.message)

        test_logger.debug("SimilarityMeasureTest - test_algorithm Ends")