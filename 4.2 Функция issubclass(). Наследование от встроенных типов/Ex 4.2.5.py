
class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))

class DictShop(dict):
    def __init__(self, dict={}):
        if (len(dict) > 0 and self.check(dict)) or (len(dict) == 0):
            super().__init__(dict)
    def check(self, dict_some):
        if isinstance(dict_some, dict):
            if all([isinstance(key, Thing) for key in dict_some.keys()]):
                return True
            else:
                raise TypeError('ключами могут быть только объекты класса Thing')
        else:
            raise TypeError('аргумент должен быть словарем')

    def __setitem__(self, key, value):
        if isinstance(key, Thing):
            super().__setitem__(key, value)
        else:
            raise TypeError('ключами могут быть только объекты класса Thing')

dict_things3 = DictShop()

#things = Thing('book', 234, 2978.22)
th_01 = Thing('Лыжи1', 111000, 11978.55)
th_02 = Thing('Книга2', 11500, 1256)
things = {th_01: th_01, th_02: th_02}
#dict_things1 = DictShop()
dict_things = DictShop(things)


th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
#dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2


for x in dict_things:
    print(x.name)

dict_things[1] = th_1 # исключение TypeError