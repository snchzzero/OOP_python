class Track:
    def __init__(self, *args):
        self.__points = []
        for count, arg in enumerate(args):
            if len(args) > 2 and isinstance(args[count], (int, float)) and isinstance(args[count + 1], (int, float)):
                self.add_back(PointTrack(args[count], args[count + 1]))
                break
            else:
                self.add_back(arg)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points = [pt] + self.__points.copy()

    def pop_back(self):
        self.__points.pop(-1)

    def pop_front(self):
        self.__points.pop(0)


class PointTrack:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, key, value):
        if isinstance(value, (int, float)):
            self.__dict__[key] = value
        else:
            raise TypeError('координаты должны быть числами')

    def __str__(self):
        return f'{self.__class__.__name__}: {self.x}, {self.y}'



tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.add_front(PointTrack(-5, -5))

tr.pop_front()
tr.pop_back()
tr.add_front(PointTrack(-10, -11))
tr.add_back(PointTrack(112, 23))

print(tr.points)


for pt in tr.points:
    print(pt)