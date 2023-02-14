class Record:
    def __init__(self, **kwargs):
        self.dict = {}
        for key, value in kwargs.items():
            self.dict[key] = value
            self.__dict__[key] = value
            #self.__dict__.update(kwargs)

    def __getitem__(self, key):
        if isinstance(key, int) and 0 <= key < len(self.dict):
            return list(self.dict.values())[key]
        else:
            raise IndexError('неверный индекс поля')

    def __setitem__(self, key, value):
        if isinstance(key, int) and 0 <= key < len(self.dict):
            self.dict[list(self.dict.keys())[key]] = value
            self.__dict__[list(self.dict.keys())[key]] = value
        else:
            raise IndexError('неверный индекс поля')










r = Record(pk=1, title='Python ООП', author='Балакирев')
# print(r[2])
# r[0] = 'dsadas'
# print(r.dict)
r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r.dict)
print(r[1]) # Супер курс по ООП
#r[3] # генерируется исключение IndexError