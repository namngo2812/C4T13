while True:
    txt = input("Your year of birth: ")
    print(txt)
    if txt.isalpha()==False:
        print("Valid")
        break
    else:
        print("Invadlid")
