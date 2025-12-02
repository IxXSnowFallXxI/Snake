import tkinter as tk
from tkinter import ttk
import random 
WIDTH = 500
HEIGHT = 500
CELL_SIZE = 10
DELAY = 100
root = tk.Tk()
root.title("Змейка 3000")
label = tk.Label(text="Главное Меню")
label.pack()
current_buttons = []
buttons = ["Начать игру", "Настройки", "Выход"]

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
        
def clear_screen():
    for btn in current_buttons:
        btn.destroy()
    current_buttons.clear()

def exit_game():
    root.destroy()

def start_game():
    global game, food, score
    clear_screen()
    canvas.delete("all")
    draw_food()
    draw_snake()
    root.after(DELAY, start_game)


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

main_menu()    
root.mainloop() 
