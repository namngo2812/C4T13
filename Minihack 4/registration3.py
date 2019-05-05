a = input("Your username: ")
while True:
    b = input("Your password: ")
    print(b)  
    if b.isalpha() == False or len(b) <=8:
        print("Invalid")
    else:
        print("valid")
        break

c = input("Re-enter your password: ")
while b != c:
    print("your password does not match!")
    c =  input("Re-enter your password: ")
    break

d = input("Your e-mail: ")
while True:
    if "@" not in d and "." not in d:
        print("Invalid")
        d = input("Your e-mail: ")
    else:
        print("valid")
        break
print("success")
