from turtle import *
from random import randint, choice

r = randint(0  ,2)
print(r)
colors = ['green', 'red', 'blue']

# print(colors[randint(0,2)])

# print(choice(colors))
shape('turtle')
begin_fill()
for i in range(0, 2):
    pen(fillcolor = colors[randint(0, 2)], pencolor = colors[randint(0, 2)], pensize = 5)
    forward(200)
    left(170)
# while True:
#     pen(fillcolor = colors[randint(0, 2)], pencolor = colors[randint(0, 2)], pensize = 5)
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
end_fill()

mainloop()