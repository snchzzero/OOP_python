import copy


class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []

    def add_thing(self, obj):
        actual_weight = sum([weight[1] for weight in self._things])
        if actual_weight + obj[1] > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(obj)

    # def __str__(self):
    #     result = ''
    #     for thing in self._things:
    #         result = result + str(thing) + ''
    #     return result

class BoxDefender:
    def __init__(self, box):
        self.box = box

    def __enter__(self):
        self.box_copy = copy.deepcopy(self.box)
        return self.box_copy

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.box._things = self.box_copy._things




# box = Box("сундук", 1000)
# box.add_thing(("спички", 46.6))
# box.add_thing(("рубашка", 134))
#
# with BoxDefender(box) as b:
#     b.add_thing(("зонт", 346.6))
#     b.add_thing(("шина_лайт", 1))

b = Box('name', 2000)
assert b._name == 'name' and b._max_weight == 2000, "неверные значения атрибутов объекта класса Box"

b.add_thing(("1", 100))
b.add_thing(("2", 200))

try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 1000))
        bb.add_thing(("4", 1900))
except ValueError:
    assert len(b._things) == 2

else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 100))
except ValueError:
    assert False, "возникло исключение ValueError, хотя, его не должно было быть"
else:
    assert len(b._things) == 3, "неверное число элементов в списке _things"