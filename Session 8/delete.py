items = ['com', 'bun', 'pho', 'chao']

# #1. Index-based
# i = 2
# items.pop(i)
# print(items)

#2. Value-based
items_to_delete = 'pho'
items.remove(items_to_delete)
print(*items, sep = ',')