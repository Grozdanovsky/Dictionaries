dic1={1:10, 2:20, 3:30, 4:40, 5:50,6:60}
dic2 = {}
for key in dic1.keys():
    print(key)

for value in dic1.values():
    print(value)

for key,value in dic1.items():
    print(key,value)
    dic2.update({value:key})

print(dic2)
