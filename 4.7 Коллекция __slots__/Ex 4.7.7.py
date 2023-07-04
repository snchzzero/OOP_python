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
