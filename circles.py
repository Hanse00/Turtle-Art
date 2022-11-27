import turtle, random

def draw():
    totalangle = 0
    turtle.penup()
    turtle.forward(100)
    turtle.right(90)
    while totalangle < 360:
        d = random.randint(25, 250)
        turtle.pendown()
        turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.begin_fill()
        turtle.circle(d)
        turtle.end_fill()
        turtle.penup()
        newangle = random.randint(30, 45)
        turtle.circle(-d, newangle)
        totalangle += newangle


def main():
    turtle.screensize(500, 500)
    turtle.hideturtle()
    turtle.colormode(255)
    turtle.speed(0)
    draw()
    input()
    turtle.getcanvas().postscript(file="circles.eps")

if __name__ == "__main__":
    main()
