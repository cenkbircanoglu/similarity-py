__author__ = 'cenk'


class Median:
    def __init__(self):
        self.data = []

    def calculate(self, data, is_tuple=False, index=None):
        if is_tuple:
            self.data = sorted([obj[index] for obj in data])
        else:
            self.data = sorted(data)

        return self.__algorithm()

    def __algorithm(self):
        data_length = len(self.data)
        index = (data_length + 1) / 2
        if data_length % 2 == 0:
            index = (data_length / 2 + (data_length + 1) / 2) / 2
        try:
            return float(self.data[index - 1])
        except:
            raise