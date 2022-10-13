list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

revList = list(reversed(list2))

tmp = tuple(zip(list1,revList))

for i in tmp:
    print(f"{i[0]} {i[1]}")