class Tuple(tuple):
    def __init__(self, iter_obj):
        super().__init__()

    def __add__(self, other):
        if not isinstance(other, tuple):
            return Tuple(tuple(self) + tuple(other))




w = Tuple((1, 3, 5))
t = Tuple([1, 2, 3])
t2 = Tuple([4, 5, 6])
t = t + "Python"
t = (t + "Python") + "ООП"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')

tn = t2 + t + w
print(tn)