

import random

n = random.randint(0, 100)
print(n)

if n < 30:
    print("Sunny")
elif n > 30 and n <= 60:
    print("Cloudy")
else:
    print("Rainy")