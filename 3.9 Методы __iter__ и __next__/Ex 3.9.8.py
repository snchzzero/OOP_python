class IterColumn:
    def __init__(self, list, column):
        self.list = list
        self.column = column

    def __iter__(self):
        self.row = 0
        self.clmn = 0
        return self

    def __next__(self):
        while self.row < len(self.list):
            self.row += 1
            return self.list[self.row - 1][self.column]
        else:
            raise StopIteration



lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x02'],
       ['x20', 'x21', 'x22', 'x23', 'x24'],
       ['x30', 'x31', 'x32', 'x33']]
it = IterColumn(lst, 1)

for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)