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


# game = TicTacToe()
# game.init()
# print(game[0, 1])
#game[0, 1] = 2
#print(game[0, 1])
#game.is_human_win
# print(game.is_human_win)
# game.check_free()
# game.show()
# game.computer_go()

# step_game = 0
# while game:
#     game.show()
#
#     if step_game % 2 == 0:
#         game.human_go()
#     else:
#         game.computer_go()
#
#     step_game += 1
#     # print(step_game)
#     print()
#
#     # if step_game == 5:
#     #     print(game.is_human_win)
#     #     print(game.is_computer_win)
#
# game.show()
# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все получится, со временем")
# else:
#     print("Ничья.")

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), \
    "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
print(bool(game))
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, \
    "при инициализации игрового поля " \
    "все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, \
    "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно " \
    "не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, \
    "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус " \
    "игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, \
    "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус " \
    "игры в момент присвоения новых значения по индексам: game[i, j] = value"