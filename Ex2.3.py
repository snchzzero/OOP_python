# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/bPH4It1_d0c
# Подвиг 4. Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть возможность создавать объекты каждого класса следующими командами:
#
# g1 = Line(a, b, c, d)
# g2 = Rect(a, b, c, d)
# g3 = Ellipse(a, b, c, d)
# Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов (произвольные числа). В каждом объекте
# координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний левый) в виде кортежей (a, b) и (c, d) соответственно.
#
# Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно (или Line, или Rect, или Ellipse).
# Координаты также генерируются случайным образом (числовые значения). Все объекты сохраните в списке elements.
# В списке elements обнулите координаты объектов только для класса Line.
# P.S. На экран в программе ничего выводить не нужно.
import random

class Line():
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect():
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse():
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

elements = list()
for i in range(217):
    a = random.randrange(1, 100)
    b = random.randrange(1, 100)
    c = random.randrange(1, 100)
    d = random.randrange(1, 100)
    elements.append(random.choice([Line(a, b, c, d),
                                   Rect(a, b, c, d),
                                   Ellipse(a, b, c, d)
                                   ])
                    )
for i in elements:
    if i.__class__ == Line:
        i.ep = (0, 0)
        i.sp = (0, 0)

#print(elements)
# print(elements[0].__dict__)
# print(elements[100].__dict__)
# print(elements[200].__dict__)
# print(elements[216].__dict__)
# print(elements[0].__class__)

