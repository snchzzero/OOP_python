# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/HbtVara1GPI
# Подвиг 8. Объявите в программе класс Cart (корзина), объекты которого создаются командой:
# cart = Cart()
# Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки. Изначально этот список
# должен быть пустым.
# В классе Cart объявить методы:
# add(self, gd) - добавление в корзину товара, представленного объектом gd;
# remove(self, indx) - удаление из корзины товара по индексу indx;
# get_list(self) - получение из корзины товаров в виде списка из строк:
# ['<наименовние_1>: <цена_1>',
# '<наименовние_2>: <цена_2>',
# ...
# '<наименовние_N>: <цена_N>']
# Объявите в программе следующие классы для описания товаров:
# Table - столы;
# TV - телевизоры;
# Notebook - ноутбуки;
# Cup - кружки.
# Объекты этих классов должны создаваться командой:
# gd = ИмяКласса(name, price)
# Каждый объект классов товаров должен содержать локальные свойства:
# name - наименование;
# price - цена.
# Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table), два ноутбука
# (Notebook) и одну кружку (Cup). Названия и цены придумайте сами.
# P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям.
class Cart():
    def __init__(self, goods=[]):
        self.goods = goods
    def add(self, gd):
        self.goods.append(gd)
    def remove(self, indx):
        self.goods.pop(indx)
    def get_list(self):
        return [f'{i.name}: {i.price}' for i in self.goods]

class Table():
    def __init__(self, name, price):
        self.name = name
        self.price = price
class TV():
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Notebook():
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Cup():
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()
tv1, tv2 = TV('Samsung', 70000), TV('LGUNO', 55000)
tbl = Table('IKEA', 5000)
lptp1, lptp2 = Notebook('iMAC', 300000), Notebook('Acer', 70000)
cp = Cup('IKEA', 1000)

cart.add(tv1)
cart.add(tv2)
cart.add(tbl)
cart.add(lptp1)
cart.add(lptp2)
cart.add(cp)
cart.remove(2)
print(cart.get_list())