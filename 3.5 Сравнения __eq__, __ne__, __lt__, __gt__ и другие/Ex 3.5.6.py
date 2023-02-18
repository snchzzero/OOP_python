stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]


class StringText:
    def __init__(self, lst_words):
        self.words = lst_words

    def __gt__(self, other):
        return len(self.words) > len(other.words)

    def __ge__(self, other):
        return len(self.words) >= len(other.words)

    def __len__(self):
        return len(self.words)


lst_text = [StringText(lst_words) for lst_words in  [i.replace("–", "").replace('?', "").replace("!", "").
                                                     replace(",", "").replace(".", "").replace(";", "").split()
                                                     for i in stich]]
lst_text_sorted = sorted(lst_text, key=lambda x: len(x), reverse=True)

lst_text_sorted = [" ".join(obj.words) for obj in lst_text_sorted]




st1 = StringText(['Я', 'к', 'вам', 'пишу', 'чего', 'же', 'боле'])
st2 = StringText(['Что', 'я', 'могу', 'еще', 'сказать'])
print(st1 < st2)


