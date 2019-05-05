items = ['chao', 'bun', 'pho', 'com rang']

menu = input('dien vao menu: ').split(',')
for i in menu:
    items.append(i)
print(*items, sep = ',')

check = input('nhap 1 item: ')
print(check)
if check not in items:
    print("error")
else:
    print('continue')

add = input( 'add more items: ')
items.append(add)
print(*items, sep = ',')

delete = input('delete your items: ')
print(delete)

items.remove(i)
print(*items, sep = ',')
