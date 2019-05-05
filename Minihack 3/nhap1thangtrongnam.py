

while True:
    a = int(input("enter 1 month <= 12: "))
    if a <= 12:
        if a in (1, 3, 5, 7, 8, 10, 12):
            print("31 days")
        elif a in (4, 6, 9, 11):
            print("30 days")
        else:
            print("28 days")
