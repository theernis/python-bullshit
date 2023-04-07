import pygame
import perlin

pygame.init()

dis_width = 400
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('noise')
clock = pygame.time.Clock()

def gameLoop():
    game_over = False

    z = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
        dis.fill((0,0,0))
        
        for x in range(dis_width):
            for y in range(dis_height):
                dis.set_at((x, y), perlin.getColor(x/dis_width, y/dis_height, z))

        pygame.display.update()
        clock.tick(60)
        print("new frame")
    pygame.quit()
    quit()
gameLoop()
