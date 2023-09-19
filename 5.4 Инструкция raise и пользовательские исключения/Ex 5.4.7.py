class DateError(Exception):
    def __str__(self):
        return "Неверный формат даты"

class DateString:
    def __init__(self, date_string):
        if not isinstance(date_string, str) or len(date_string.split('.')) < 3:
            raise DateError

        day = date_string.split('.')[0]
        month = date_string.split('.')[1]
        year = date_string.split('.')[2]

        for elem in [day, month, year]:
            if not all([i in '1234567890' for i in elem]):
                raise DateError

        if not 1 <= int(day) <= 31 or not 1 <= int(month) <= 12 or not 1 <= int(year) <= 3000:
            raise DateError

        self.day = '0' + day if len(day) == 1 else day
        self.month = '0' + month if len(month) == 1 else month
        self.year = year

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'


date_string = input()
try:
    date = DateString(date_string)
    print(date) # date - объект класса DateString
except Exception as ex:
    print(ex)