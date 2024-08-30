import turtle

# Create a turtle
star = turtle.Turtle()
star.speed(10)
star.color("yellow")



# Set up the screen
screen = turtle.Screen()
screen.bgcolor("blue")

# Draw a star polygon
for i in range(18):
  star.forward(100)
  star.right(145)
  
turtle.done()