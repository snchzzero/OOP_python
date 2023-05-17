class Vector:
    def __init__(self, *args):
        self.list = args

    def new_obj(self, list):
        if all([isinstance(digit, int) for digit in list]):
            return VectorInt(*list)
        else:
            return Vector(*list)

    def __add__(self, other):
        if len(self.list) == len(other.list):
            new_l = list(map(lambda x: x[0] + x[1],
                            list(zip(self.list, other.list))))
            return self.new_obj(new_l)
        else:
            raise TypeError('размерности векторов не совпадают')

    def __sub__(self, other):
        if len(self.list) == len(other.list):
            new_l = list(map(lambda x: x[0] - x[1],
                            list(zip(self.list, other.list))))
            return self.new_obj(new_l)
        else:
            raise TypeError('размерности векторов не совпадают')

    def get_coords(self):
        return tuple(self.list)


class VectorInt(Vector):
    def __init__(self, *args):
        if all([isinstance(digit, int) for digit in args]):
            self.list = args
        else:
            raise ValueError('координаты должны быть целыми числами')


v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(2, 3, 4, 5)

v3 = Vector(2.3, 3, 4, 5)

v12 = v1 - v2
v13 = v1 - v3
print(v12)
print(v13)
print(v12.get_coords())
print(v13.get_coords())

# v1 = Vector(1, 2, 3)
# v2 = Vector(3, 4, 5)
#
# assert (v1 + v2).get_coords() == (
# 4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
# assert (v1 - v2).get_coords() == (
# -2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"
#
# v = VectorInt(1, 2, 3, 4)
# assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"
#
# try:
#     v = VectorInt(1, 2, 3.4, 4)
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"
#
# v1 = VectorInt(1, 2, 3, 4)
# v2 = VectorInt(4, 2, 3, 4)
# v3 = Vector(1.0, 2, 3, 4)
#
# v = v1 + v2
# assert type(
#     v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
# v = v1 + v3
# assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"