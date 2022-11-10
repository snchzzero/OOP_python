class Shop:
    def __init__(self, name, goods=list()):
        self.name = name
        self.goods = goods

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

class Product:
    id_total = 0

    def __init__(self, name="", weight=0, price=0):
        self.id = self.total()
        self.name = name
        self.weight = weight
        self.price = price

    @classmethod
    def total(cls):
        cls.id_total += 1
        return cls.id_total

    def __setattr__(self, key, value):
        if key == 'id' and type(value) == int:
            self.__dict__[key] = value
        elif key == 'name' and type(value) == str:
            self.__dict__[key] = value
        elif (key == 'weight' or key == 'price')  and (type(value) == int or type(value) == float) and value >= 0:
            self.__dict__[key] = value
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")


#book = Product("Python ООП", 100, 1024)
#book2 = Product("Python", 150, 512)

shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")

shop.remove_product(book)

for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")