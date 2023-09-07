class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], float) or not self.min_value <= args[0] < self.max_value:
            raise ValueError('значение не прошло валидацию')


class IntegerValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], int) or not self.min_value < args[0] <= self.max_value or isinstance(args[0], bool):
            raise ValueError('значение не прошло валидацию')
def is_valid(lst, validators):
    new_lst = []
    for value in lst:
        try:
            validators[0](value)
        except ValueError:
            try:
                validators[1](value)
            except ValueError:
                continue
        new_lst.append(value)
    return new_lst



fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]

print(lst_out)

