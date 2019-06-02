wokers = [
{
    "Name":"Huy",
    "Role":"Waiter",
    "Hour":12,
    "Salary":0.8
},
{
    "Name":"Tung",
    "Role":"Cook",
    "Hour":24,
    "Salary":1.5
},
{
    "Name":"Duc",
    "Role":"Manager",
    "Hour":20,
    "Salary":2,
}
]
# a1 =  {"Name":"Don",
#     "Role":"waiter",
#     "Hour":12,
#     "Salary":0.9,}

# a2 =  {"Name":"Duh??",
#     "Role":"waiter",
#     "Hour":14,
#     "Salary":0.7,}

# wokers.append(a1)
# wokers.append(a2)

print(wokers[0])
print(wokers[1])
print(wokers[2])
# print(wokers[3])
# print(wokers[4])
import math
sums = 0

#  print(wokers[3]) : in ra phan tu trong mot list

# remove_worker = wokers.pop(2)   dùng pop() để xoá 1 phần tử dict trong 1 dict list
# print(wokers)
# print(remove_worker)
for i in range (len(wokers)):
    s = wokers[i]["Salary"]
    h = wokers[i]["Hour"]
    su = s*h*30
    print(math.floor(su))
    sums += su 
print('Total: ',math.floor(sums))

