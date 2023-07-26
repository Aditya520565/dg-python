from turtle import *

pensize(5)
speed('fastest')
bgcolor('grey')
pencolor('black')

for i in range(6):
    lt(60)
    fd(120)
    for i in range(6):
        lt(60)
        fd(90)


hideturtle()
mainloop()