class Model:
    def query(self, **kwargs):
        self.dict = kwargs

    def __str__(self):
        if 'dict' in self.__dict__:
            s = 'Model:'
            for key, value in self.dict.items():
                s += f" {key} = {value},"
            return s[:-1]
        else:
            return 'Model'

model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)
print(str(model).replace(' ', ''))
