class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for j in range(3))for i in range(3))

    def clear(self):
        for i in range(len(self.pole)):
            for j in range(len(self.pole[0])):
                self.pole[i][j].is_free = True
                self.pole[i][j].value = 0

    def __setitem__(self, key, value):
        if self.validate(key):
            if bool(self.pole[key[0]][key[1]]):
                self.pole[key[0]][key[1]].value = value
                self.pole[key[0]][key[1]].is_free = False
            else:
                raise ValueError('клетка уже занята')

    def __getitem__(self, item):
        #print(type(item))
        if isinstance(item, tuple) and len(item) == 2 and all([isinstance(item[0], int), isinstance(item[1], int)]):
            return self.pole[item[0]][item[1]].value
        elif isinstance(item, tuple) and len(item) == 2 and any([isinstance(item[0], slice), isinstance(item[1], slice)]):
            if isinstance(item[0], slice):
                return tuple([self.pole[i][item[1]].value for i in range(3)][item[0].start:item[0].stop])
            elif isinstance(item[1], slice):
                return tuple([obj.value for obj in self.pole[item[0]][item[1].start:item[1].stop]])

    def validate(self, key):
        if len(key) == 2 and 0 <= key[0] < 3 and 0 <= key[1] < 3:
            return True
        else:
            raise IndexError('неверный индекс клетки')

class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free



# game = TicTacToe()
# game.clear()
# game[0, 0] = 1
# game[1, 0] = 2
# print(game[0, 0])
# print(game[0, :])
# print(game[:, 1])

game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2
# формируется поле:
# 1 0 0
# 2 0 0
# 0 0 0
#game[3, 2] = 2  # генерируется исключение IndexError
if game[0, 0] == 0:
    game[0, 0] = 2
v1 = game[0, :]  # 1, 0, 0
v2 = game[:, 0]  # 1, 2, 0


g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"

g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3

print(g[0, :])
print(g[1, :])
print(g[:, 0])

assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3), \
    "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"