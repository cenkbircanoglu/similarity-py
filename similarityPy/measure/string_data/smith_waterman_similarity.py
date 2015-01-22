# coding=utf-8
"""
Created on 18 January 2014
@author: Cenk Bircanoglu
"""

from similarityPy.measure.similarity_measure import SimilarityMeasure
from similarityPy.measure.similarity_measure_type import SimilarityMeasureType



# TODO

class SmithWatermanSimilarity(SimilarityMeasure):
    similarity_measure_type = SimilarityMeasureType.DISTANCE_ABBR

    def _algorithm(self):
        raise NotImplementedError("Subclasses should implement this!")