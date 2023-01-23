class ListMath:
    def __init__(self, mylist = [].copy()):
        self.lst_math = []
        for i in mylist:
            if type(i) == int or type(i) == float:
                self.lst_math.append(i)

    def __add__(self, other):
        return ListMath(list(map(lambda x: round(x + other,2 ), self.lst_math)))

    def __radd__(self, other):
        return ListMath(list(map(lambda x: round(x + other, 2), self.lst_math)))

    def __iadd__(self, other):
        l = (list(map(lambda x: round(x + other, 2), self.lst_math)))
        self.lst_math.clear()
        self.lst_math.extend(l)
        return self


    def __sub__(self, other):
        return ListMath(list(map(lambda x: round(x - other, 2), self.lst_math)))

    def __rsub__(self, other):
        return ListMath(list(map(lambda x: round(other - x, 2), self.lst_math)))

    def __isub__(self, other):
        l = (list(map(lambda x: round(x - other, 2), self.lst_math)))
        self.lst_math.clear()
        self.lst_math.extend(l)
        return self

    def __mul__(self, other):
        return ListMath(list(map(lambda x: round(x * other, 2), self.lst_math)))

    def __rmul__(self, other):
        return ListMath(list(map(lambda x: round(other * x, 2), self.lst_math)))

    def __imul__(self, other):
        l = (list(map(lambda x: round(other * x, 2), self.lst_math)))
        self.lst_math.clear()
        self.lst_math.extend(l)
        return self

    def __truediv__(self, other):
        return ListMath(list(map(lambda x: round(x / other, 2), self.lst_math)))

    def __rtruediv__(self, other):
        return ListMath(list(map(lambda x: round(other / x, 2), self.lst_math)))

    def __itruediv__(self, other):
       l = (list(map(lambda x: round(x / other, 2), self.lst_math)))
       self.lst_math.clear()
       self.lst_math.extend(l)
       return self


# lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
# print(lst)
# lst = lst + 76 # сложение каждого числа списка с определенным числом [77, 71, 83.68]
# print(lst)
# lst = 6.5 + lst # сложение каждого числа списка с определенным числом [83.5, 77.5, 90.18]
# print(lst)
# lst += 76.7  # сложение каждого числа списка с определенным числом [160.2, 154.2, 166.88]
# print(lst)
# lst = lst - 76 # вычитание из каждого числа списка определенного числа [84.2, 78.2, 90.88]
# print(lst)
# lst = 7.0 - lst # вычитание из числа каждого числа списка [-77.2, -71.2, -83.88]
# print(lst)
# lst -= 76.3  # [-153.5, -147.5, -160.18]
# print(lst)
# lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5) [-767.5, -737.5, -800.9]
# print(lst)
# lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5) [-3837.5, -3687.5, -4004.5]
# print(lst)
# lst *= 5.54  # [-21259.75, -20428.75, -22184.93]
# print(lst)
# lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13) [-1635.37, -1571.44, -1706.53]
# print(lst)
# lst = 3 / lst # деление числа на каждый элемент списка [-0.0, -0.0, -0.0]
# print(lst)
# lst /= 13.0  # [-0.0, -0.0, -0.0]
# print(lst)

lst1 = ListMath()
lp = [1, False, 2, -5, "abc", 7]
lst2 = ListMath(lp)
lst3 = ListMath(lp)

assert id(lst2.lst_math) != id(lst3.lst_math), "внутри объектов класса ListMath должна создаваться копия списка"

assert lst1.lst_math == [] and lst2.lst_math == [1, 2, -5, 7], "неверные значения в списке объекта класса ListMath"

res1 = lst2 + 76
lst = ListMath([1, 2, 3])
lst += 5
assert lst.lst_math == [6, 7, 8] and res1.lst_math == [77, 78, 71, 83], "неверные значения, полученные при операциях сложения"

lst = ListMath([0, 1, 2])
res3 = lst - 76
res4 = 7 - lst
assert res3.lst_math == [-76, -75, -74] and res4.lst_math == [7, 6, 5], "неверные значения, полученные при операциях вычитания"

lst -= 3
assert lst.lst_math == [-3, -2, -1], "неверные значения, полученные при операции вычитания -="

lst = ListMath([1, 2, 3])
res5 = lst * 5
res6 = 3 * lst
lst *= 4
assert res5.lst_math == [5, 10, 15] and res6.lst_math == [3, 6, 9], "неверные значения, полученные при операциях умножения"
assert lst.lst_math == [4, 8, 12], "неверные значения, полученные при операциях умножения"

lst = lst / 2
lst /= 13.0


lst = ListMath([3, 2, 1]) # 3 2 1
res1 = lst + 3  # 6, 5, 4
res1 += 3 # res1.lst_math = 9,8,7
print(res1.lst_math)
lst2 = 10 - lst  # 7 8 9
print(lst2.lst_math)