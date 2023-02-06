class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):

        if (float(value) > 0):
            self.__dict__[key] = float(value)
        else:
            raise ValueError("габаритные размеры должны быть положительными числами")

    def __hash__(self):
        return hash((self.a, self.b, self.c))

s_inp = input()  # эту строку (переменную s_inp) в программе не менять
#s_inp = ['1 2 3;', '4 5 6.78;', '1 2 3;', '3 1 2.5']
lst_dims = []
for i in s_inp.split(';'):
    a, b, c = i.strip().replace(';', '').split()
    lst_dims.append(Dimensions(a, b, c))

lst_dims = sorted(lst_dims, key=lambda x: hash(x))


