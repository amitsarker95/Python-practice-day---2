sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
    }

keys = ["name", "salary"]

values = []

for i in sample_dict:
    if i in keys:
        values.append(sample_dict[i])

newDict = dict(zip(keys,values))
print(newDict)