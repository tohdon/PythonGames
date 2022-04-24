import turtle as t

def rect(horizontial, vertical, color):
    t.pd()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(horizontial)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
t.bgcolor('Dodger blue')

#feet
t.goto(-100, -150)
rect(50, 20, 'blue')
t.goto(-30, -150)
rect(50, 20, 'blue')

#legs
t.goto(-25, -50)
rect(15, 100, 'green')
t.goto(-55, -50)
rect(15, 100, 'green')
#body
t.goto(-90,100)
rect(100, 150, 'yellow')
#arm
t.goto(-150, 70)
rect(60,15, 'green')
t.goto(-150, 110)
rect(15, 40, 'green')

t.goto(10, 70)
rect(60,15, 'green')
t.goto(55, 110)
rect(15, 40, 'green')
#neck
t.goto(-50, 120)
rect(15, 20, 'grey')
#head
t.goto(-85, 170)
rect(80, 50, 'red')
#eyes
t.goto(-60, 160)
rect(30,10, 'red')
t.goto(-55, 155)
rect(5,5, 'black')
t.goto(-40, 155)
rect(5,5, 'black')
#mouth
t.goto(-65, 135)
rect(40,5, 'black')
t.hideturtle()