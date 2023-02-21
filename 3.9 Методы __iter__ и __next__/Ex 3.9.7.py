class TriangleListIterator:
    def __init__(self, list):
        self.list = list


    def __iter__(self):
        self.row = 0
        self.column = 0
        return self

    def __next__(self):
        if self.row < len(self.list):
            while self.row < len(self.list):
                if self.column <= self.row:
                    self.column += 1
                    return self.list[self.row][self.column - 1]
                self.row += 1
                self.column = 0
            else:
                raise StopIteration
        else:
            raise StopIteration



lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22', 'x23', 'x24'],
       ['x30', 'x31', 'x32', 'x33']]
it = TriangleListIterator(lst)

for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)