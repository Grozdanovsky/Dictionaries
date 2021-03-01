list_keys = [1, 2, 3, 4, 5, 6]
list_values = [10, 20, 30, 40, 50, 60]
dict1 = {}
for item in range(len(list_keys)):
    dict1.update({list_keys[item]:list_values[item]})

print(dict1)


# dict1 = dict(zip(list_keys, list_values))
# print(dict1)
# print(zip(list_keys,list_values))