class Budget:
    def __init__(self):
        self.list = []

    def add_item(self, it):
        self.list.append(it)

    def remove_item(self, indx):
        self.list.pop(indx)

    def get_items(self):
        return self.list


class Item:
    def __init__(self, name=None, money=None):
        self.name = name
        self.money = money

    def __add__(self, other):
        if self.__class__.__name__ == "Item" and other.__class__.__name__ == "Item":
            return self.money + other.money
        else:
            return self + other.money

    def __radd__(self, other):
        if self.__class__.__name__ == "Item" and other.__class__.__name__ == "Item":
            return self.money + other.money
        else:
            return self.money + other


# my_budget = Budget()
# my_budget.add_item(Item("Курс по Python ООП", 2000))
# my_budget.add_item(Item("Курс по Django", 5000.01))
# my_budget.add_item(Item("Курс по NumPy", 0))
# my_budget.add_item(Item("Курс по C++", 1500.10))
#
# # вычисление общих расходов
# s = 0
# for x in my_budget.get_items():
#     s = s + x

my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))
assert len(my_budget.get_items()) == 4
my_budget.remove_item(1)
assert len(my_budget.get_items()) == 3
s = 0
for x in my_budget.get_items():
    s = s + x
assert s == 3500.1
# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
assert Item('a', 150) + Item('b', 111.11)  == 261.11
