import pygame
from fighter import Fighter

if __name__ == '__main__':

    pygame.init()

    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Fighting')

    FPS = 60
    clock = pygame.time.Clock()


    def draw_bg():
        fon = pygame.image.load('data/img.png')
        fon = pygame.transform.scale(fon, (1000, 600))
        screen.blit(fon, (0, 0))


    fighter_1 = Fighter(200, 420, 1, 'data/idle.png')
    fighter_2 = Fighter(700, 420, 2, 'data/idle.png')

    def healthbar(pos_x, pos_y, health):
        healthbar_rect = pygame.Rect((pos_x, pos_y, 400 * (health / 100), 30))
        health_rect = pygame.Rect((pos_x, pos_y, 400, 30))
        pygame.draw.rect(screen, (255, 0, 0), health_rect)
        pygame.draw.rect(screen, (255, 255, 0), healthbar_rect)


    running = True
    while running:

        clock.tick(FPS)

        draw_bg()
        healthbar(30, 20, fighter_2.health)
        healthbar(570, 20, fighter_1.health)

        fighter_1.move(screen, fighter_2)
        fighter_2.move(screen, fighter_1)

        fighter_1.animation(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()