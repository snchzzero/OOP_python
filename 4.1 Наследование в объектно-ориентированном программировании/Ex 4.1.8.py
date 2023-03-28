class Singleton:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name
        else:
            self.name = self.name


game = Game('игра1')
game2 = Game('игра2')
game3 = Game('игра3')
