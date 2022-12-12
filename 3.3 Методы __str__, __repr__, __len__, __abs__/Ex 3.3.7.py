import math

class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.__img = value

    def __setattr__(self, key, value):
        if key in ['_Complex__real', 'real']:
            if type(value) == int or type(value) == float:
                self.__dict__["_Complex__real"] = value
            else:
                raise ValueError("Неверный тип данных.")
        elif key in ['_Complex__img', 'img']:
            if type(value) == int or type(value) == float:
                self.__dict__["_Complex__img"] = value
            else:
                raise ValueError("Неверный тип данных.")


    def __abs__(self):
        return math.sqrt((self.real * self.real) + (self.img * self.img))




cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = (abs(cmp))
