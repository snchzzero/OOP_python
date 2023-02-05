class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))


lst_in = ['Python; Балакирев С.М.; 2020',
'Python ООП; Балакирев С.М.; 2021',
'Python ООП; Балакирев С.М.; 2022',
'Python; Балакирев С.М.; 2021']

lst_bs = []
for i in lst_in:
    name = (i.split(';')[0])
    author = (i.split(';')[1].lstrip())
    year = int(i.split(';')[2].lstrip())
    lst_bs.append(BookStudy(name, author, year))

unique_books = len(set(map(lambda x: hash(x), lst_bs)))