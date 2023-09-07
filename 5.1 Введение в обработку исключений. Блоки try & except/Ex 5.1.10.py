class Triangle:
    def __init__(self, a, b, c):
        if self.check_positive(a, b, c):
            self._a = a
            self._b = b
            self._c = c

    def check_positive(self, a, b, c):
        for i in [a, b, c]:
            if not isinstance(i, (int, float)) or i <= 0:
                raise TypeError('стороны треугольника должны быть положительными числами')
        if not (a < b + c and b < a + c and c < a + b):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')
        return True

#input_data = [(2.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []
for data in input_data:
    try:
        lst_tr.append(Triangle(data[0], data[1], data[2]))
    except (TypeError, ValueError):
        continue
print(lst_tr)