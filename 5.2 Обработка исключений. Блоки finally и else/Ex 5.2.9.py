class Rect:
    def __init__(self, x, y, width, height):
        if not all([isinstance(param, (int, float))for param in [x, y, width, height]]) \
                or not width >= 0 or not height >= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def is_collision(self, rect):
        point_x_self = [i for i in range(self._x, self._x + self._width + 1)]
        point_y_self = [i for i in range(self._y, self._y + self._height + 1)]
        point_x_rect = [i for i in range(rect._x, rect._x + rect._width + 1)]
        point_y_rect = [i for i in range(rect._y, rect._y + rect._height + 1)]
        if not all([pxs not in point_x_rect for pxs in point_x_self]) or \
                not all([pys not in point_y_rect for pys in point_y_self]):
                raise TypeError('прямоугольники пересекаются')
        else:
            return True



lst_rect = []
for param in [
    [0, 0, 5, 3],
    [6, 0, 3, 5],
    [3, 2, 4, 4],
    [0, 8, 8, 1]
]:
    lst_rect.append(Rect(param[0], param[1], param[2], param[3]))

lst_not_collision = []
for rect in lst_rect:
    try:
        for x in lst_rect:
            if rect != x:
                try:
                    rect.is_collision(x)
                except Exception:
                    raise TypeError('прямоугольники пересекаются')
    except Exception:
        continue
    finally:
        lst_not_collision.append(rect)

print(lst_not_collision)
print(lst_not_collision)






