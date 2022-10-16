import turtle

# creating a custom turtle variable so I don't have to recall turtle so often 
bruno = turtle.Turtle()
bruno.color('red')
bruno.pensize(5)

bruno.begin_fill()
bruno.fillcolor('yellow') 
# using the for loop to create a square shape
for x in range(4):
    bruno.forward(100)
    bruno.right(90)
bruno.end_fill()

# moving turtle to a different space on the GUI so the next shape doesn't draw in the earlier
bruno.penup()
bruno.goto(-250, 190)
bruno.pendown()

bruno.shape('turtle') #assigning a new turtle shape 
bruno.pencolor('blue')
# using the for loop to create the the "Star of David" shape
for x in range(8):
    bruno.forward(100)
    bruno.right(135)

turtle.done()