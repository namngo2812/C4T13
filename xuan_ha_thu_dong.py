season = int(input("nhập 1 tháng trong năm: "))

print(season)

if season <= 3 and season > 0:
    print("mùa xuân")
elif season <= 6:
    print("mùa hạ")
elif season <=10:
    print("mùa thu")
else:
    print("mùa đông")

