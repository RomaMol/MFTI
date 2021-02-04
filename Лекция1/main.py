# This is a sample Python script.
import turtle


def david_star():

    for step in range(6):
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(50)
            turtle.left(360/3)
        turtle.end_fill()
        turtle.forward(50)
        turtle.right(60)

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    turtle.shape('turtle')
    turtle.shapesize(2)
    turtle.color('green', 'yellow')
    turtle.speed(10)

    david_star()
    turtle.backward(200)
    david_star()

    turtle.done()




if __name__ == '__main__':
    print_hi('PyCharm')
