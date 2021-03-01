counter = int(input("write a number: "))
dic1 = {}

for item in range(1,counter+1):
     dic1.update({item: item*item})

print(dic1)