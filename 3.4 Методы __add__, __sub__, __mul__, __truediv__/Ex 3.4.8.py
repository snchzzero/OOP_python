class Lib:
    def __init__(self, book_list=[]):
        self.book_list = book_list

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if other.__class__.__name__ == "Book":
            self.book_list.remove(other)

        elif type(other) == int and 0 <= other <= len(self.book_list):
            self.book_list.pop(other)
        return self

    def __len__(self):
        return len(self.book_list)

class Book:
    def __init__(self, title=None, author=None, year=None):
        self.title = title
        self.author = author
        self.year = year


lib = Lib()
b1 = Book('Процесс', 'Кафка', 2020)
lib = lib + b1 # добавление новой книги в библиотеку
b2 = Book('Три товарища', 'Ремарк', 2021)
lib += b2
b3 = Book('Бесы', 'Достоевский', 2022)
lib += b3
b4 = Book('1984', 'Оруэлл', 2022)
lib += b4
print(len(lib)) # Печатает 4 - ОК

lib = lib - b1 # удаление книги book из библиотеки
lib -= b2
print(len(lib)) # 2, ведь мы удалили 2 книги

lib = lib - 1 # удаление книги по ее порядковому номеру
lib -= 0
print(len(lib))
