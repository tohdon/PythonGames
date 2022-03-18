import turtle as t1
import random
caterpillar = t1.Turtle()
t1.bgcolor('lightgrey')
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.pu()
caterpillar.hideturtle()
leaf = t1.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20), (6,18), (2,14))
t1.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.speed(0)
leaf.pu()
leaf.hideturtle()
game_started = False
text_turtle = t1.Turtle()
text_turtle.write('Pres SPACE to start', align='center',font=('Arial', 16, 'bold'))
text_turtle.hideturtle()
score_turtle = t1.Turtle()
score_turtle.speed(0)
score_turtle.hideturtle()

def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() ==180:
        caterpillar.seth(90)
def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() ==180:
        caterpillar.seth(270)
def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() ==270:
        caterpillar.seth(180)
def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() ==270:
        caterpillar.seth(0)
def place_leaf():
    leaf.ht()
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.st()
def outside_window():
    left_wall = -t1.window_width()/2
    right_wall = t1.window_width()/2
    top_wall = t1.window_height()/2
    bottom_wall = -t1.window_height()/2
    (x, y) = caterpillar.pos()
    outside = \
            x< left_wall or \
            x> right_wall or \
            x< bottom_wall or \
            x> top_wall
    return outside
  
def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    caterpillar.pu()
    caterpillar.hideturtle()
    caterpillar.write('GAME OVER', align='center',font=('Arial', 30, 'normal'))
def display_score(current_score):
    score_turtle.clear()
    score_turtle.pu()
    x = (t1.window_width()/2) - 50
    y = (t1.window_height()/2) - 50
    score_turtle.setpos(x,y)
    score_turtle.write("Score:" + str(current_score), align='right',font=('Arial', 40, 'bold'))
  
def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    score = 0
    text_turtle.clear()
    t_speed = 2
    t_length = 3
    caterpillar.shapesize(1, t_length, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()
    while True:
        caterpillar.forward(t_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            t_length = t_length + 1
            caterpillar.shapesize(1, t_length,1 )
            t_speed= t_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            break
      
t1.onkey(start_game, 'space')

t1.onkey(move_up, 'Up')
t1.onkey(move_down, 'Down')
t1.onkey(move_right, 'Right')
t1.onkey(move_left, 'Left')
t1.listen()
t1.mainloop()
      
