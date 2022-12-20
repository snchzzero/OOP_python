class PolyLine:
    list = []
    def __init__(self, *args):
        for arg in args:
            self.add_coord(arg[0], arg[1])

    def add_coord(self, x, y):
        self.list.append(tuple([x, y]))

    def remove_coord(self, indx):
        self.list.pop(indx)

    def get_coord(self):
        return self.list



poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
poly.add_coord(5, 6)
print(poly.get_coord())
poly.remove_coord(0)
print(poly.get_coord())