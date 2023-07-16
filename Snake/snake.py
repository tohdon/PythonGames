import signal,sys,time
import curses as c
from curses import KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_UP
from random import randint

c.initscr()
win = c.newwin(20, 60, 0, 0)
win.keypad(1)
c.noecho()
c.curs_set(0)
win.border(0)
win.nodelay(1)
snake = [[4, 10], [4, 9], [4,8]]
food = [10,20]
win.addch(food[0], food[1], 'O')
score = 0
key = KEY_RIGHT
                          
terminate = False                            

def signal_handling(signum,frame):           
    global terminate                         
    terminate = True                         

signal.signal(signal.SIGINT,signal_handling) 
try:
    while key != 27:
        win.border(0)
        win.addstr(0, 2, 'Score: '+ str(score) + ' ')
        win.addstr(0, 27,' SNAKE ')
        win.timeout(100)
        default_key = key
        event = win.getch()
        if terminate:
            prin("Break")
            break       
       
        if snake[0] in snake[1:]:
            break
        key = key if event == -1 else event
        if key not in [KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, 27]:
            key = default_key
        if snake[0][0] == 0:
            snake[0][0] = 18
        if snake[0][0] == 19:
            snake[0][0] = 1
        if snake[0][1] == 0:
            snake[0][1] = 58
        if snake[0][1] == 59:
            snake[0][1] = 1        
        snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1) , snake[0][1] + (key == KEY_RIGHT and 1) + (key == KEY_LEFT and -1)])
        if snake[0] == food:
            food = []
            score += 1 
            #while food == []:
            x1 = randint(1, 18)
            y1 = randint(1, 48)
            food = [x1,y1]
            print(x1)
            print(y1)
            if food in snake:
                 print("eat")
                 food = []
            win.addch(food[0], food[1], 'O')
            
        else:
            last = snake.pop()
            win.addch(last[0], last[1], ' ')
            
        win.addch(snake[0][0], snake[0][1], 'X')
        
    c.endwin()
except KeyboardInterrupt:
    pass
except curses.error:
    print ("cursors error")
finally:
    print('Exit Game with Ctrl+C!')
    sys.exit(0)
