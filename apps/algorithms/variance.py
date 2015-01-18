from apps.algorithms.mean import Mean

from apps.algorithms.sum_formula import SumFormula


__author__ = 'cenk'


class Variance:
    def __init__(self):
        self._data = []
        self._n = 0

    def calculate(self, data, is_tuple=False, index=None):
        if is_tuple:
            self._data = sorted([obj[index] for obj in data])
        else:
            self._data = sorted(data)
        self._n = len(self._data)
        return self.__algorithm()


    def __algorithm(self):
        try:
            mean = Mean()
            mean_value = mean.calculate(self._data)
            values = map(lambda x: (float(x) - mean_value), self._data)
            sum_formula = SumFormula()
            sum_of_powers = sum_formula.calculate(values, power=2)

            result = sum_of_powers / (self._n - 1)
            return round(result, 4)
        except:
            print ""