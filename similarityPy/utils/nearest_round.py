__author__ = 'cenk'


def nearest_round(number, denary=5):
    step = 10 ** denary
    return float(round(number * step)) / step