entertainment= [
{
    'name' : 'john wick',
    'year' :  '2014',
    'actor' : 'Keanu Reeves'
},
{   
    'name' : 'harry potter',
    'author' : 'j.k. Rowling',
    'year'  : '2003'
}
]

entertainment.append({
    'name' : 'Nancy',
    'author' : 'robert',
    'year'  : '2003'
})

# for i in range (len(entertainment)):
#     for k in entertainment[i].keys():
#         print(k.split(" "))
#     print()
#     for v in entertainment[i].values():
#         print(v.split(" "))

entertainment[0].pop('name') #để xoá 1 key và 1 value trong dict
# del entertainment[0]["name"] để xoá 1 key và 1 value trong dict
print(entertainment)

for i in range (len(entertainment)):
    for k, v in entertainment[i].items():
        print(k, v)