class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.list = []

    def add_point(self, x, y, speed):
        self.list.append([(x, y), speed])

    def __setitem__(self, key, value):
        if isinstance(key, int) and 0 <= key < len(self.list):
            self.list[key][1] = value
        else:
            raise IndexError('некорректный индекс')

    def __getitem__(self, key):
        if isinstance(key, int) and 0 <= key < len(self.list):
            return self.list[key]
        else:
            raise IndexError('некорректный индекс')


tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2
tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError