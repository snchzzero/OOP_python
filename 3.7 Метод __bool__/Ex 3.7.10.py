class Vector:
    def __init__(self, *args):
        self.list = [arg for arg in args if type(arg) == int or type(arg) == float]

    def __add__(self, other):
        return Vector(list(map(lambda x: x[0] + x[1], list(zip(self.list, other.list)))))

    def __sub__(self, other):
        return Vector(list(map(lambda x: x[0] - x[1], list(zip(self.list, other.list)))))

    def __mul__(self, other):
        return Vector(list(map(lambda x: x[0] * x[1], list(zip(self.list, other.list)))))

    def __iadd__(self, other):
        if type(other) == int or type(other) == float:
            return list(map(lambda x: x + other, self.list))
        else:
            return list(map(lambda x: x[0] + x[1], list(zip(self.list, other.list))))

    def __isub__(self, other):
        if type(other) == int or type(other) == float:
            return list(map(lambda x: x - other, self.list))
        else:
            return list(map(lambda x: x[0] - x[1], list(zip(self.list, other.list))))

    def __eq__(self, other):
        return (all([True if x[0] == x[1] else False for x in list(zip(self.list, other.list))]))



# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# v1 += 10
#print(v1.list)  # [11, 12, 13]
# a = (v1 + v2)
# print(a)
# print(list(zip([1, 2, 3], [1, 2, 3])))
# print(*list(map(lambda x: x[0] + x[1] ,list(zip([1, 2, 3], [1, 2, 3])))))
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).list)  # [5, 7, 9]
print((v1 - v2).list)  # [-3, -3, -3]
print((v1 * v2).list)  # [4, 10, 18]

v1 += 10
print(v1.list)  # [11, 12, 13]
v1 -= 10
print(v1.list)  # [1, 2, 3]
v1 += v2
print(v1.list)  # [5, 7, 9]
v2 -= v1
print(v2.list)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True
