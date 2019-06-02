dict_list = {
    "question": "How many legs an octopus has?",
    "answers":["one leg", 'two legs', 'three legs', 'four legs'],    
}
print(dict_list["question"])
x = dict_list["answers"]
for i,item in enumerate(x):
    print(i+1,".",item)
count=0
while True:
    print("Lan choi thu",count+1)
    n = int(input("Your answer:"))
    rightAnswer = 4
    if n == 4:
        print('Hura')
        break
    else:
        count+=1
        print(':(')    


