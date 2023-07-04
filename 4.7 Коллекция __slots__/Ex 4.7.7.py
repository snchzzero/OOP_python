class Note:
    def __init__(self, name, ton):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key in ['name', '_name'] and value in ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']:
            self.__dict__['_name'] = value
        elif key in ['ton', '_ton'] and isinstance(value, int) and value in [-1, 0, 1]:
            self.__dict__['_ton'] = value
        else:
            raise ValueError('недопустимое значение аргумента')


class Notes:
    __slots__ = ['_do', '_re', '_mi', '_fa', '_solt', '_la', '_si']
    obj_id = None
    list = []

    def __new__(cls):
        if cls.obj_id is None:
            cls.obj_id = super().__new__(cls)
            return cls.obj_id
        else:
            return cls.obj_id

    def __init__(self):
        self._do = Note('до', 0)
        self._re = Note('ре', 0)
        self._mi = Note('ми', 0)
        self._fa = Note('фа', 0)
        self._solt = Note('соль', 0)
        self._la = Note('ля', 0)
        self._si = Note('си', 0)

    def __getitem__(self, item):
        if isinstance(item, int) and 0 <= item <= 6:
            atr = self.__slots__[item]
            return getattr(self, atr)
        else:
            raise IndexError('недопустимый индекс')





notes = Notes()
notes2 = Notes()
nota = notes[2]  # ссылка на ноту ми
print(nota)
notes[3]._ton = -1 # изменение тональности ноты фа

print(notes[3]._ton)