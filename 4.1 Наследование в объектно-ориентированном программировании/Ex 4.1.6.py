class Thing:
    total = 0
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name, price,  weight=None, dims=None, memory=None, frm=None):

        self.id = self.total
        self.name = name
        self.price = price
        self.weight = weight
        self.dims = dims
        self.memory = memory
        self.frm = frm
        Thing.total += 1

    def get_data(self):
        return (self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm)

class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price, weight, dims)

class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price, memory=memory, frm=frm)

table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')

#table2=Thing("Круглый", 1024, 812.55, (700, 750, 700))
#table3=Thing("Круглый", 1024, 812.55, (700, 750, 700))
print(*table.get_data())
print(*book.get_data())
#print(*table2.get_data())
#print(*table3.get_data())
