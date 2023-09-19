class CellException(Exception):
    pass


class CellIntegerException(CellException):
    def __str__(self):
        return 'значение выходит за допустимый диапазон'


class CellFloatException(CellException):
    def __str__(self):
        return 'значение выходит за допустимый диапазон'


class CellStringException(CellException):
    def __str__(self):
        return 'длина строки выходит за допустимый диапазон'


class CellInteger:
    def __init__(self, min_value, max_value, value=None):
        self._min_value = min_value
        self._max_value = max_value
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not self._min_value <= value <= self._max_value:
            raise CellIntegerException
        self._value = value


class CellFloat:
    def __init__(self, min_value, max_value, value=None):
        self._min_value = min_value
        self._max_value = max_value
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not self._min_value <= value <= self._max_value:
            raise CellFloatException
        self._value = value


class CellString:
    def __init__(self, min_length, max_length, value=None):
        self._min_length = min_length
        self._max_length = max_length
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not self._min_length <= value <= self._max_length:
            raise CellFloatException
        self._value = value


class TupleData:
    def __init__(self, *args):
        self.list = []
        for arg in args:
            if not isinstance(arg, (CellInteger, CellFloat, CellString)):
                raise CellException
            self.list.append(arg)

