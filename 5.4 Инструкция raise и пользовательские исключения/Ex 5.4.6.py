class PrimaryKeyError(Exception):
    def __init__(self, id=None, pk=None):
        if id is None and pk is None:
            self.message = 'Первичный ключ должен быть целым неотрицательным числом'
        elif id:
            self.message = f'Значение первичного ключа id = {id} недопустимо'
        elif pk:
            self.message = f'Значение первичного ключа pk = {pk} недопустимо'

    def __str__(self):
        return self.message


e1 = PrimaryKeyError()          # Первичный ключ должен быть целым неотрицательным числом
e2 = PrimaryKeyError(id='abc')  # Значение первичного ключа id = abc недопустимо
e3 = PrimaryKeyError(pk='123')  # Значение первичного ключа pk = 123 недопустимо

print(e2) # Значение первичного ключа id = abc недопустимо

try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as ex:
    print(ex)


assert issubclass(PrimaryKeyError, Exception), "класс PrimaryKeyError должен наследоваться от класса Exception"

e1 = PrimaryKeyError(id=1)
e2 = PrimaryKeyError(pk=2)
e3 = PrimaryKeyError()

assert str(e1) == "Значение первичного ключа id = 1 недопустимо", "неверное сообщение для исключения объекта класса PrimaryKeyError"
assert str(e2) == "Значение первичного ключа pk = 2 недопустимо", "неверное сообщение для исключения объекта класса PrimaryKeyError"
assert str(e3) == "Первичный ключ должен быть целым неотрицательным числом", "неверное сообщение для исключения объекта класса PrimaryKeyError"