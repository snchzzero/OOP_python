class Bag:
    def __init__(self, max_weight, things=list()):
        self.max_weight = max_weight
        self.__things = things

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        all_weights = self.get_total_weight()
        if thing.weight + all_weights <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        self.__things.pop(int(indx))

    def get_total_weight(self):
        return sum([thing.weight for thing in self.__things])

class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
bag.add_thing(Thing("Бумага2", 281))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")

