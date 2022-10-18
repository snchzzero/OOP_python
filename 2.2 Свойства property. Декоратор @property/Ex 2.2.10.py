class PhoneBook:
    def __init__(self):
        self.list = list()

    def add_phone(self, phone):
        self.list.append(phone)

    def remove_phone(self, indx):
        self.list.pop(indx)

    def get_phone_list(self):
        return self.list

class PhoneNumber:
    def __init__(self, number=None, fio=None):
        self.number = number
        self.fio = fio

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)
p.remove_phone(-1)
phones = p.get_phone_list()
print(phones)