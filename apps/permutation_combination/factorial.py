__author__ = 'cenk'


class Factorial(object):
    def __init__(self, number):
        if number == 0:
            self.result = 1
        if number > 0:
            self.result = number * Factorial(number - 1).result

    def __str__(self):
        return str(self.result)

