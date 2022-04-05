# Name: Ritik Kumar
# email : ritikkhanna079@gamil.com
# Pattern Print

import turtle
t= turtle.Turtle()
list = ['red','green', 'blue', 'white','yellow']
window = turtle.Screen()
window.bgcolor("black")
t.speed(11)
for i in range (350):
    t.color(list[i%5])
    t.pensize(i%5 +1 )
    t.forward(i)
    t.left(70)