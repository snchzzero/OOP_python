class NewList():
    def __init__(self, list=[]):
        self.list = list

    def get_list(self):
        return self.list

    def __rsub__(self, other):
        clist = other.copy()
        for i in self.list:
            for j in range(len(clist)):
                if i == clist[j] and type(i) == type(clist[j]):
                    clist.pop(j)
                    break
        return NewList(clist)


    def __sub__(self, other):

        if type(other) == list:
            clist = self.list.copy()
            for i in other:
                for j in range(len(clist)):
                    if i == clist[j] and type(i) == type(clist[j]):
                        clist.pop(j)
                        break

        else:
            clist = self.list.copy()
            for i in other.list:
                for j in range(len(clist)):
                    if i == clist[j] and type(i) == type(clist[j]):
                        clist.pop(j)
                        break

        return NewList(clist)












# lst = NewList() # пустой список
# lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями
# print(lst)
# print("sdsad")

# lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
# lst2 = NewList([0, 1, 2, 3, True])
# res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
# print(res_1.get_list())
#
# lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
# print(lst1.get_list())
#
# res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
# print(res_2.get_list())
#
# res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
# print(res_4.get_list())

lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])

assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"

res1 = lst1 - lst2
res2 = lst1 - [0, True]
res3 = [1, 2, 3, 4.5] - lst2
lst1 -= lst2

assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"

