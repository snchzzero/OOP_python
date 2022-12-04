class WordString:
    def __init__(self, str=''):
        self.__string_list = str.split(' ')

    @property
    def string(self):
        return ' '.join(self.__string_list)

    @string.setter
    def string(self, str):
        self.__string_list.clear()
        self.__string_list = str.split(' ')

    def __len__(self):
        total = 0
        for string in self.__string_list:
            if string not in " ":
                total += 1
        return total


    def __call__(self, index):
        if 0 <= index < len(self.__string_list):
            return self.__string_list[index]

# words = WordString()
# words.string = "Курс по Python ООП"
# print(words.string)
# print(len(words))
# print(words.words(3))
words = WordString()
words.string = "Курс                 по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")