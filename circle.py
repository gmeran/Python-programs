import turtle
s = turtle.Screen()
t = turtle.Turtle()

def drwCir(t,radius):
    t.penup()
    t.goto(0,100)
    t.pendown()
    t.circle(radius)
   
    
    


def drwCirs(t,numcirc,incre):
    t.pendown()
    radius = 50
    for i in range(numcirc):
        drwCir(t,radius)
        radius+=incre
drwCirs(t,10,25)
        
    
    


