import types

__author__ = 'cenk'


class Derivate:
    def __init__(self, data):
        """
        :param data (list): [1,2,3,4,5]
        :return:None
        """
        if type(data) is list:
            self._data = data
        elif isinstance(data, types.FunctionType):
            self._function = data
        else:
            raise TypeError("You must initialize array.")
        self._result = []
        self._equation = None

    def _algorithm(self):
        """
        Raise NotImplementedError.
        :return:None
        """
        raise NotImplementedError("Subclasses should implement this!")

    def process(self):
        """
        Call the algorithm and calculate the distance.
        :return:None
        """
        self._algorithm()

    def get_result(self):
        """
        Get function of result.
        :return: result (list)
        """
        return self._result

    def get_equation(self):
        """
        Get function of result.
        :return: equation (str)
        """
        return self._equation

    @classmethod
    def calculate(cls, data):
        """
        This is a method that simplfy calling and accessing the result. Set data, then process and then return the result.
        :param data:
        :return: result (list)
        """
        derivate = cls(data)
        derivate.process()
        return derivate.get_result()

    def _result_to_equation(self):
        """
        Raise NotImplementedError.
        :return:None
        """
        raise NotImplementedError("Subclasses should implement this!")

    @classmethod
    def calculate_equation(cls, data):
        """
        This is a method that simplfy calling and accessing the equation version of the result.
        Set data, then process and then return the equation string.
        :param data:
        :return: equation (str)
        """
        derivate = cls(data)
        derivate.process()
        derivate._result_to_equation()
        return derivate.get_equation()