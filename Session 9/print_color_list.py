items = ['red', 'green', 'blue', 'teal']
print(items)

Your_new_color = input('Your new color: ')
items.append(Your_new_color)
print( 'Your new list: ',*items, sep = ',')