class ListInteger(list):
    def __init__(self, *args):
        if self.check(*args):
            super().__init__(*args)
        else:
            raise TypeError('можно передавать только целочисленные значения')

    def check(self, args):
        return all([isinstance(arg, int) for arg in args])

    def __setitem__(self, key, value):
        if isinstance(value, int):
            super().__setitem__(key, value)
        else:
            raise TypeError('можно передавать только целочисленные значения')

    def append(self, value):
        if isinstance(value, int):
            super().append(value)
        else:
            raise TypeError('можно передавать только целочисленные значения')



a = [1, 2, 3]
#print(a[4])

s = ListInteger((1, 2, 3))
#a = ListInteger((1.3, 2, 3))
s[1] = 10
s.append(11)
#s.append(11.2)
print(s)
print(a)
s[0] = 10.5 # TypeError