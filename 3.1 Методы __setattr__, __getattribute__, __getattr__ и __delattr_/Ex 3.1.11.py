import time

class GeyserClassic:
    MAX_DATE_FILTER = 100
    dict = {1: None, 2: None, 3: None}

    def add_filter(self, slot_num, filter):
        if slot_num == 1 and self.dict[1] == None and filter.__class__ == Mechanical:
            self.dict[1] = filter
        elif slot_num == 2 and self.dict[2] == None and filter.__class__ == Aragon:
            self.dict[2] = filter
        elif slot_num == 3 and self.dict[3] == None and filter.__class__ == Calcium:
            self.dict[3] = filter

    def remove_filter(self, slot_num):
        self.dict[slot_num] = None

    def get_filters(self):
        return tuple(self.dict.values())

    def water_on(self):
        if all(self.dict.values()) == True:
            #print([time.time() - _.date for _ in self.dict.values()])
            #a = all([True if (time.time() - _.date) <= self.MAX_DATE_FILTER else False for _ in self.dict.values() ])
            #print(a)
            #if a:
            if all([True if (time.time() - _.date) <= self.MAX_DATE_FILTER else False for _ in self.dict.values()]):
                return True
            else:
                return False
        else:
            return False

class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key not in self.__dict__:
            self.__dict__[key] = value

class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key not in self.__dict__:
            self.__dict__[key] = value

class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key not in self.__dict__:
            self.__dict__[key] = value

# a = GeyserClassic()
# a.add_filter(1, Mechanical(time.time()))
# a.add_filter(2, Aragon(time.time()-99))
# a.add_filter(3, Calcium(time.time()))
# print(a.get_filters())
# print(a.water_on())

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))

assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"

my_water.add_filter(3, Calcium(time.time()))
assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"

f1, f2, f3 = my_water.get_filters()
assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3, Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"

my_water.remove_filter(1)
assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"

my_water.add_filter(1, Mechanical(time.time()))
assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)

my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

f1 = Mechanical(1.0)
f2 = Aragon(2.0)
f3 = Calcium(3.0)
assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

f1.date = 5.0
f2.date = 5.0
f3.date = 5.0

assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"

