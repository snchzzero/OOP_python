class SuperShop:
    def __init__(self, name, goods=list()):
        self.name = name
        self.goods = goods

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

class StringValue:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length
    def __set_name__(self, owner, name):
        self.name = "_" + name
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if type(value) == str and self.min_length <= len(value) < self.max_length:
            instance.__dict__[self.name] = value

class PriceValue:
    def __init__(self, max_value):
        self.max_value = max_value
    def __set_name__(self, owner, name):
        self.name = "_" + name
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if (type(value) == int or type(value) == float) and 0 <= value < self.max_value:
            instance.__dict__[self.name] = value


class Product:
    name = StringValue(2, 50)
    price = PriceValue(10000)

    def __init__(self, name, price):
        self.name = name
        self.price = price

# shop = SuperShop("У Балакирева")
# shop.add_product(Product("Курс по Python", 0))
# shop.add_product(Product("Курс по Python ООП", 2000))
# for p in shop.goods:
#     print(f"{p.name}: {p.price}")
# shop.remove_product(shop.goods[-1])
# for p in shop.goods:
#     print(f"{p.name}: {p.price}")

shop = SuperShop("У Балакирева")
shop.add_product(Product("name", 100))
shop.add_product(Product("name", 100))
assert shop.name == "У Балакирева", "атрибут name объекта класса SuperShop содержит некорректное значение"

for p in shop.goods:
    assert p.price == 100, "дескриптор price вернул неверное значение"
    assert p.name == "name", "дескриптор name вернул неверное значение"

t = Product("name 123", 1000)
shop.add_product(t)
shop.remove_product(t)
assert len(shop.goods) == 2, "неверное количество товаров: возможно некорректно работают методы add_product и remove_product"

assert hasattr(shop.goods[0], 'name') and hasattr(shop.goods[0], 'price')

t = Product(1000, "name 123")
if hasattr(t, '_name'):
    assert type(t.name) == str, "типы поля name должнен быть str"
if hasattr(t, '_price'):
    assert type(t.price) in (int, float), "тип поля price должнен быть int или float"

