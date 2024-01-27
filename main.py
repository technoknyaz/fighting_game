import pygame
from fighter import Fighter

if __name__ == '__main__':

    pygame.init()

    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Fighting')

    fon = pygame.image.load('data/bg.jpg').convert_alpha()
    fon = pygame.transform.scale(fon, (1000, 600))
    screen.blit(fon, (0, 0))

    fighter_1 = Fighter(200, 420)
    fighter_2 = Fighter(700, 420)


    running = True
    while running:

        fighter_1.draw(screen)
        fighter_2.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()