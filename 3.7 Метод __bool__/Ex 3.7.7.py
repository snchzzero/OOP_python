class Ellipse:
    def __init__(self, *args):
        if len(args) == 4:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]

    def __bool__(self):
        return all([i in self.__dict__.keys() for i in ['x1', 'y1', 'x2', 'y2']])


    def get_coords(self):
        if bool(self):
            return tuple((self.x1, self.y1, self.x2, self.y2))
        else:
            raise AttributeError('нет координат для извлечения')





el1 = Ellipse()
el2 = Ellipse(5, 6, 7, 1)
# print(bool(el1))
# print(bool(el2))
# #print(el1.get_coords())
# print(el2.get_coords())
lst_geom = [Ellipse(), Ellipse(), Ellipse(5, 6, 7, 1), Ellipse(5, 6, 7, 4)]
for el in lst_geom:
     print(bool(el))


for el in lst_geom:
    if bool(el):
        print(el.get_coords())