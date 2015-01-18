__author__ = 'cenk'


class MathFunction(object):
    def __init__(self, function_string):
        self.function_string = function_string

    def is_valid(self):
        # TODO
        return True

    def function_string_to_function(self):
        function = lambda x: x
        if self.function_string:
            function = self.function_string
        return function

    def to_function(self):
        return self.function_string_to_function()