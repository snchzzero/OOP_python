class Point:
    def __init__(self, x=None, y=None):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return (self.__x, self.__y)

class Rectangle:
    def __init__(self, *args):
        #print(type(args))
        self.__sp = args[0]
        self.__ep = args[1]

    def set_coords(self, sp=None, ep=None):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return (self.__sp, self.__ep)

    def draw(self):
        print(f'Прямоугольник с координатами: {self.__sp} {self.__ep}')

rect = Rectangle(0, 0, 20, 34)

# pt = Point(1, 2)
# print(pt.get_coords())
# r1 = Rectangle(Point(3, 4), Point(5, 6))


assert isinstance(rect, Rectangle) and hasattr(Rectangle, 'set_coords') and hasattr(Rectangle, 'get_coords') and hasattr(Rectangle, 'draw'), "в классе Rectangle присутствуют не все методы"

r = Rectangle(1, 2.6, 3.3, 4)
r.set_coords(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
a, b = sp.get_coords()
c, d = ep.get_coords()
assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"

r = Rectangle(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
a, b = sp.get_coords()
c, d = ep.get_coords()
assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"

assert isinstance(r._Rectangle__sp, Point) and isinstance(r._Rectangle__ep, Point), "атрибуты __sp и __ep должны ссылаться на объекты класса Point"