import sys
class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)



lst_in = [
    'Системный блок: 1500 75890.56',
    'Монитор Samsung: 2000 34000',
    'Клавиатура: 200.44 545',
    'Монитор Samsung: 2000 34000',
]
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять!

shop_items = {}
for i in lst_in:
    name = (i.split(':')[0])
    weight = float(i.split(':')[1].lstrip().split()[0])
    price = float(i.split(':')[1].lstrip().split()[1])
    new = ShopItem(name, weight, price)
    total = 1
    if len(shop_items) > 0:
        for key in shop_items.keys():
            if (hash(key) == hash(new)):
                shop_items[key][1] =  shop_items[key][1] + 1
                total += 1
        shop_items[new] = [new, total]
    else:
        shop_items[new] = [new, 1]



# s1 = ShopItem('Системный блок', 1500, 75890.56)
# s2 = ShopItem('Монитор Samsung', 2000, 34000)
# s3 = ShopItem('Клавиатура', 200.44, 545)
# s4 = ShopItem('Монитор Samsung', 2000, 34000)
#
# print(hash(s1), s1 == s2)
# print(hash(s2), s2 == s4)
# print(hash(s3))
# print(hash(s4))

it1 = ShopItem('name', 10, 11)
it2 = ShopItem('name', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

it2 = ShopItem('name', 10, 12)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('name', 11, 11)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('NAME', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

name = lst_in[0].split(':')
for sp in shop_items.values():
    assert isinstance(sp[0], ShopItem) and type(sp[1]) == int, "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"

v = list(shop_items.values())
if v[0][0].name.strip() == "Системный блок":
    assert v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3, "неверные значения в словаре shop_items"

if v[0][0].name.strip() == "X-box":
    assert v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3, "неверные значения в словаре shop_items"
