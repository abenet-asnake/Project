import turtle

def draw_branch(branch_length):
    if branch_length > 10:
        turtle.forward(branch_length)
        turtle.left(30)
        draw_branch(branch_length - 15)
        turtle.right(60)
        draw_branch(branch_length - 15)
        turtle.left(30)
        turtle.backward(branch_length)
    else:
        # Draw a leaf
        turtle.color("green")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.color("brown")

# Set up the turtle
turtle.left(90)
turtle.up()
turtle.backward(100)
turtle.down()
turtle.color("brown")

# Draw the tree

# Draw the tree
draw_branch(70)

turtle.done()
# ...existing code...