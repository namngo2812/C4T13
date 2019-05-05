# while True:
#     password = input("Your password: ")
#     print(password)
#     if password.isalpha()==False:
#         print("Valid")
#         break
#     else:
#         print("Invalid")



a = "valid"
b = "invalid"
while True:
    password = input("Your password: ")
    print(password)  
    if password.isalpha()==False and len(password) <=8:
        print(b)
    else:
        print(a)
        break