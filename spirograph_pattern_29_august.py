import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
spiro = turtle.Turtle()
spiro.speed(0)

# Draw a spirograph pattern
for _ in range(60):
    spiro.color(random.choice(["red", "blue", "green", "orange", "purple", "yellow"]))
    spiro.circle(100)
    spiro.left(6)

turtle.done()
