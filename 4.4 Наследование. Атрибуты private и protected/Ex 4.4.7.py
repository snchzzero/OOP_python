class Furniture:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def __verify_name(self, name):
        if isinstance(name, str):
            return True
        else:
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, weight):
        if isinstance(weight, (int, float)) and weight > 0:
            return True
        else:
            raise TypeError('вес должен быть положительным числом')

    def __setattr__(self, key, value):
        if key == '_name':
            if self.__verify_name(value):
                self.__dict__[key] = value
        elif key == '_weight':
            if self.__verify_weight(value):
                self.__dict__[key] = value
        else:
            self.__dict__[key] = value


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return tuple(self.__dict__.values())



# obj = Furniture('шкаф-купе', 56)
# obj._name = 'irfsad'
# obj._weight = 2
# obj._weight = -2

cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
print(chair.get_attrs())
print(cl.get_attrs())