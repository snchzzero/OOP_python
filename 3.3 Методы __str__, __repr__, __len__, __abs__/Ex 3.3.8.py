import math
from functools import reduce

class RadiusVector:
    def __init__(self, *args):
        self.coords=[]
        if len(args) == 1 and args[0] > 0:
            self.coords = [0 for _ in range(args[0])]
        elif len(args) > 1:
            for _ in args:
                if type(_) == float or type(_) == int:
                    self.coords.append(_)

    def set_coords(self, *args):
        if len(args) > 0:
            if all([True for _ in args[:len(self.coords)] if type(_) == float or type(_) == int]):
                for _ in range(len(args[:len(self.coords)])):
                    if type(args[_]) == float or type(args[_]) == int:
                        self.coords[_] = args[_]

    def get_coords(self):
        return tuple(self.coords)

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return math.sqrt(reduce(lambda x, i: (i * i) + x, self.coords, 0))




vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
v3D = RadiusVector(1, 2, 3)
#print(res_abs)