class TableValues:
    def __init__(self, rows, cols, cell=None):
        if cell == None:
            raise ValueError('параметр cell не указан')
        else:
            #print(cell())
            self.cells = tuple(tuple(cell() for col in range(cols)) for row in range(rows))
            #print(cell())

    def __getitem__(self, item):
        return self.cells[item[0]][item[1]].value
        #print(self.cells[item[0]][item[1]])

    def __setitem__(self, item, value):
        self.cells[item[0]][item[1]].value = value


class CellInteger:
    def __init__(self, start_value=0):
        self.start_value = start_value
        self.__value = IntegerValue(start_value)

    @property
    def value(self):
        return self.__value.value

    @value.setter
    def value(self, value):
        self.__value.value = value


class IntegerValue:
    def __init__(self, value):
        self.__value = value

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
            raise ValueError('возможны только целочисленные значения')





a = IntegerValue(10)
table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
#table[0, 0] = 1.45 # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()

tb = TableValues(3, 2, cell=CellInteger)
tb[0, 0] = 1
assert tb[0, 0] == 1, "некорректно работает запись и/или считывание значения в ячейку таблицы по индексам"

try:
    tb[2, 1] = 1.5
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

for row in tb.cells:
    for x in row:
        assert isinstance(x, CellInteger), "коллекция cells должна содержать только объекты класса  CellInteger"

cell = CellInteger(10)
assert cell.value == 10, "дескриптор value вернул неверное значение"