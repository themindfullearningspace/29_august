import turtle

# Creat a turtle
tree = turtle.Turtle()
tree.speed(10)
tree.color("green")
# tree.pensize(5)
tree.left(90) # It will rotate 90 degree towards left.
# tree.penup()
# tree.backward(100)
# tree.pendown()

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("Black")

# Function to draw a fractal tree

def draw_tree(branch_length):
  if branch_length > 5:
# Moves the turtle forward by the current 'branch_length', drawing a line that represents the branch.
# Recursive Function to Draw the tree
    tree.forward(branch_length)

# Drawing the Right Sub-Branch
    tree.right(20)
    draw_tree(branch_length - 15)
    
# Drawing the Left Sub-Branch
    tree.left(40)
    draw_tree(branch_length - 15)
    
# Returning to Original Position and Angle
    tree.right(20)
    tree.backward(branch_length)
    
draw_tree(100)
turtle.done()