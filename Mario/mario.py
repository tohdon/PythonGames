import turtle

Pen = turtle.Turtle()
grid_of_pixels2 = [[1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1], [1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1], [1,1,1,0,0,0,3,3,3,3,3,0,3,1,1,1],
                    [1,1,0,3,0,3,3,3,3,3,3,0,3,3,3,1], [1,1,0,3,0,0,3,3,3,3,3,3,0,3,3,3], [1,1,0,0,3,3,3,3,3,3,3,0,0,0,0,1],
                    [1,1,1,1,3,3,3,3,3,3,3,3,3,3,1,1], [1,1,1,0,0,2,0,0,0,0,2,0,1,1,1,1], [1,1,0,0,0,2,0,0,0,0,2,0,0,0,1,1],
                    [0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0], [3,3,3,0,2,3,2,2,2,2,3,2,0,3,3,3], [3,3,3,3,2,2,2,2,2,2,2,0,3,3,3,3],
                    [1,1,1,2,2,2,1,1,1,1,2,2,2,1,1,1], [1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1], [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0]]
palette= []
palette = ["#4B610B","#FFFF00","#DF0101","#FE9A2E"]
boxSize = 10
Pen.speed(10)
Pen.color(0,0,0)
Pen.penup()
Pen.forward(-100)
Pen.setheading(90)
Pen.forward(100)
Pen.setheading(0)

def box(Dimension):
    Pen.begin_fill()
    Pen.forward(Dimension)
    Pen.left(90)
    Pen.forward(Dimension)
    Pen.left(90)
    Pen.forward(Dimension)
    Pen.left(90)
    Pen.forward(Dimension)
    Pen.end_fill()
    Pen.setheading(0)
    
    
for i in range(0, len(grid_of_pixels2)):
    for j in range(0, len(grid_of_pixels2[i])):
        val = grid_of_pixels2[i][j]
        Pen.color(palette[val])
        box(boxSize)
        Pen.penup()
        Pen.forward(boxSize)
        Pen.pendown()
    Pen.setheading(270)
    Pen.penup()
    Pen.forward(boxSize)
    Pen.setheading(180)
    Pen.forward(boxSize*len(grid_of_pixels2[i]))
    Pen.setheading(0)
    Pen.pendown()

input('Press <ENTER> to continue')
