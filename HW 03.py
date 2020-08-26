"""
Gabriel Meran
CS 100 2016F Section 021
HW 03 Sept 16,2016
"""

"""
Exercise 1
"""

a = 3
b = 4
c = 5

# 1
if(a<b):
    print('OK')
# 2
if(c<b):
    print('OK')
# 3
if((a+b)== c):
    print('OK')
# 4
if ((a**2 + b**2)== c**2):
    print('OK')


"""
Exercise 2
"""
# 1
if(a<b):
    print('OK')
else:
    print("NOT OK")
# 2
if(c<b):
    print('OK')
else:
    print("NOT OK")
# 3
if((a+b)== c):
    print('OK')
else:
    print("NOT OK")
# 4
if ((a**2 + b**2)== c**2):
    print('OK')
else:
    print("NOT OK")

"""
Exercise 3
"""

import turtle
s = turtle.Screen()
t = turtle.Turtle()

shape = input( 'Do you want your shape to a line, a triangle, or a square:')
length = int(input('Enter the length of the turtle line you want :'))
width = int(input('Enter the width of the turtle line you want :'))
color = input('Enter the color for the turtle line you want :')

t.pencolor(color)
t.pensize(width)
if( shape == 'line'):
    t.forward(length)
elif(shape == 'triangle'):
    t.forward(length)
    t.right(120)
    t.forward(length)
    t.right(120)
    t.forward(length)
elif(shape == 'square'):
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
else :
    print('That shape was not available in your choices')



