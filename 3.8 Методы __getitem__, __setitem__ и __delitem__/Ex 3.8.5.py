class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.array = []
        for i in range(self.max_length):
            self.array.append(cell())

    def __getitem__(self, key):
        if 0 <= key < self.max_length:
            return self.array[key].value
        else:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __setitem__(self, key, value):
        if 0 <= key < self.max_length:
            self.array[key].value = value
        else:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __str__(self):
        return str([elem.value for elem in self.array]).replace(',','').replace('[', '').replace(']', '')

class Integer():
    def __init__(self, start_value=0):
        self.start_value = start_value
        self.__value = 0


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __setattr__(self, key, value):
        if isinstance(value, int):
            self.__dict__['_' +self.__class__.__name__ + '__value'] = value
        else:
            raise ValueError('должно быть целое число')



ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
#ar_int[1] = 10
for i in range(10):
    ar_int[i] = i+1
#ar_int[1] = 10.5 # должно генерироваться исключение ValueError
#ar_int[10] = 1 # должно генерироваться исключение IndexError
print(ar_int)
