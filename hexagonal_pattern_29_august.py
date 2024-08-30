import turtle

# Create a turtle
hexagon = turtle.Turtle()
hexagon.speed(10)
hexagon.color("cyan")

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Function to draw a hexagon
def draw_hexagon():
  for _ in range(6):
    hexagon.forward(100)
    hexagon.right(60)
    
    
# Draw the hexagonal pattern
for i in range(36):
  draw_hexagon()
  hexagon.right(10)
  
  
turtle.done()