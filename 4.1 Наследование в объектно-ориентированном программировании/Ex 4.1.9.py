class Validator:
    def _is_valid(self, data):
        return True

    def __call__(self, *args, **kwargs):
        if self._is_valid(args[0]):
            return True
        else:
            raise ValueError('данные не прошли валидацию')

class IntegerValidator(Validator):

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if isinstance(data, int) and self.min_value <= data <= self.max_value:
            return True
        else:
            return False


class FloatValidator (Validator):

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if isinstance(data, float) and self.min_value <= data <= self.max_value:
            return True
        else:
           return False







v = Validator()
v('data')
integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
res2 = float_validator(10)    # исключение ValueError

print(res1)
print(res2)