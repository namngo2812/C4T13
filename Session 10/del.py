John_Wick = {
    'actor' : 'Keanu Reeves',
    'description' : 'a sad man',
    'life style' : 'homeless', 
}

print(John_Wick)

# John_Wick.pop('actor')
# print(John_Wick)

a =  input('delete a key: ')
b =  input('delete a des: ')

print("*"*50)

John_Wick[a] = b
print(John_Wick)
print("*"*50)
John_Wick.pop(a)

print(John_Wick)