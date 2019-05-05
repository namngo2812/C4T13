from random import randint, shuffle

words = ['cat', 'dog', 'cut', 'knife', 'Amsterdam', "integer"]


while True:
    wasd = words[randint(0, len(words) - 1  )] 
    
    wasd = list(wasd)
    shuffle(wasd) # dao thu tu cac phan tu trong 1 list
    wasd = ''.join(wasd) # noi cac phan tu cua list thanh 1 string
    
    
    print("shuffle: ", wasd)
    

    begin = input('work your brain out: ')
    if begin in words:
        print('Good job!')
    else:
        print('Noob!!')
        break
    
    



