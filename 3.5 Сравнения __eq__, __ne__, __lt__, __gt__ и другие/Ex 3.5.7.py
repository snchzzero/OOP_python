class Morph:
    def __init__(self, *args):
        self.list = [word.lower() for word in list(args)]

    def add_word(self, word):
        self.list.append(word.lower())

    def get_words(self):
        return tuple(self.list)

    def __eq__(self, other):
        return other.lower() in self.list

mw = Morph("связь", "связи", "связью", "связей", "связям", "связями", "связях")
mw2 = Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах')
mw3 = Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах')
mw4 = Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах')
mw5 = Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')
dict_words = [mw, mw2, mw3, mw4, mw5]
text = input()
text = [word.replace('!', '').replace('.', '').replace(',', '').replace('?', '').replace('-', '').replace('"', '').replace("'", '').lower() for word in text.split()]
total = 0
for word in text:
    for obj in dict_words:
        for word_obj in obj.list:
            if word == word_obj:
                total += 1
                break

print(total)


# mw.add_word("cerf")
# print(mw.get_words())
# print(mw == 'связям')
# print(mw == 'связямм')
# print(mw != 'связямм')
# print()
# print('связям' == mw)
# print('связямм' == mw)
# print('связямм' == mw)
