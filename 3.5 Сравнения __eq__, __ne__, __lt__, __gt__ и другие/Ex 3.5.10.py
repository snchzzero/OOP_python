class Box:
    def __init__(self):
        self.list = []

    def add_thing(self, obj):
        self.list.append(obj)

    def get_things(self):
        return self.list

    def __eq__(self, other):
        total = 0
        for si in self.list:
            for oi in other.list:
                if oi == si:
                    total += 1
                    break
        return total == len(self.list)

class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass


b1 = Box()
b2 = Box()

b1.add_thing(Thing('Мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 != b2 # True
print(res)