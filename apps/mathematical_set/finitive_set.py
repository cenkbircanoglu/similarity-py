__author__ = 'cenk'


class FinitiveMatSet(object):
    def __init__(self, function, arguments, name):
        self.function = function
        self.arguments = arguments
        self.elements = self.set_elements(function=function, arguments=self.unify_elements(arguments))
        self.name = name
        self.size = len(self.elements)

    def __str__(self):
        return self.name

    def unify_elements(self, elements):
        unified_elements = []
        for element in elements:
            if element not in unified_elements:
                unified_elements.append(element)
        return unified_elements

    def set_elements(self, function, arguments):
        elements = arguments
        if function:
            if function.is_valid():
                elements = map(function.to_function(), arguments)
        return elements


    def is_empty(self):
        boolean = True
        if len(self.arguments) > 0:
            boolean = False
        return boolean







