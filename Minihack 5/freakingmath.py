from random import randint
while True:

    a = randint(1, 100)
    b = randint(1, 100)
    x = randint(-1,1)
    
    sign = randint(1,2)

    if sign == 1 :
        c = a - b + x
        print(a,  "-", b, "=", c)
    elif sign != 1:
        c = a + b + x
        print(a,  "+", b, "=", c)

    userchoice = input("Answer right or wrong:  ")
    if userchoice == "right" and x == 0: 
        print("Awesome")
    elif userchoice == "wrong" and x != 0:
        print("Awesome")
    else:
        print("You suck!")
        break