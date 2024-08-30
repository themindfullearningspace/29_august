import turtle
import random

# Create a turtle
mandelbrot = turtle.Turtle()
mandelbrot.speed(10)
# mandelbrot.color("white")


# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Draw Mandelbrot - like pattern
for i in range(500):
  mandelbrot.color(random.choice(["red", "blue", "green", "orange", "purple", "yellow"]))
  mandelbrot.forward(i)
  mandelbrot.left(121)

turtle.done()