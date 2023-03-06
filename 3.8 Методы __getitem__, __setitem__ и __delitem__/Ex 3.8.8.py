class RadiusVector:
    def __init__(self, *args):
        self.coords = [arg for arg in args]

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.coords[item]
        elif isinstance(item, slice):
            return tuple(self.coords[item.start:item.stop:item.step])
            # return str(self.coords[item.start:item.stop:item.step]).replace('[', '').replace(']', '')

    def __setitem__(self, item, value):
        if isinstance(item, int):
            self.coords[item] = value
        elif isinstance(item, slice):
            self.coords[item.start:item.stop] = value







v = RadiusVector(1, 2, 3, 4)
print(v[1:2])  # 1
print(v[:])
print(v[2])
print(v[1:])
print(v[1::2])
v[1:3] = [0, 0, 0]
print(v[:])
