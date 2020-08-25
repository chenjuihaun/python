import turtle

# Create screen and turtle objects
screen = turtle.Screen()
screen.setup(500, 500)
myTurtle = turtle.Turtle()

# Move the turtle: draw a square
for color in ['red', 'blue', 'green', 'orange']:
    myTurtle.color(color)
    myTurtle.forward(100)
    myTurtle.left(90)

# Exit
screen.exitonclick()