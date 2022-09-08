from string import ascii_lowercase, digits

class  CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        if number.count("-") == 3:
            return all(map(lambda x: x.isdigit() and len(x) == 4, number.split("-")))

            # проверяет строку с номером карты и возвращает булево значение True, если номер в верном формате и False - в противном случае. Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).
        else:
            return False

    @classmethod
    def check_name(cls, name):
        if len(name.split()) == 2:
            if all(map(lambda x: x in cls.CHARS_FOR_NAME, [i for i in name.split()[0]])) \
                    and all(map(lambda x: x in cls.CHARS_FOR_NAME, [i for i in name.split()[1]])):
                    return True
            else:
                return False
        else:
            return False

is_number = CardCheck.check_card_number("1230-5672-9012-0000")
is_name = CardCheck.check_name("SERGEY BALAKIREV")

print(is_number)
print(is_name)