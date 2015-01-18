# coding=utf-8

from apps.measure.similarity_measure import SimilarityMeasure
from apps.measure.similarity_measure_type import SimilarityMeasureType


__author__ = 'cenk'

# TODO

class SmithWatermanSimilarity(SimilarityMeasure):
    similarity_measure_type = SimilarityMeasureType.DISTANCE_ABBR

    def _algorithm(self):
        raise NotImplementedError("Subclasses should implement this!")