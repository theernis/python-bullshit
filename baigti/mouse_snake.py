from pynput.mouse import Button, Controller
import time
import random
mouse = Controller()
snake_block = 1
snake_speed = 15
dis_width = int(float(input("width:"))/snake_block)*snake_block
dis_height = int(float(input("height:"))/snake_block)*snake_block
def gameLoop():
    foodx = random.randint(0, dis_width)
    foody = random.randint(0, dis_height)
    x1_change = 0
    y1_change = 0
    game_close = 0
    speed = int(input("speed: "))
    print("speed: "+str(speed))
    while game_close == 0:
        x1 = mouse.position[0]
        y1 = mouse.position[1]
        if x1 == foodx and y1 == foody:
            foodx = random.randint(0, dis_width)
            foody = random.randint(0, dis_height)
            speed += random.randint(1, 10)
            print("speed: "+str(speed))
        if foodx < x1:
            x1_change = -snake_block
        if foodx > x1:
            x1_change = snake_block
        if foody < y1:
            y1_change = -snake_block
        if foody > y1:
            y1_change = snake_block
        if foodx == x1:
            x1_change = 0
        if foody == y1:
            y1_change = 0
        mouse.move(x1_change, y1_change)
        time.sleep(1/(snake_speed*speed))
gameLoop()
