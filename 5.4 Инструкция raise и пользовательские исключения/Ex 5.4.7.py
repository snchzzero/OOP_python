class DateError(ValueError):
    pass

class DateString:
    def __init__(self, date_string):
        if not isinstance(date_string, str) or len(date_string.split('.')) < 3:
            raise DateString

        day = date_string.split('.')[0]
        month = date_string.split('.')[1]
        year = date_string.split('.')[2]

        for elem in [day, month, year]:
            if elem in [day, month] and not all([i in '123456789' for i in elem]):
                raise DateString
            elif elem in year and not all([i in '1234567890' for i in elem]):
                raise DateString
