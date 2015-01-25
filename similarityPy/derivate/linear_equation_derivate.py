from similarityPy.derivate.derivate import Derivate

__author__ = 'cenk'


class LinearEquationDerivate(Derivate):
    variable = "x"

    def _algorithm(self):
        result = []
        x_length = len(self._data) - 1
        for (i, value) in enumerate(self._data):
            if i < x_length:
                result.append((x_length - i) * value)
        self._result = result

    def _result_to_equation(self):
        equation = ""
        x_length = len(self._result) - 1
        for (i, val) in enumerate(self._result):
            equation += str(val)
            if x_length - i > 0:
                equation += "*" + self.variable
            if x_length - i > 1:
                equation += "^" + str(x_length - i) + "+ "
            if x_length - i == 1:
                equation += "+ "
        self._equation = equation
