import sys
class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        #lst_in = list(map(str.strip, sys.stdin.readlines()))
        lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
                  'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
                  'Python ООП; Балакирев С.М.; 2022',
                  'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']
        for i in lst_in:
            mail_from = i.split(';')[0]
            title = i.split(';')[1].lstrip()
            content = i.split(';')[2].lstrip()
            self.inbox_list.append(MailItem(mail_from, title, content))

class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        if self.is_read: return True
        else: return False


lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
          'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
          'Python ООП; Балакирев С.М.; 2022',
          'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']

mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(1)
mail.inbox_list[-1].set_read(2)
for i in mail.inbox_list:
    print(bool(i))

inbox_list_filtered = list(filter(lambda x: x,mail.inbox_list))
print(inbox_list_filtered)