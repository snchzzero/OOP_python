class GamePole:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines

    def init_pole(self):
        pass
        # инициализации начального состояния игрового поля

    def open_cell(i, j):
        pass

    def show_pole(self):
        pass
        #отображает игровое поле в консоли


class Cell:
    def __init__(self):
        self.__is_mine = None
        self.__number = None
        self.__is_open = None

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

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
        #print(key)
        # print(value)
        #print('_' + self.__class__.__name__+'__is_mine')
        if (key == '_' + self.__class__.__name__+'__is_mine' or key == '_' + self.__class__.__name__ + '__is_open') or \
            (key == 'is_mine' or key == 'is_open') and type(value) == bool:
                print(value)





a = Cell()
a.is_mine = True
a.is_mine = 0
a.number = 3