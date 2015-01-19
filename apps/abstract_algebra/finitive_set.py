__author__ = 'cenk'


class FinitiveMatSet(object):
    def __init__(self, custom_f, data, name):
        self._func = custom_f
        self._data = self.__unify_elements(data)
        self._elements = []
        self._name = name

    def get_size(self):
        return len(self._elements)

    def __str__(self):
        return self._name

    def __unify_elements(self, elements):
        unified_elements = []
        for element in elements:
            if element not in unified_elements:
                unified_elements.append(element)
        return unified_elements

    def get_elements(self):
        return self._elements

    def process(self):
        elements = []
        if self._func:
            elements = map(self._func, self._data)
        self._elements = elements

    def get_name(self):
        return self._name






