entertainment = [
{
    'question': 'what movie is it?',
    'answer':   ['john wick', 'lucy', 'hangover'],
    'rightAnswer':1
},
{
    'question': 'con cho may chan?',
    'answer':   ['1', '2', '3', '4'],
    'rightAnswer':4
},
{
    'question': 'con ga may chan?',
    'answer':   ['1', '2', '3', '4'],
    'rightAnswer':2
},
{
    'question': 'con meo khuyet tat 1 chan co may chan?',
    'answer':   ['1', '2', '3', '4'],
    'rightAnswer':3
},
{
    'question': 'con ruoi co may chan',
    'answer':   ['1', '2', '3', 'vo so'],
    'rightAnswer':2

},

]
countTrue=0
totalRightAns = len(entertainment)
for i in range(len(entertainment)):
    print(entertainment[i]['question'])
    x = entertainment[i]["answer"]
    for i,item in enumerate(x):
        print(i+1,".",item)
    rightAnswers = entertainment[i]["rightAnswer"]
    
    n = int(input("Your answer:"))
    if n == rightAnswers-1:
        # print('Hura')
        countTrue+=1
        print("Dung roi nhe ^^")
    else:
        print(':(')    
print("Your point is",countTrue)
print("Your percent is",str(countTrue/totalRightAns*100)+"%")

