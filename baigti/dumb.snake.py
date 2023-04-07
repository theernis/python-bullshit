import pygame
import time
import random

pygame.init()
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
snake_block = 10
snake_speed = int(input("snake speed:"))
display_width = int(float(input("width:")) / snake_block) * snake_block
display_height = int(float(input("height:")) / snake_block) * snake_block
sleep_time = float(input("sleep time:"))
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('#python')
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    value = score_font.render("Snake Score: " + str(score), True, blue)
    display.blit(value, [0, 0])


def your_high_score(score):
    value = score_font.render("Highscore: " + str(score), True, blue)
    display.blit(value, [0, 30])


def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])
        if x == snake_list[len(snake_list) - 1]:
            pygame.draw.rect(display, blue, [x[0] + 1, x[1] + 1, snake_block - 2, snake_block - 2])


def message(msg, color):
    text = font_style.render(msg, True, color)
    display.blit(text, [display_width / 3, display_height / 3])


def test_up(snake_head, snake_list):
    return is_dead([snake_head[0], snake_head[1] + snake_block], snake_list) * 1


def test_right(snake_head, snake_list):
    return is_dead([snake_head[0] + snake_block, snake_head[1]], snake_list) * 1


def test_down(snake_head, snake_list):
    return is_dead([snake_head[0], snake_head[1] - snake_block], snake_list) * 1


def test_left(snake_head, snake_list):
    return is_dead([snake_head[0] - snake_block, snake_head[1]], snake_list) * 1


def is_dead(snake_head, snake_list):
    if snake_head[0] >= display_width or snake_head[0] < 0 or snake_head[1] >= display_height or snake_head[1] < 0:
        return True
    for x in snake_list[:-1]:
        if x == snake_head:
            return True
    return False


def invert(x):
    x = 1 if x == 0 else 0
    return x


def vector2(up, right, down, left):
    x = random.randint(-left, right) * snake_block
    y = random.randint(-down, up) * snake_block
    if x != 0 and y == 0 or x == 0 and y != 0:
        return [x, y]
    else:
        return vector2(up, right, down, left)


def game_loop(high):
    x1_change = 0
    y1_change = 0
    game_over = False
    game_close = False
    x1 = int((display_width / 2) / snake_block) * snake_block
    y1 = int((display_height / 2) / snake_block) * snake_block
    highs_core = high
    snake_list = []
    length_of_snake = 1
    food_x = int(random.randint(0, display_width - snake_block) / snake_block) * snake_block
    food_y = int(random.randint(0, display_height - snake_block) / snake_block) * snake_block
    while not game_over:
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        game_close = is_dead(snake_head, snake_list)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        while game_close:
            message("Snake died!", red)
            your_score(length_of_snake - 1)
            pygame.display.update()
            time.sleep(sleep_time)
            display.fill(black)
            game_loop(highs_core)
        display.fill(black)
        pygame.draw.rect(display, red, [food_x + 1, food_y + 1, snake_block - 2, snake_block - 2])
        draw_snake(snake_list)
        your_score(length_of_snake - 1)
        if highs_core < length_of_snake - 1:
            highs_core = length_of_snake - 1
        your_high_score(highs_core)
        if x1 == food_x and y1 == food_y:
            food_x = int(random.randint(0, display_width - snake_block) / snake_block) * snake_block
            food_y = int(random.randint(0, display_height - snake_block) / snake_block) * snake_block
            length_of_snake += 1
        for x in snake_list[:-1]:
            if x == [food_x, food_y]:
                food_x = int(random.randint(0, display_width - snake_block) / snake_block) * snake_block
                food_y = int(random.randint(0, display_height - snake_block) / snake_block) * snake_block
        up = test_up(snake_head, snake_list)
        right = test_right(snake_head, snake_list)
        down = test_down(snake_head, snake_list)
        left = test_left(snake_head, snake_list)
        if down == 0 or up == 0 or left == 0 or right == 0:
            rotation = vector2(invert(up), invert(right), invert(down), invert(left))
            x1_change = rotation[0]
            y1_change = rotation[1]
        x1 += x1_change
        y1 += y1_change
        pygame.display.update()
        clock.tick(snake_speed * length_of_snake)


game_loop(0)
