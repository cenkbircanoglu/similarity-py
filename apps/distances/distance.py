__author__ = 'cenk'


class Distance:
    def __init__(self, data):
        self._data = data
        self._result = None

    def _algorithm(self):
        raise NotImplementedError("Subclasses should implement this!")

    def process(self):
        self._algorithm()

    def clear_data(self):
        pass

    def get_result(self):
        return self._result