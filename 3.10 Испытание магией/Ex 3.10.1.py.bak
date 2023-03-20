class TicTacToe:
    def __init__(self):
        self.pole = None

    def init(self):
        self.pole = tuple(tuple(Cell() for i in range(3)) for j in range(3))

    def show(self):
        pass

    def human_go(self):
        pass

    def computer_go(self):
        pass

    def bool(self):
        pass

    def validate(self, key):
        if isinstance(key, tuple) and len(key) == 2:
            return all([isinstance(key[0], int), 0 <= key[0] <= 2, isinstance(key[1], int), 0 <= key[1] <= 2])
        if isinstance(key, int):
            return  0 <= key <= 2

    def __getitem__(self, key):
        if self.validate(key):
            return self.pole[key[0]][key[1]].value

    def __setitem__(self, key, value):
        if self.validate(key):
            if self.validate(value):
                self.pole[key[0]][key[1]].value = value



class Cell():
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0

game = TicTacToe()
game.init()
print(game[0, 1])
game[0, 1] = 2
print(game[0, 1])
