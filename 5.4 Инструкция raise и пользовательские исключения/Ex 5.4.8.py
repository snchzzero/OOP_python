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
        if not self._min_length <= len(value) <= self._max_length:
            raise CellStringException
        self._value = value


class TupleData:
    def __init__(self, *args):
        self.list = []
        for arg in args:
            if not isinstance(arg, (CellInteger, CellFloat, CellString)):
                raise CellException
            self.list.append(arg)

    def __getitem__(self, item):
        if not isinstance(item, int) or not 0 <= item <= len(self.list):
            raise IndexError
        return self.list[item].value

    def __setitem__(self, item, value):
        if not isinstance(item, int) or not 0 <= item <= len(self.list):
            raise IndexError
        self.list[item].value = value

    def __len__(self):
        return len(self.list)

    def __iter__(self):
        self.indx = 0
        return self

    def __next__(self):
        if self.indx < len(self.list):
            self.indx += 1
            return self.list[self.indx - 1].value
        else:
            raise StopIteration



ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[-1] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")

# t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))
#
# d = (1, 0, 'sergey')
# t[0] = d[0]
# t[1] = d[1]
# t[2] = d[2]
# for i, x in enumerate(t):
#     assert x == d[i], "объект класса TupleData хранит неверную информацию"
#
# assert len(t) == 3, "неверное число элементов в объекте класса TupleData"
#
# cell = CellFloat(-5, 5)
# try:
#     cell.value = -6.0
# except CellFloatException:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение CellFloatException"
#
# cell = CellInteger(-1, 7)
# try:
#     cell.value = 8
# except CellIntegerException:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение CellIntegerException"
#
# cell = CellString(5, 7)
# try:
#     cell.value = "hello world"
# except CellStringException:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение CellStringException"
#
# assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException, CellException) and issubclass(
#     CellStringException,
#     CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"
