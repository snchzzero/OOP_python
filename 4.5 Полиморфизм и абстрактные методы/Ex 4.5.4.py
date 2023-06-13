class ShopInterface():
    def get_id(self):
        raise NotImplementedError("в классе не переопределен метод get_id")


class ShopItem(ShopInterface):
    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self._id = hash(self)

    def __hash__(self):
        return hash((self._name, self._weight, self._price))

    def get_id(self):
        return self._id


shi1 = ShopItem("thing", 35, 150)
shi2 = ShopItem("thing2", 36, 150)

print(shi1.get_id())
print(shi2.get_id())