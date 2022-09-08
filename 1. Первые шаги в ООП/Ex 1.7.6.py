class Viber:
    Mlist = list()

    @classmethod
    def add_message(cls, msg):
        cls.Mlist.append(msg)
        print(cls.Mlist)

    @classmethod
    def remove_message(cls, msg):
        cls.Mlist.remove(msg)
        print(cls.Mlist)

    @classmethod
    def set_like(cls, msg):
        if msg in cls.Mlist:
            if msg.fl_like == True:
                msg.fl_like = False
            else:
                msg.fl_like = True

    @classmethod
    def show_last_message(cls,number):
        for i in number:
            print(cls.Mlist[-i])

    @classmethod
    def total_messages(cls):
        print(len(cls.Mlist))
        return len(cls.Mlist)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)

# assert hasattr(Viber, 'show_last_message'), "отсутствует метод show_last_message"
#
# msg = Message("Всем привет!")
# Viber.add_message(msg)
# assert Viber.total_messages() == 1, "сообщение не было добавлено: некорректно работает метод add_message"
#
# Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# assert Viber.total_messages() == 3, "неверное число сообщений: некорректно работает метод add_message"
#
# assert msg.fl_like == False, "лайка по умолчанию не должно быть - значение False"
# Viber.set_like(msg)
# assert msg.fl_like == True, "лайк не проставился: некорректно работает метод set_like"
# Viber.set_like(msg)
# assert msg.fl_like == False, "лайк не убрался при повторном вызове метода set_like"
# Viber.remove_message(msg)
#
# assert Viber.total_messages() == 2, "неверное число сообщений: некорректно работает метод remove_message"



