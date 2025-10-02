import time
import os
import sys


ESC = "\x1b"
CSI = f"{ESC}["
RESET = f"{CSI}0m"

BLUE = f"{CSI}48:5:12m"
WHITE = f"{CSI}48:5:15m"
BLACK = f"{CSI}48:5:0m"
GRAY = f"{CSI}38;5;8m"
RED = f"{CSI}38;5;9m"
GREEN = f"{CSI}38;5;10m"

# Вариант 9
#Флаг Финляндии
def flag(height=16, width = 32):
    line_flag_h = height//4
    offse_h = height // 2 - line_flag_h//2
    line_flag_w = width//4
    offset_w = width // 2 - line_flag_w//2
    for line in range(height):
        if line < offse_h or line > offse_h+line_flag_h/2:
            print(f"{WHITE}{' '*(offset_w-5)}{BLUE}{' '* line_flag_w}{WHITE}{' '*(offset_w+5)}{RESET}")
        else:
            print(f"{BLUE}{' '* (width)}{RESET}")

#Узор
def pattern(size=2,radius=10):
    for y in range(-radius,radius+1):
        line = ""
        for _ in range(size):
            for x in range(-radius,radius+1):
                if x*x+(y*2)**2<=radius*radius:
                    line += BLACK +  " ";
                else:
                    line += WHITE +  " ";
        line += RESET;
        print(line)

#График
def graph(x_min=-30, x_max=30, y_min=-10, y_max=10):
    for y in range(y_max, y_min-1, -1): 
        line = ""
        for x in range(x_min, x_max+1):
            if abs(y-x/3) < 0.5: 
                line += "*"  
            elif x == 0:  
                line += "│"
            elif y == 0: 
                line += "─"
            else:
                line += " "
        print(line)

# Найти в файле 
# Числа от 5 до 10 и числа от -5 до -10, остальные отбросить

def poisk_number_in_file():
    file = open("sequence.txt")
    n = file.read().split()
    file.close()

    c2 = c1 = t = 0
    for x in n:
        x = float(x)
        if 5 <= x <= 10:
            c1+= 1; t+=1
        elif -10 <= x <= -5: 
            c2+=1; t+=1
    if t:
        max_x = 50
        bar1 = "#" * (c1*max_x//t) + RESET
        bar2 = "#" * (c2*max_x//t) + RESET

        print(f"{bar1} {c1*100//t}% :5-10")
        print(f"{bar2} {c2*100//t}% :(-10)-(-5)")
    else:
        print("Нет чисел")

# Анимация
#чистка экрана
def clear():
    print(CSI + "2J" + CSI + "H", end="")
#отрисовка змейки
def draw(rows, cols, snake):
    clear()
    for y in range(rows):
        line = ""
        for x in range(cols):
            if (y, x) == snake[-1]:
                line += RED + "O" + RESET    
            elif (y, x) in snake:
                line += GREEN + "*" + RESET   
            else:
                line += " "                 
        print(line)
#движение змейки
def snake_game(rows=10, cols=30, snake_len=6, delay=0.2):

    snake = [(0, i) for i in range(snake_len)]
    direction = (0, 1) 
    while True:

            head_y, head_x = snake[-1]
            dy, dx = direction
            new_head = (head_y + dy, head_x + dx)

            if new_head[1] >= cols: 
                direction = (1, 0)   
                new_head = (head_y + 1, head_x)
            elif new_head[0] >= rows:  
                direction = (0, -1)   
                new_head = (head_y, head_x - 1)
            elif new_head[1] < 0:  
                direction = (-1, 0) 
                new_head = (head_y - 1, head_x)
            elif new_head[0] < 0:   
                direction = (0, 1)   
                new_head = (head_y, head_x + 1)


            snake.append(new_head)
            if len(snake) > snake_len:
                snake.pop(0)

            draw(rows, cols, snake)
            time.sleep(delay)

if __name__ == "__main__":
    flag()
    pattern()
    graph()
    poisk_number_in_file()
    time.sleep(5)
    snake_game()