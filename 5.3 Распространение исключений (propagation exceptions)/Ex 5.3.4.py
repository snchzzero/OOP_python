import sys
def input_int_numbers(list_input):
    result = []
    try:
        for elem in list_input.split():
            result.append(int(elem))
        return tuple(result)
    except:
        raise TypeError('все числа должны быть целыми')

for list_input in sys.stdin:
    try:
        res = input_int_numbers(list_input)
        print(*res)
        break
    except:
        continue

