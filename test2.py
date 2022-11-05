x = input().split(',')
print(x)
y = int(input())
print(y)
l1 = list()
for i in range(len(x)):
    for j in range(len(x)):
        if int(x[i]) + int(x[j]) == int(y) and i != j:
            if i not in l1 and len(l1) < 2:
                l1.append(i)
            if j not in l1 and len(l1) < 2:
                l1.append(j)
print(l1)