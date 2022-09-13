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
        print(new_email)




    @classmethod
    def check_email(cls, email):
        pass

    @staticmethod
    def __is_email_str(self, email):
        return True if type(email) == str else False

EmailValidator.get_random_email()