import random
class GamePole:
    count = 0
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance



    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cels = tuple(tuple(Cell() for m in range(self.M)) for n in range(self.N))



    def init_pole(self):
        # инициализации начального состояния игрового поля
        total = 0
        while total < self.total_mines:
            n = random.randint(0, self.N - 1)
            m = random.randint(0, self.M - 1)
            if  self.__pole_cels[n][m].is_mine != True:
                self.__pole_cels[n][m].is_mine = True
                total += 1

        # для записи количества мин вокруг клетки
        for n in range(self.N):
            for m in range (self.M):
                number = 0
                for cord_check in [[n, m + 1 ], [n + 1, m + 1 ], [n + 1, m],
                                  [n + 1, m - 1], [n, m - 1], [n - 1, m - 1], [n - 1, m], [n - 1, m + 1]]:
                   if 0 <= cord_check[0] < self.N and 0 <= cord_check[1] < self.M:
                       if self.__pole_cels[cord_check[0]][cord_check[1]].is_mine == True:
                           number += 1
                if number > 0:
                    self.__pole_cels[n][m].number = number

    def valid(self, i, j):
        return 0 <= i < self.N and 0 <= j < self.M and type(i) == int and type(j) == int

    def open_cell(self, i, j):
        if self.valid(i, j):
            self.__pole_cels[i][j].is_open = True
        else:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
    def show_pole(self):
        pass
        #отображает игровое поле в консоли

    @property
    def pole(self):
        return self.__pole_cels

    def __call__(self, *args, **kwargs):
        if self.count == 0:
            self.count += 1
            return self.__init__(*args, **kwargs)



class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        self.__is_open = value

    def __setattr__(self, key, value):
        if (key == '_' + self.__class__.__name__+'__is_mine' or key == 'is_mine') and type(value) == bool:
            self.__dict__['_' + self.__class__.__name__ + '__is_mine'] = value
        elif (key == '_' + self.__class__.__name__ + '__is_open' or key == 'is_open') and type(value) == bool:
            self.__dict__['_' + self.__class__.__name__ + '__is_open'] = value
        elif (key == '_' + self.__class__.__name__ + '__number' or key == 'number') and type(value) == int and 0 <= value <= 8:
            self.__dict__['_' + self.__class__.__name__ + '__number'] = value
        else:
            raise ValueError("недопустимое значение атрибута")






# #b = Cell()
# a = GamePole(4, 3, 2)
# a.init_pole()
# # a = Cell()
# # a.is_mine = True
# # a.is_mine = True
# # a.number = 3

# pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
# pole.init_pole()
# if pole.pole[0][1]:
#     pole.open_cell(0, 1)
# if pole.pole[3][5]:
#     pole.open_cell(3, 5)
# pole.open_cell(30, 100)  # генерируется исключение IndexError
# pole.show_pole()

p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
    Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1

assert m == 10, "на поле расставлено неверное количество мин"
p.open_cell(0, 1)
p.open_cell(9, 19)

try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                continue
            if pole[ii][jj].is_mine:
                n += 1

    return n


for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"