class DataBase:
    def __init__(self, path):
        self.dict_db = {}
        self.path = path

    def write(self, record):
        self.dict_db[record.pk] = [record]

    def read(self, pk):
        return self.dict_db[pk]



class Record:
    total = 0
    pk = None
    def __new__(cls, *args, **kwargs):
        cls.__instance = super().__new__(cls)
        #print(cls.__instance)
        cls.total += 1
        return cls.__instance

    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = Record.total

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)

#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['Балакирев С.М.; программист; 33', 'Балакирев С.М.; прогdраммист; 33',
'Кузнецов А.В.; разведчик-нелегал; 35',
'Суворов А.В.; полководец; 42',
'Иванов И.И.; фигурант всех подобных списков; 26',
'Балакирев С.М.; преподаватель; 33']
db = DataBase('path')
for i in lst_in:
    fio = (i.split(';')[0])
    descr = (i.split(';')[1].lstrip())
    old = float(i.split(';')[2].lstrip())
    new = Record(fio, descr, old)
    print(hash(new))
    db.write(new)
    for key in db.dict_db.keys():
        print(hash(key))
        if hash(key) == hash(new):
            db.dict_db[key].append(new)

print(db.dict_db)

db22345 = DataBase('123')
r1 = Record('fio', 'descr', 10)
r2 = Record('fio', 'descr', 10)
assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

db22345.write(r2)
r22 = db22345.read(r2.pk)
print(r22.pk)
print(r2.pk)
assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

fio = lst_in[0].split(';')[0].strip()
v = list(db.dict_db.values())
if fio == "Балакирев С.М.":
    assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"

if fio == "Гейтс Б.":
    assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"



