import random
word = input('dien mot tu bat ky: ')

shuffled = list(word)

random.shuffle(shuffled)
print("shuffled: ", shuffled)

shuffled = ''.join(shuffled)
print(shuffled)