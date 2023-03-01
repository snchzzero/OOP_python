class Cell:
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = [[Cell(0) for col in range(self.cols)]for row in range(self.rows)]

    def valid_index(self, key):
        return 0 <= key[0] < self.rows and 0 <= key[1] < self.cols


    def __setitem__(self, key, value):
        if self.valid_index(key):
            if isinstance(value, self.type_data):
                self.table[key[0]][key[1]].data = value
            else:
                raise TypeError('неверный тип присваиваемых данных')
        else:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        if self.valid_index(item):
            return self.table[item[0]][item[1]].data
        else:
            raise IndexError('неверный индекс')

    def __iter__(self):
        self.start_row = 0
        return self

    def __next__(self):
        if self.start_row < self.rows:
            self.start_row += 1
            return [obj.data for obj in self.table[self.start_row - 1]]
        else:
            raise StopIteration



# tb = TableValues(3, 2)
# print(tb[0, 0])
# print(tb[2, 1])
# tb[0, 0] = 1
# tb[2, 1] = 2
# print(tb[0, 0])
# print(tb[2, 1])
# for row in tb:  # перебор по строкам
#     for value in row: # перебор по столбцам
#         print(value, end=' ')  # вывод значений ячеек в консоль
#     print()

tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(
            value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"

try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"