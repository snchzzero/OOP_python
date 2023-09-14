class Test:
    def __init__(self, descr):
        if not isinstance(descr, str) or not 10 <= len(descr) <= 10000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr


    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        if not isinstance(ans_digit, (int, float)) or not isinstance(max_error_digit, (int, float)) \
                or not max_error_digit >= 0:
            raise ValueError('недопустимые значения аргументов теста')
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def run(self):
        ans = float(input())
        return self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit


descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
ans = float(ans) # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может

# Какое значение получится при вычислении 2 + 2? | 4

try:
    a = TestAnsDigit(descr, ans)
    result = a.run()
    print(result)
except Exception as ex:
    print(ex)

try:
    test = Test('descr')
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при вызове инициализатора класса Test с неверным набором аргументов"

try:
    test = Test('descr ghgfhgjg ghjghjg')
    test.run()
except NotImplementedError:
    assert True
else:
    assert False

assert issubclass(TestAnsDigit, Test)

t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1)
t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, 0.5)

try:
    t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, -0.5)
except ValueError:
    assert True
else:
    assert False