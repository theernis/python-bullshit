import pygame
import time
import random
pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
snake_block = 10
snake_speed = int(input("snake speed:"))
dis_width = int(float(input("width:"))/snake_block)*snake_block
dis_height = int(float(input("height:"))/snake_block)*snake_block
sleeptime = float(input("sleeptime:"))
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('#python')
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
def Your_score(score):
    value = score_font.render("Snake Score: " + str(score), True, blue)
    dis.blit(value, [0, 0])
def Your_highscore(score):
    value = score_font.render("Highscore: " + str(score), True, blue)
    dis.blit(value, [0, 30])
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
        if x == snake_list[len(snake_list)-1]:
            pygame.draw.rect(dis, blue, [x[0]+1, x[1]+1, snake_block-2, snake_block-2])
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
def distance(a, b):
    if a > b:
        return (a-b)
    else:
        return (b-a)
def gameLoop(high):
    x1_change = 0
    y1_change = 0
    game_over = False
    game_close = False
    x1 = int((dis_width / 2) / snake_block) * snake_block
    y1 = int((dis_height / 2) / snake_block) * snake_block
    highscore = high
    snake_List = []
    Length_of_snake = 1
    score = 0
    foodx = int(random.randint(0, dis_width - snake_block) / snake_block) * snake_block
    foody = int(random.randint(0, dis_height - snake_block) / snake_block) * snake_block
    while not game_over:
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        score = Length_of_snake - 1
        xdistance = distance(foodx, snake_Head[0])
        ydistance = distance(foody, snake_Head[1])
        if x1 >= dis_width+snake_block or x1 < 0 or y1 >= dis_height+snake_block or y1 < 0:
            game_close = True
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        while game_close == True:
            message("Snake died!", white)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            time.sleep(sleeptime)
            dis.fill(black)
            gameLoop(highscore)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx+1, foody+1, snake_block-2, snake_block-2])
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        draw_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        if highscore < Length_of_snake - 1:
            highscore = Length_of_snake - 1
        Your_highscore(highscore)
        if x1 == foodx and y1 == foody:
            foodx = int(random.randint(0, dis_width - snake_block) / snake_block) * snake_block
            foody = int(random.randint(0, dis_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1
        for x in snake_List[:-1]:
            if x == [foodx, foody]:
                foodx = int(random.randint(0, dis_width - snake_block) / snake_block) * snake_block
                foody = int(random.randint(0, dis_height - snake_block) / snake_block) * snake_block
        if xdistance <= ydistance:
            if foodx < x1 and x1_change >= 0:
                x1_change = -snake_block
                y1_change = 0
            if foodx > x1 and x1_change <= 0:
                x1_change = snake_block
                y1_change = 0
            if foody < y1 and y1_change >= 0:
                y1_change = -snake_block
                x1_change = 0
            if foody > y1 and y1_change <= 0:
                y1_change = snake_block
                x1_change = 0
        else:
            if foody < y1 and y1_change >= 0:
                y1_change = -snake_block
                x1_change = 0
            if foody > y1 and y1_change <= 0:
                y1_change = snake_block
                x1_change = 0
            if foodx < x1 and x1_change >= 0:
                x1_change = -snake_block
                y1_change = 0
            if foodx > x1 and x1_change <= 0:
                x1_change = snake_block
                y1_change = 0
        x1 += x1_change
        y1 += y1_change
        pygame.display.update()
        clock.tick(snake_speed*5*Length_of_snake)
    pygame.quit()
    quit()
gameLoop(0)
