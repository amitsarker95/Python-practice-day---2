sample_dict = {'a': 100, 'b': 200, 'c': 300}
searchVal = 100
isFound = False
for i in sample_dict:
    if sample_dict[i] == searchVal:
        isFound = True


if isFound != False:
    print("Present")
else:
    print("Not Present")