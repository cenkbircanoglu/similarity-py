# coding=utf-8
__author__ = 'cenk'


class Distance:
    def __init__(self, data):

        if type(data) is list:
            self._data = data
            self._result = None
        else:
            raise TypeError("You must initialize array.")

    def _algorithm(self):
        raise NotImplementedError("Subclasses should implement this!")

    def process(self):
        self._algorithm()

    def clear_data(self):
        pass

    def get_result(self):
        return self._result