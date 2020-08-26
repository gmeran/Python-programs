import turtle
t = turtle.Turtle()
for i in range(4):
    if i%3 == 0:
       t.forward(100)
       t.left(120)
    elif i%3 == 1:
         t.forward(100)
         t.left(60)
    else:
       t.left(60)
