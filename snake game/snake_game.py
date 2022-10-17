from tkinter import *
import random

G_WIDTH=700
G_HEIGHT=600
S_SPEED =90
SPACE_SIZE=25
BODY_PARTS=3
SNAKE_COLOR="#95CD41"
FOOD_COLOR="#EA5C2B"
BG_COLOR="#F6D860"

class Snake:
    def __init__(self):
        self.body_size=BODY_PARTS
        self.coordinates=[]
        self.squares=[]

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])
        
        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snake")
            self.squares.append(square)
class Food:
    def __init__(self):
        x=random.randint(0,(G_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y=random.randint(0,(G_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE

        self.coordinates=[x,y]
        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag="food")

def next_turn(snake,food):
    x,y=snake.coordinates[0]
    if direction =='up':
        y-=SPACE_SIZE
    elif direction =='down':
        y+=SPACE_SIZE
    elif direction =='left':
        x-=SPACE_SIZE
    elif direction =='right':
        x+=SPACE_SIZE

    snake.coordinates.insert(0,(x,y))
    square =canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)
    snake.squares.insert(0,square)
    
    if x==food.coordinates[0] and y==food.coordinates[1]:
        global score
        score+=1
        label.config(text=f"Score : {score}")
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_collisons(snake):
        game_over()
    else:
        window.after(S_SPEED,next_turn,snake,food)

def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisons(snake): 
    x,y=snake.coordinates[0]

    if x<0 or x>=G_WIDTH:
        return True
    elif y<0 or y>=G_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x==body_part[0] and y==body_part[1]:
            return True
    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,
        font=('times new roman',50),text='GAME OVER',fill='red',tag='gameover')

def main_game():
    global window
    window =Tk()
    
    window.title("Snake Game")
    window.resizable(False,False)
    
    global score
    score =0
    
    global direction
    direction = 'down'
   
    global label
    label=Label(window,text=f"Score : {score}",font=('consolas',18))
    label.pack()
    
    global canvas
    canvas = Canvas(window,bg=BG_COLOR,height=G_HEIGHT,width=G_WIDTH)
    canvas.focus()
    canvas.pack()
    
    window.update()
    
    w_width=window.winfo_width()
    w_height=window.winfo_height()
    s_width=window.winfo_screenwidth()
    s_height=window.winfo_screenheight()
    
    x=int((s_width/2)-(w_width/2))
    y=int((s_height/2)-(w_height/2))
    
    window.geometry(f"{w_width}x{w_height}+{x}+{y}")
    
    window.bind('<Left>',lambda event: change_direction('left'))
    window.bind('<Right>',lambda event: change_direction('right'))
    window.bind('<Up>',lambda event: change_direction('up'))
    window.bind('<Down>',lambda event: change_direction('down'))
    window.bind('<Return>',lambda event: main_game())

    snake = Snake()
    food =Food()
    next_turn(snake,food)

    window.mainloop()

main_game()
