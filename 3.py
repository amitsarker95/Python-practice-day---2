list1 = ["M", "na", "i", "Bo"]
list2 = ["y", "me", "s", "nd"]

finalResult = []

for i in range(len(list1)):
    tmp = list1[i]+list2[i]
    finalResult.append(tmp)

print(finalResult)