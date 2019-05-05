items = [5, 1 ,82, 9, -1, 120]
print(*items)

number = int(input('enter a number:'))

# for i in range(len(items)):
if number in items:
    # if items[i]== number:
    print('Found, position',end=" ")
    for i in range(len(items)):
        if items[i] == number:
            print(i+1)
            break
else:
    print('Not found')