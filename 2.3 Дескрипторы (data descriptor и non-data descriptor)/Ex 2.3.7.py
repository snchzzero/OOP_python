class FloatValue:
    @classmethod
    def verify(cls, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")
    def __set_name__(self, owner, name):
        self.name = "_" + name
    def __get__(self, instance, owner):
        #getattr(instance, self.name)
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        self.verify(value)
        #setattr(instance, self.name, value)
        instance.__dict__[self.name] = value


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, N, M ):
        self.cells = [[Cell() for m in range(M)] for n in range(N)]



table = TableSheet(5, 3)
total = 1.0
for n in range(5):
    for m in range(3):
        table.cells[n][m].value = total
        total += 1.0


#tb = TableSheet(4, 3)
#print(len(tb.cells))  # == 4
#print(len(tb.cells[0]))  # == 3
#assert len(tb.cells) == 4 and len(tb.cells[0]) == 3, "неверное число строк и стобцов в таблице tb = TableSheet(4, 3)"


#print(len(table.cells))  # == 4
#print(len(table.cells[0]))  # == 3


assert isinstance(table, TableSheet)
assert len(table.cells) == 5 and len(table.cells[0]) == 3

assert type(table.cells) == list

res = [int(x.value) for row in table.cells for x in row]
assert res == list(range(1, 16))

table.cells[0][0].value = 1.0
x = table.cells[1][0].value

try:
    table.cells[0][0].value = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"