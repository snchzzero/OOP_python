# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Vr4c1LgE91o
# Подвиг 5. Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:
# tr = TriangleChecker(a, b, c)
# Здесь a, b, c - длины сторон треугольника.
# В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал следующие коды:
# 1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
# 2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
# 3 - стороны a, b, c образуют треугольник.
# Проверку параметров a, b, c проводить именно в таком порядке.
# Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:
# a, b, c = map(int, input().split())
# Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c.
# Вызовите метод is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).
# Sample Input:
# 3 4 5
# Sample Output:
# 3

class TriangleChecker():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        l1 = list(self.__dict__.values())
        #print(type(l1[0]))
        if (
            ((type(l1[0]) != int and type(l1[0]) != float) or
            (type(l1[1]) != int and type(l1[1]) != float) or
            (type(l1[2]) == int and type(l1[2]) == float))
            or (l1[0] <= 0 or l1[1] <= 0 or l1[2] <= 0)
           ):
            return 1
        if l1[0] + l1[1] <= l1[2] or l1[0] + l1[2] <= l1[1] or l1[1] + l1[2] <= l1[0]:
            return 2
        else:
            return 3

a, b, c = map(int, input().split())
#a, b, c = input().split()
# a = 3
# b = 4
# c = 5
tr = TriangleChecker(a, b, c)
#print(tr.__dict__)
print(tr.is_triangle())