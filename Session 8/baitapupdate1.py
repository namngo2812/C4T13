items = ['sport', 'lol', 'bts'] 

print(items)

i = input("New stuff: ")
items.append(i)

print(*items, sep = ',')

