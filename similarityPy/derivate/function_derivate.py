from similarityPy.derivate.derivate import Derivate
from similarityPy.utils.nearest_round import nearest_round

__author__ = 'cenk'


class FunctionDerivate(Derivate):
    variable = "x"

    def _algorithm(self):
        """Computes the numerical derivative of a function."""
        if hasattr(self, '_data'):
            self._turn_data_to_function()
        if hasattr(self, '_function'):
            def df(x, h=0.1e-5):
                return nearest_round((self._function(x + h / 2) - self._function(x - h / 2)) / h)

            self._result = df

    def _turn_data_to_function(self):

        x_length = len(self._data) - 1

        def f(x):
            equation = ""
            for (i, val) in enumerate(self._data):
                equation += str(val)
                if x_length - i > 0:
                    equation += "*" + self.variable
                if x_length - i > 1:
                    equation += "**" + str(x_length - i) + "+ "
                if x_length - i == 1:
                    equation += "+ "
            return eval(equation)

        self._function = f

    def _result_to_equation(self):
        pass