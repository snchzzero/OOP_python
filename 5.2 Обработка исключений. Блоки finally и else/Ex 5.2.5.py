#list_input = [5.4, "3.2"]
list_input = [8, 3.0]
#list_input = input().split()
try:
    for index, elem in enumerate(list_input):
        if '.' in str(elem):
            list_input[index] = float(elem)
        elif not isinstance(elem, bool):
            list_input[index] = int(elem)
    result = sum(list_input)
except:
    result = str(list_input[0]) + str(list_input[1])
finally:
    print(result)


