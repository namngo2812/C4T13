items = ['com', 'pho', 'chao', 'com rang']
print(*items, sep=',') # separator = sep

#index

print("Index 1")
print(items[1])

print("Index 0")
print(items[2])

print("Index 3")
print(items[3])

# items[-1] là lặp lại 

i = int(input("Enter index: "))
print(items[i])