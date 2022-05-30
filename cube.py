import turtle
turtle.pensize(2)
turtle.bgcolor("black")
turtle.pencolor("white")
turtle.speed(100)
def animated():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

def s():
    for i in range(4):
       turtle.right(180)
       animated()
while True:
    turtle.right(10)
    s()
turtle.done()            
