#lst_in = input().split()
a = "1 -5.6 True abc 0 23.56 hello"
lst_in = a.split()

lst_out = [(int(i) if '.' not in i else float(i)) if all([_ in '1234567890.-' for _ in i]) else i for i in lst_in]
# print(lst_out)



def integer_float(x):
    try:
        x = int(x)
        return x
    except ValueError:
        try:
            x = float(x)
            return x
        except ValueError:
            return x

lst_out = list(map(lambda x: integer_float(x), lst_in))

print(lst_out)
