class SparseTable:
    def __init__(self, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.dict = {}

    def add_data(self, row, col, data):
        self.dict[(row, col)] = data
        self.rows = max(self.dict.keys(), key= lambda x: x[0])[0] + 1
        self.cols = max(self.dict.keys(), key=lambda x: x[1])[1] + 1

    def remove_data(self, row, col):
        if (row, col) in self.dict.keys():
            del self.dict[(row, col)]
            self.rows = max(self.dict.keys(), key=lambda x: x[0])[0] + 1
            self.cols = max(self.dict.keys(), key=lambda x: x[1])[1] + 1
        else:
            raise IndexError('ячейка с указанными индексами не существует')

    def __setitem__(self, key, value):
        self.dict[key] = value
        self.rows = max(self.dict.keys(), key=lambda x: x[0])[0] + 1
        self.cols = max(self.dict.keys(), key=lambda x: x[1])[1] + 1

    def __getitem__(self, item):
        if item in self.dict.keys():
            return self.dict[item]
        else:
            raise ValueError('данные по указанным индексам отсутствуют')

class Cell:
    def __init__(self, value):
        self.value = value

# st = SparseTable()
# st.add_data(2, 5, Cell("cell_25"))
# st.add_data(0, 0, Cell("cell_00"))
# st[2, 5] = 25 # изменение значения существующей ячейки
# st[11, 7] = 'cell_117' # создание новой ячейки
# print(st[0, 0]) # cell_00
# st.remove_data(2, 5)
# print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
# val = st[2, 5] # ValueError
# st.remove_data(12, 3) # IndexError

st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"