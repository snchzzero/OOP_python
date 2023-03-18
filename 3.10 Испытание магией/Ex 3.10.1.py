import random
class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)
    def __init__(self):
        self.pole = None
        self.init()

    def init(self):
        self.pole = tuple(tuple(Cell() for i in range(3)) for j in range(3))

    def show(self):
        for i, y in enumerate(self.pole):
            for j, x in enumerate(y):
                print(x.value, end=" ")
            print()

    def human_go(self):
        print('Введите координаты')
        cord = [int(i) for i in input().split()]
        while self.validate(cord) == False or \
                all([True if free != cord else False for free in self.check_free()]) == True:
            print('Такого поля не существует либо уже занято, введите еще раз')
            cord = [int(i) for i in input().split()]
        self[cord[0], cord[1]] = 1


    def computer_go(self):
        list_free = self.check_free()
        cord = random.randrange(0, len(list_free))
        self[list_free[cord][0], list_free[cord][1]] = 2

    @property
    def is_human_win(self):
        return self.check_wine(1)

    @property
    def is_computer_win(self):
        return self.check_wine(2)

    @property
    def is_draw(self):
        return True if self.check_wine(1) and self.check_wine(2) else False

    def check_wine(self, value):
        wine_index = [[(0, 0), (0, 1), (0, 2)],
                      [(1, 0), (1, 1), (1, 2)],
                      [(2, 0), (2, 1), (2, 2)],
                      [(0, 0), (1, 1), (2, 2)],
                      [(0, 1), (1, 1), (2, 1)],
                      [(0, 2), (1, 2), (2, 2)],
                      [(2, 0), (1, 1), (0, 2)],
                      [(0, 0), (1, 0), (2, 0)]]
        for var in wine_index:
            if all([True if self[index] == value else False for index in var]):
                return True
        return False

    def check_free(self):
        list_free = []
        for i, y in enumerate(self.pole):
            for j, x in enumerate(y):
                list_free.append([i, j]) if x.value == 0 else False
        return list_free

    def validate(self, key):
        if isinstance(key, int):
            return 0 <= key <= 2
        elif isinstance(key, (tuple, list)) and len(key) == 2:
            return all([isinstance(key[0], int), 0 <= key[0] <= 2, isinstance(key[1], int), 0 <= key[1] <= 2])


    def __getitem__(self, key):
        if self.validate(key):
            return self.pole[key[0]][key[1]].value
        else:
            raise IndexError('некорректно указанные индексы')

    def __setitem__(self, key, value):
        if self.validate(key):
            if self.validate(value):
                self.pole[key[0]][key[1]].value = value
        else:
            raise IndexError('некорректно указанные индексы')

    def __bool__(self):
        return all([len(self.check_free()) > 0, self.is_human_win == False, self.is_computer_win == False])

class Cell():
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0
