import turtle

turtle.pendown()
def up():
    turtle.setheading(0)
    turtle.forward(2)
   # write your code here!
def down():
    turtle.setheading(180)
    turtle.forward(2)
   # write your code here!
def left():
    turtle.setheading(-90)
    turtle.forward(2)
   # write your code here!
def right():
    turtle.setheading(90)
    turtle.forward(2)
   # write your code here!

turtle.onkeypress(up, 'd')

turtle.onkeypress(down, 'a')


turtle.onkeypress(right, 'w')


turtle.onkeypress(left, 's')




turtle.listen() 

turtle.mainloop()
