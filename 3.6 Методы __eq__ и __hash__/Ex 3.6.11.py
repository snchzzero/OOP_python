import math

class Triangle:
    def validate(self, a, b, c):
        if a < b + c and b < c + a and c < a + b:
            return True
        else:
            return False

    def __init__(self, a=None, b=None, c=None):
            if self.validate(a, b, c):
                self.__a = a
                self.__b = b
                self.__c = c
            else:
                raise ValueError("с указанными длинами нельзя образовать треугольник")

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value

    def __setattr__(self, key, value):
        if ((type(value) == int or type(value) == float) and value > 0):
            self.__dict__['_' + self.__class__.__name__ + '__' + key[-1]] = value
        else:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args):
        p = len(self) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

# tr = Triangle(1, 2, 2)
# print(tr())
# tr.a = 10
# tr.c = 23

tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
print(tr())
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"