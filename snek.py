import tkinter as tk
from tkinter import ttk
import random 
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 10
DELAY = 100
root = tk.Tk()
root.title("Змейка 3000")
label = tk.Label(text="Главное Меню")
label.pack()
current_buttons = []
buttons = ["Начать игру", "Настройки", "Выход"]
directions = ["Up", "Down", "Left", "Right"]


canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg = "black"
)
canvas.pack()
directions = ['Up', 'Down', 'Left', 'Right']
snake = [(100, 100), (90, 100), (80, 100)]
direction = 'Right'
score = 0
game_over = False


def create_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) *CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) *CELL_SIZE
        if (x, y) not in snake:
            return (x, y)
food = create_food()    

def draw_food():
    canvas.create_rectangle(
        food[0], food[1],
        food[0] + CELL_SIZE,
        food[1] + CELL_SIZE,
        fill='red',
        )

def draw_snake():
    for segment in snake:
        canvas.create_rectangle(
            segment[0], segment[1],
            segment[0] + CELL_SIZE,
            segment[1] +CELL_SIZE,
            fill='green',
            outline='darkgreen',
            )
def move_snake():
    head_x, head_y = snake[0]
    if direction == "Up":
        new_head = (head_x, head_y - CELL_SIZE)
    elif direction == "Down":
        new_head = (head_x, head_y + CELL_SIZE)
    elif direction == "Left":
        new_head = (head_x - CELL_SIZE, head_y)
    elif direction == "Right":
        new_head = (head_x + CELL_SIZE, head_y)
    snake.insert(0, new_head)
    if not check_food_collision():
        snake.pop()

def check_food_collision():
    global food, score
    if snake[0] == food:
        score += 1
        food = create_food()
        return True
    return False

def check_self_collision():
    return snake[0] in snake[1:]

def check_wall_collision():
    head_x, head_y = snake[0]
    return (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT
        )
def end_game():
    global game_over, score
    game_over = True
    if score % 10 == 1 and score % 100 != 11:
        ending = "очко"
    elif score % 10 in (2, 3, 4) and score % 100 not in (12, 13, 14):
        ending = "очка"
    else:
        ending = "очков"
    if check_self_collision():
        text= f"Игра окончена! Вы укусили сами себя!\nВаш счет: {score} {ending}!"
    elif check_wall_collision():
        text= f"Игра окончена! Вы врезались в стену!\nВаш счет: {score} {ending}!"
    else:
        text= f"Игра окончена! Вы врезались в стену!\nВаш счет: {score} {ending}!"       
    canvas.create_text(
        WIDTH//2, HEIGHT//2,
        text=text,
        fill="white",
        font=("Arial", 20)
        )

def reset_game():
    global game_over, score, snake, food
    food = create_food()
    game_over = False
    snake = [(100, 100), (90, 100), (80, 100)]
    direction = "Right"
    score = 0

def on_key_press(event):
    global direction
    key = event.keysym
    if key in directions:
        if (key == "Up" and direction != "Down" or
            key == "Down" and direction != "Up" or
            key == "Left" and direction != "Right" or
            key == "Right" and direction != "Left"):
            direction = key
    elif key == "space" and game_over:
        reset_game()
        main_menu()
root.bind("<KeyPress>", on_key_press)
                       
def clear_screen():
    canvas.delete("all")
    for btn in current_buttons:
        btn.destroy()
    current_buttons.clear()

def update_title():
    root.title(f"Score: {score}")

def settings():
    clear_screen()
    set_buttons = ["Уровень сложности", "Карта", "Графика", "Назад"]
    for i, text in enumerate(set_buttons):
        if text == "Назад":
            button = ttk.Button(text=f'{i+1}) {text}', command=main_menu)
        else:
            button = ttk.Button(text=f'{i+1}) {text}')
        button.place(x=WIDTH//2.5, y=HEIGHT//3 + i*45)
        current_buttons.append(button)
        
def main_menu():
    clear_screen() 
    for i, text in enumerate(buttons):
        if text == "Выход":
            button = ttk.Button(text=f'{i+1}) {text}', command=exit_game)
        elif text == "Настройки":
            button = ttk.Button(text=f'{i+1}) {text}', command=settings)
        elif text == "Начать игру":
            button = ttk.Button(text=f'{i+1}) {text}', command=start_game)
            
        button.place(x=WIDTH//2.5, y=HEIGHT//3 + i*45)
        current_buttons.append(button)
        
def start_game():
    global game, food, score, snake
    if game_over:
        reset_game()
    move_snake()
    if check_wall_collision() or check_self_collision():
        end_game()
        return
    clear_screen()
    canvas.delete("all")
    draw_food()
    draw_snake()
    update_title()
    root.after(DELAY, start_game)
def exit_game():
    root.destroy()
draw_food()
draw_snake()
root.after(DELAY, start_game)
main_menu()    
root.mainloop() 
#1)Исправить баг с сохранением движения после смерти.
#2)Исправить баг с невозможность старта игры после двух смертей. 
