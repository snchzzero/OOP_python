class ItemAttrs:
    def __getitem__(self, item):
        for count, key in enumerate(self.__dict__):
            if count == item:
                return self.__dict__[key]

    def __setitem__(self, item, value):
        for count, key in enumerate(self.__dict__):
            if count == item:
                self.__dict__[key] = value


class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __getitem__(self, item):
        return super().__getitem__(item)


pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10
print(pt[0])