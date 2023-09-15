digits = list(map(float, input().split()))
#digits = [1, 2, 3, 4, 5]


class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        return super(TupleLimit, cls).__new__(cls, tuple(lst))

    def __init__(self, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        self.lst = lst
        self.max_length = max_length

    def __repr__(self):
        return ' '.join([str(i) for i in self.lst])

    def __str__(self):
        return ' '.join([str(i) for i in self.lst])



try:
    new_obj = TupleLimit(digits, 5)
    print(new_obj)
except Exception as ex:
    print(ex)
