class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

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
        if (key.startswith("_Dimensions__") and key.replace('_Dimensions__', '') in ['a', 'b', 'c'] and
                self.MIN_DIMENSION <= value <= self.MAX_DIMENSION):
            self.__dict__[key] = value
        elif ((key == 'a' or key == 'b' or key == 'c') and
              self.MIN_DIMENSION <= value <= self.MAX_DIMENSION):
            self.__dict__[f'_Dimensions__{key}'] = value

    def volume(self):
        return self.a * self.b * self.c

    def __ge__(self, other):
        return self.a * self.b * self.c >= other.a * other.b * other.c

    def __gt__(self, other):
        return self.a * self.b * self.c >= other.a * other.b * other.c

class ShopItem():
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim

trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.volume())


# print(lst_shop_sorted)
#
# d3 = Dimensions(52, 60, 80)
# d4 = Dimensions(50, 60, 80)
# print(d3 <= d4)
# print(d3 < d4)
#
# d3.a = 55
# d3.b = 66
# d3.c = 88
# print(d3.c)

assert len(lst_shop) == 4, "число элементов в lst_shop не равно 4"

lst_sp = []
lst_sp.append(ShopItem('кеды', 1024, Dimensions(40, 30, 120)))
lst_sp.append(ShopItem('зонт', 500.24, Dimensions(10, 20, 50)))
lst_sp.append(ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)))
lst_sp.append(ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200)))

lst_sp_sorted = ['зонт', 'кеды', 'табуретка', 'холодильник']
s = [x.name for x in lst_shop_sorted]
assert lst_sp_sorted == s, "список lst_shop_sorted сформирован неверно"

d1 = Dimensions(40, 30, 120)
d2 = Dimensions(40, 30, 120)
d3 = Dimensions(30, 20, 100)
assert d1 <= d2, "неверно отработал оператор <="
assert d3 <= d2, "неверно отработал оператор <="
assert d3 < d2, "неверно отработал оператор <"

d2.a = 10
d2.b = 10
d2.c = 10
assert d2 < d1, "неверно отработал оператор < после изменения объема через объекты-свойства a, b, c"