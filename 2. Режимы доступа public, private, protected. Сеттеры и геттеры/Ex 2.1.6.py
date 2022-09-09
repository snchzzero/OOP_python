class Book:
    def __init__(self, author=None, title=None, price=None):
        self.__author = author
        self.__title = title
        self.__price = price

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

book = Book("Константин Симонов", "Живые и мертвые", 99)
print(book.get_author())
print(book.get_title())
print(book.get_price())
book.set_price(100)
book.set_author("Человек-Амфибия")
book.set_title("Александр Беляев")
print(book.get_author())
print(book.get_title())
print(book.get_price())
