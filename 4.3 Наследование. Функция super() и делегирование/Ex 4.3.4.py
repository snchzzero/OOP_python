class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year


class DigitBook(Book):
    def __init__(self, title, author, pages, year, size, frm):
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm


book = Book('title', 'author', 23, 1789)
db = DigitBook('title2', 'author2', 45, 1234, 23, 'txt')
db2 = DigitBook('title3', 'author3', 67, 3456, 45678, 'pdf')
