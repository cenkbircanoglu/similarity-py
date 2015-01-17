# coding=utf-8

from apps.distance.distance import Distance


__author__ = 'cenk'

# TODO

class NeedlemanWunschSimilarity(Distance):
    def _algorithm(self):
        raise NotImplementedError("Subclasses should implement this!")
