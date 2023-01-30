class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        if self.__class__.__name__ == "Box3D" and other.__class__.__name__ == "Box3D":
            return Box3D(self.width + other.width, self.height + other.height, self.depth + other.depth)
        elif (type(other) == int or type(other) == float) and self.__class__.__name__ == "Box3D":
            return Box3D(self.width + other, self.height + other, self.depth + other)

    def __radd__(self, other):
        if (type(other) == int or type(other) == float) and self.__class__.__name__ == "Box3D":
            return Box3D(self.width + other, self.height + other, self.depth + other)

    def __mul__(self, other):
        return Box3D(self.width * other, self.height * other, self.depth * other)

    def __rmul__(self, other):
        return Box3D(self.width * other, self.height * other, self.depth * other)

    def __sub__(self, other):
        return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)

    def __floordiv__(self, other):
        return Box3D(self.width // other, self.height // other, self.depth // other)

    def __mod__(self, other):
        return Box3D(self.width % other, self.height % other, self.depth % other)


# box1 = Box3D(1, 2, 3)
# box2 = Box3D(2, 4, 6)
#
# box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
# box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
# box = 3 * box2    # Box3D: width=6, height=12, depth=18
# box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
# box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
# box = box2 % 3    # Box3D: width=2, height=1, depth=0
# box3 = Box3D(2, 4, 6)

def test_add():
    box1, box2 = Box3D(1, 2, 3), Box3D(2, 4, 6)
    res1 = box1 + box2
    res2 = box2 + box1

    assert type(res1) is Box3D
    assert type(res2) is Box3D
    assert res1.width == res2.width == box1.width + box2.width
    assert res1.height == res2.height == box1.height + box2.height
    assert res1.depth == res2.depth == box1.depth + box2.depth


def test_add_float():
    box1 = Box3D(1, 2, 3)
    constant = 4.75
    res1 = box1 + constant
    res2 = constant + box1

    assert type(res1) is Box3D
    assert type(res2) is Box3D
    assert res1.width == res2.width == box1.width + constant
    assert res1.height == res2.height == box1.height + constant
    assert res1.depth == res2.depth == box1.depth + constant


def test_multiply():
    box1 = Box3D(1, 2, 3)
    constant = 4.1
    res1 = box1 * constant
    res2 = constant * box1

    assert type(res1) is Box3D
    assert type(res2) is Box3D
    assert res1.width == res2.width == box1.width * constant
    assert res1.height == res2.height == box1.height * constant
    assert res1.depth == res2.depth == box1.depth * constant


def test_subtract():
    box1, box2 = Box3D(1, 2, 3), Box3D(2, 4, 6)
    res1 = box2 - box1

    assert type(res1) is Box3D
    assert res1.width == box2.width - box1.width
    assert res1.height == box2.height - box1.height
    assert res1.depth == box2.depth - box1.depth


def test_floordiv():

    box1 = Box3D(53, 7, 28)
    constant = 12
    res1 = box1 // constant

    assert type(res1) is Box3D
    assert res1.width == box1.width // constant
    assert res1.height == box1.height // constant
    assert res1.depth == box1.depth // constant


def test_mod():
    box1 = Box3D(53, 7, 28)
    constant = 12
    res1 = box1 % constant

    assert type(res1) is Box3D
    assert res1.width == box1.width % constant
    assert res1.height == box1.height % constant
    assert res1.depth == box1.depth % constant

test_add()
test_add_float()
test_multiply()
test_subtract()
test_floordiv()
test_mod()