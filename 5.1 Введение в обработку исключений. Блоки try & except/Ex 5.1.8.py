lst_in = input().split()
# print(int('-15'))
# a = "8 11 abcd -7.5 2.0 -5"
# lst_in = a.split()
# print(lst_in)


def integer(x):
    try:
        x = int(x)
        return x
    except Exception:
        return False


summa_of_integer = sum(list(map(lambda x: int(x), list(filter(lambda x: integer(x), lst_in)))))
print(summa_of_integer)
