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
food = [5, 0, 50, 0]

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg = "black"
)
canvas.pack()

def create_food():
    x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) *CELL_SIZE
    y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) *CELL_SIZE
    canvas.create_rectangle(
        food[0], food[1],
        food[0] + CELL_SIZE,
        food[1] + CELL_SIZE,
        fill="red")

    
def clear_screen():
    for btn in current_buttons:
        btn.destroy()
    current_buttons.clear()

def exit_game():
    root.destroy()

def start_game():
    clear_screen()
    canvas.delete("all")
    create_food()


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
