import pygame

pygame.init()
dis_width = 400
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('NAME')
clock = pygame.time.Clock()

def gameLoop():
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
        dis.fill((0, 0, 0))

        #Your Code

        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()
gameLoop()
