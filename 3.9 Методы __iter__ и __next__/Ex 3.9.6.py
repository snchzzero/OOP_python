class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.list = ['fio', 'job', 'old', 'salary', 'year_job']

    def validate(self, index):
        if  0 <= index < len(self.list):
            return True
        else:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        if self.validate(item):
            return self.__dict__[self.list[item]]

    def __setitem__(self, key, value):
        if self.validate(key):
            self.__dict__[self.list[key]] = value

    def __iter__(self):
        self.indx = 0
        return self

    def __next__(self):
        if self.indx < len(self.list):
            self.indx += 1
            return self[self.indx - 1]
        else:
            raise StopIteration



pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
print(pers[0])
pers[0] = 'Балакирев С.М.'
print(pers[0])
for v in pers:
    print(v)
pers[5] = 123 # IndexError