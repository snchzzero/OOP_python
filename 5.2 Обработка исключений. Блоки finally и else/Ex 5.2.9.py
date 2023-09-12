class Rect:
    def __init__(self, x, y, width, height):
        if not all([isinstance(param, (int, float))for param in [x, y, width, height]]) \
                or not width > 0 or not height > 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def is_collision(self, rect):

        if any(
                [
                    self._y > (rect._y + rect._height),
                    (self._y + self._height) < rect._y,
                    self._x > (rect._x + rect._width),
                    (self._x + self._width) < rect._x
                ]
        ):
            return True
        raise TypeError('прямоугольники пересекаются')


lst_rect = []
for param in [
    [0, 0, 5, 3],
    [6, 0, 3, 5],
    [3, 2, 4, 4],
    [0, 8, 8, 1]
]:
    lst_rect.append(Rect(param[0], param[1], param[2], param[3]))
#
lst_not_collision = []
lst_failed = []
for rect in lst_rect:
    if rect in lst_failed:
        continue
    try:
        for x in lst_rect:
            if rect != x:
                try:
                    rect.is_collision(x)
                except Exception:
                    lst_failed.append(x)
                    raise TypeError('прямоугольники пересекаются')
        lst_not_collision.append(rect)
    except Exception:
        continue
#
#
# print(lst_not_collision)
# print(lst_not_collision)




r = Rect(1, 2, 10, 20)
assert r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20, "неверные значения атрибутов объекта класса Rect"

r2 = Rect(1.0, 2, 10.5, 20)

try:
    r2 = Rect(0, 2, 0, 20)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"


assert len(lst_rect) == 4, "список lst_rect содержит не 4 элемента"
assert len(lst_not_collision) == 1, "неверное число элементов в списке lst_not_collision"

def not_collision(rect):
    for x in lst_rect:
        try:
            if x != rect:
                rect.is_collision(x)
        except TypeError:
            return False
    return True

f = list(filter(not_collision, lst_rect))
assert lst_not_collision == f, "неверно выделены не пересекающиеся прямоугольники, возможно, некорректно работает метод is_collision"

r = Rect(3, 2, 2, 5)
rr = Rect(1, 4, 6, 2)

try:
    r.is_collision(rr)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове метода is_collision() для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"






