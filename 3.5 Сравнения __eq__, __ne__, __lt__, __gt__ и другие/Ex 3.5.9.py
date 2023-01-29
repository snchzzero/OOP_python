class MoneyR:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, volume):
        self.__cb = volume

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, numbers):
        self.__volume = numbers

    def convert(self, obj):
        if obj.cb == None:
            raise ValueError("Неизвестен курс валют.")
        else:
            key = [k for k in obj.cb.rates.keys() if obj.__class__.__name__.lower()[-1] == k[0]][0]
            if key == 'rub':
                return round(obj.volume)
            else:
                return round(obj.volume * (obj.cb.rates['rub'] * obj.cb.rates[key]))

    def __eq__(self, other):
        return self.convert(self) == self.convert(other)

    def __gt__(self, other):
        return self.convert(self) > self.convert(other)

    def __ge__(self, other):
        return self.convert(self) >= self.convert(other)

class MoneyD:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, volume):
        self.__cb = volume

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, numbers):
        self.__volume = numbers

    def convert(self, obj):
        if obj.cb == None:
            raise ValueError("Неизвестен курс валют.")
        else:
            key = [k for k in obj.cb.rates.keys() if obj.__class__.__name__.lower()[-1] == k[0]][0]
            if key == 'rub':
                return round(obj.volume)
            else:
                return round(obj.volume * (obj.cb.rates['rub'] * obj.cb.rates[key]))

    def __eq__(self, other):
        return self.convert(self) == self.convert(other)

    def __gt__(self, other):
        return self.convert(self) > self.convert(other)

    def __ge__(self, other):
        return self.convert(self) >= self.convert(other)

class MoneyE:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, volume):
        self.__cb = volume

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, numbers):
        self.__volume = numbers

    def convert(self, obj):
        if obj.cb == None:
            raise ValueError("Неизвестен курс валют.")
        else:
            key = [k for k in obj.cb.rates.keys() if obj.__class__.__name__.lower()[-1] == k[0]][0]
            if key == 'rub':
                return round(obj.volume)
            else:
                return round(obj.volume * (obj.cb.rates['rub'] * obj.cb.rates[key]))

    def __eq__(self, other):
        return self.convert(self) == self.convert(other)

    def __gt__(self, other):
        return self.convert(self) > self.convert(other)

    def __ge__(self, other):
        return self.convert(self) >= self.convert(other)

class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls

#cb = CentralBank()
#print(cb)
#print(CentralBank.rates)
CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
#print(CentralBank.rates)
r = MoneyR(45000)
d = MoneyE(500)
e = MoneyE()
e.volume =10
print(e.volume)
print(e.cb)
# r = MoneyR(45000)
# d = MoneyR(45000.1)
CentralBank.register(r)
CentralBank.register(d)
CentralBank.register(e)
print(e.cb)
print(r == d)
print(r < d)
print(r <= d)
