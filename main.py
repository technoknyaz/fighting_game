import pygame
from fighter import Fighter
import sys
from tools import Button

pygame.init()

size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Fighting')

FPS = 20
clock = pygame.time.Clock()
main_menu_fon = pygame.image.load("data/main_menu_fon.png")
main_menu_fon = pygame.transform.scale(main_menu_fon, size)
cursor = pygame.image.load("data/cursor.png")
cursor = pygame.transform.scale(cursor, (32, 32))
pygame.mouse.set_visible(False)

def draw_bg():
    fon = pygame.image.load('data/img.png')
    fon = pygame.transform.scale(fon, (1000, 600))
    screen.blit(fon, (0, 0))

# def healthbar(pos_x, pos_y, health):
#     healthbar_rect = pygame.Rect((pos_x, pos_y, 400 * (health / 100), 30))
#     health_rect = pygame.Rect((pos_x, pos_y, 400, 30))
#     pygame.draw.rect(screen, (255, 0, 0), health_rect)
#     pygame.draw.rect(screen, (255, 255, 0), healthbar_rect)

def main_menu():
    button_start = Button(width / 2 - (270 / 2), 250, 270, 74, "", "data/play01.png", "data/play02.png")
    exit_button = Button(width / 2 - (270 / 2), 350, 270, 74, "", "data/back01.png", "data/back02.png")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_menu_fon, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == button_start:
                new_game()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False

            for btn in [button_start, exit_button]:
                btn.handle_event(event)

        for btn in [button_start, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x, y))

        pygame.display.update()
def new_game():
    running = True
    fighter_1 = Fighter(200, 200, 1, "data/idle.png")
    fighter_2 = Fighter(200, 200, 2, "data/idle.png")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    fighter_1.attacking = True
                    fighter_1.attack(fighter_2, screen)


        fighter_1.move()
        fighter_2.move()
        draw_bg()
        fighter_1.render(screen)
        fighter_2.render(screen)
        fighter_1.update(fighter_2, screen)
        fighter_2.update(fighter_1, screen)


        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main_menu()

