class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y



pt = Point(1, 2)

try:
    attr = pt._z
    print(attr)
except AttributeError:
    print('Атрибут с именем z не существует')
