import math
class PathLines:
    #my_list = list()
    def __init__(self, *args):
        self.my_list = list()
        for arg in args:
            self.add_line(arg)


    def get_path(self):
        return self.my_list
    def get_length(self):
        total =0
        for line in self.my_list:
            total += line.LenLineTo()
        return total
    def add_line(self, line):
        if len(self.my_list) > 0:
            line.prev_x = self.my_list[-1].x
            line.prev_y = self.my_list[-1].y
        elif len(self.my_list) == 0:
            line.prev_x = 0
            line.prev_y = 0
        self.my_list.append(line)


class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def prev_x(self, prev_x):
        self.prev_x = prev_x

    def prev_y(self, prev_y):
        self.prev_y = prev_y

    def LenLineTo(self):
        return math.sqrt(pow(self.x-self.prev_x, 2) + pow(self.y-self.prev_y, 2))

p = PathLines(LineTo(1, 2))
print(p.get_length())  # 2.23606797749979
p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
print(p.get_length())  # 28.191631669843197
m = p.get_path()
print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True

h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
print(h.get_length())  # 71.8992593599813

k = PathLines()
print(k.get_length())  # 0
print(k.get_path())  # []