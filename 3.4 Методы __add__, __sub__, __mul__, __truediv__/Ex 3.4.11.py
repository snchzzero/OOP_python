class MaxPooling:
    def __init__(self, step, size):
        self.step = step
        self.size = size

    def valid(self, list):
        for l in list:
            if len(l) == len(list[0]) and all([True if type(elem) == int or type(elem) == float else False for elem in l]):
                continue
            else:
                return False
        return True

    def matrix_gen(self, list):
        result = [[]]
        ll = []
        x = y = 0
        # формируем координаты в соответствии с step
        while y < len(list) and x < len(list[y]):
            for y in range(y, y + self.size[1]):
                for x in range(x, x + self.size[0]):
                    if y < len(list) and x < len(list[y]):
                        ll.append(list[y][x])
                x -= self.size[1] - 1
            y -= self.size[0] - 1
            if len(ll) == self.size[0] * self.size[1]:
                result[-1].append(max(ll))
            ll.clear()
            if (x + self.step[0] < len(list[y])):
                x = x + self.step[0]
            elif (y + self.step[1] < len(list)):
                y = y + self.step[1]
                x = 0
                result.append([])
            else:
                break
        if len(result[-1]) == 0:
            result.pop(-1)
        return result



    def __call__(self, *args, **kwargs):
        if self.valid(args[0]):
            #print('YES')
            return self.matrix_gen(args[0])
        else:
            raise ValueError("Неверный формат для первого параметра matrix.")

# mp = MaxPooling(step=(2, 2), size=(2,2))
# res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
# print(res)


mp = MaxPooling(step=(2, 2), size=(2,2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
print(res1)
res2 = mp(m2)
print(res2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2,2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"

# mp = MaxPooling(step=(2, 2), size=(2, 2))
# print(mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]))  # [[6, 8], [9, 7]]
# print(mp([[5, 0, 88, 2, 7, 65],
#           [1, 33, 7, 45, 0, 1],
#           [54, 8, 2, 38, 22, 7],
#           [73, 23, 6, 1, 15, 0],
#           [4, 12, 9, 1, 76, 6],
#           [0, 15, 10, 8, 11, 78]]))  # [[33, 88, 65], [73, 38, 22], [15, 10, 78]]
# print(mp([[1, 5, 2], [7, 0, 1], [4, 10, 3]]))  # [[7]]
mp = MaxPooling(step=(2, 2), size=(3, 3))
print(mp([[1, 2, 3, 4, 5, 6, 5], [0, 4, 5, 1, 3, 45, 4], [7, 8, 9, 2, 10, 3, 0],
          [0, 1, 2, 3, 4, 100, 3], [3, 4, 5, 5, 60, 1, 4]]))