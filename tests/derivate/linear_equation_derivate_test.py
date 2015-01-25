from unittest import TestCase

from similarityPy.derivate.linear_equation_derivate import LinearEquationDerivate

from tests import test_logger


__author__ = 'cenk'


class LinearEquationDerivateTest(TestCase):
    def setUp(self):
        pass

    def test_algorithm(self):
        test_logger.debug("LinearEquationDerivateTest - test_algorithm Starts")
        """
        This data symbolise "y=2x + 1"
        """
        data = [2, 1]
        linear_equation_derivate = LinearEquationDerivate.calculate(data)
        expected_result = [2]
        self.assertEquals(expected_result, linear_equation_derivate)

        linear_equation_derivate = LinearEquationDerivate.calculate_equation(data)
        expected_result = "2"
        self.assertEquals(expected_result, linear_equation_derivate)

        data = [3, 4, 5, 6, 2, 1]
        linear_equation_derivate = LinearEquationDerivate.calculate(data)
        expected_result = [15, 16, 15, 12, 2]
        self.assertEquals(expected_result, linear_equation_derivate)
        linear_equation_derivate = LinearEquationDerivate.calculate_equation(data)
        expected_result = "15*x^4+ 16*x^3+ 15*x^2+ 12*x+ 2"
        self.assertEquals(expected_result, linear_equation_derivate)

        test_logger.debug("LinearEquationDerivateTest - test_algorithm Ends")

        def derivative(f):
            """Computes the numerical derivative of a function."""

            def df(x, h=0.1e-5):
                return (f(x + h / 2) - f(x - h / 2) ) / h

            return df

        def g(x):
            return x * x * x

        dg = derivative(g)
        print dg(3)