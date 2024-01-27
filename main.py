import pygame

if __name__ == '__main__':

    pygame.init()

    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Fighting')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()