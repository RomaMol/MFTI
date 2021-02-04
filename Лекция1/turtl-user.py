import turtle


def turtle_user():
    turtle.shape()
    turtle.shapesize(2)
    turtle.color('green')

    for step in range(6):
        turtle.forward(50)
        turtle.right(60)

    turtle.done()
