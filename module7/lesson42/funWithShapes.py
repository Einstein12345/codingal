import turtle

t = turtle.Turtle()
t.speed(0)

# Square
for _ in range(4):
    t.forward(100)
    t.right(90)

# Triangle
t.penup()
t.goto(-150, 0)
t.pendown()
for _ in range(3):
    t.forward(100)
    t.left(120)
turtle.Screen().bgcolor("green")
turtle.done()