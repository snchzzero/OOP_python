import random

class EmailValidator:
    #__instance = None  # сылка на экземпляр класса
    CHARS = "abcdefghijklmnoprstquvwxyz1234567890._"
    def __new__(cls, *args, **kwargs):
        return None
        #if cls.__instance == None:
            #cls.__instance = super().__new__(cls)   # адрес нового объекта
            #return cls.__instance

    @classmethod
    def get_random_email(cls):
        len_email_before_Dog = random.randint(1, 100)  #(1, 100)
        len_email_after_Dog = random.randint(1, 47)  #(1, 47)
        len_email_after_Dot = random.randint(2, 3)
        CHARS_list = list()
        CHARS_list.extend(cls.CHARS)
        new_email = ''
        total = 0
        for a in [len_email_before_Dog, len_email_after_Dog, len_email_after_Dot]:
            if total == 1:
                new_email += '@'
            elif total == 2:
                new_email += '.'
            for i in range(0, a):
                if len(new_email) > 0:
                    s = random.choice(CHARS_list)
                    if (s != '.' and new_email[-1] != '.') or (s != '.' and new_email[-1] == '.'):
                        new_email += s
                elif len(new_email) == 0:
                    s = random.choice(CHARS_list)
                    new_email += s
            total += 1
        total = 0
        return new_email
        #print(new_email)


    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            l1 = [i for i in email.split("@")]
            if len(l1) == 2:
                if len(l1[0]) < 101 and len(l1[1]) < 51:
                    if l1[1].count('.') >= 1:
                        for s in range (1, len(email)):
                            if email[s-1] == email[s] == '.':
                                return False
                        return True
        return False

    @staticmethod
    def __is_email_str(email):
        return True if type(email) == str else False


#print(EmailValidator.check_email('x8nxv2k2v16_@cgi_lrkoo17kju9r5ezvs.4k'))
assert EmailValidator.check_email("sc_lib@list.ru") == True and EmailValidator.check_email("sc_lib@list_ru") == False and EmailValidator.check_email("sc@lib@list_ru") == False and EmailValidator.check_email("sc.lib@list_ru") == False and EmailValidator.check_email("sclib@list.ru") == True and EmailValidator.check_email("sc.lib@listru") == False and EmailValidator.check_email("sc..lib@list.ru") == False, "метод check_email отработал некорректно"

m = EmailValidator.get_random_email()
assert EmailValidator.check_email(m) == True, "метод check_email забраковал сгенерированный email методом get_random_email"

assert EmailValidator() is None, "при создании объекта класса EmailValidator возвратилось значение отличное от None"

assert EmailValidator._EmailValidator__is_email_str('abc'), "метод __is_email_str() вернул False для строки"