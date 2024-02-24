import pygame
import sqlite3 as sql
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

con = sql.connect('data.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS background(id INTEGER PRIMARY KEY, img BLOB)')

#for i in range(1, 3):
#    with open(f'data/bg_{i}.png', 'rb') as img:
#        cur.execute('INSERT INTO background(img) VALUES(?)', [img.read()])

bg_photo = cur.execute('SELECT img FROM background').fetchall()


con.commit()
cur.close()
con.close()

def draw_bg():
    global fon
    fon_bg = pygame.transform.scale(fon, (1000, 600))
    screen.blit(fon_bg, (0, 0))

def healthbar(pos_x, pos_y, health):
    healthbar_rect = pygame.Rect((pos_x, pos_y, 400 * (health / 100), 30))
    health_rect = pygame.Rect((pos_x, pos_y, 400, 30))
    pygame.draw.rect(screen, (255, 0, 0), health_rect)
    pygame.draw.rect(screen, (255, 255, 0), healthbar_rect)

def main_menu():
    button_start = Button(width / 2 - (270 / 2), 250, 270, 74, "", "data/play01.png", "data/play02.png")
    exit_button = Button(width / 2 - (270 / 2), 350, 270, 74, "", "data/back01.png", "data/back02.png")
    option_button = Button(width / 2 - (270 / 2), 450, 270, 74, "", "data/option01.png", "data/option02.png")

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

            if event.type == pygame.USEREVENT and event.button == option_button:
                option()

            for btn in [button_start, exit_button, option_button]:
                btn.handle_event(event)

        for btn in [button_start, exit_button, option_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x, y))

        pygame.display.update()

def option():
    global fon
    running = True
    main_menu_fon = pygame.image.load("data/main_menu_fon.png")
    main_menu_fon = pygame.transform.scale(main_menu_fon, size)
    exit_button = Button(width / 2 - (270 / 2), 500, 270, 74, "", "data/back01.png", "data/back02.png")
    choose_btn_1 = Button(100, 400, 270, 74, "", "data/yes01.png", "data/yes02.png")
    choose_btn_2 = Button(650, 400, 270, 74, "", "data/yes01.png", "data/yes02.png")

    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_menu_fon, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False

            if event.type == pygame.USEREVENT and event.button == choose_btn_1:
                fon = pygame.image.load('data/bg_1.png')
                running = False

            if event.type == pygame.USEREVENT and event.button == choose_btn_2:
                fon = pygame.image.load('data/bg_2.png')
                running = False

            for btn in [exit_button, choose_btn_1, choose_btn_2]:
                btn.handle_event(event)

        for btn in [exit_button, choose_btn_1, choose_btn_2]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x, y))

        bg_1 = pygame.image.load('data/bg_1.png')
        bg_1 = pygame.transform.scale(bg_1, (350, 250))
        bg_1_rect = bg_1.get_rect(bottomright=(400, 350))
        screen.blit(bg_1, bg_1_rect)

        bg_2 = pygame.image.load('data/bg_2.png')
        bg_2 = pygame.transform.scale(bg_2, (350, 250))
        bg_2_rect = bg_2.get_rect(bottomright=(950, 350))
        screen.blit(bg_2, bg_2_rect)

        pygame.display.update()


def new_game():
    running = True

    fighter_1 = Fighter(200, 200, 1, "data/idle.png", "LEFT")
    fighter_2 = Fighter(600, 200, 2, "data/idle_2_l.png", "RIGHT")

    game_start = False
    round_end = False
    score = [0, 0]
    round_end_time = 0

    font2 = pygame.font.Font(None, 0)
    text2 = font2.render(f'123', True, (0, 0, 0))

    intro_count = 4
    last_update = pygame.time.get_ticks()

    while running:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    fighter_1.attacking = True
                    fighter_1.attack(fighter_2, screen)
                if event.key == pygame.K_DOWN:
                    fighter_2.attacking = True
                    fighter_2.attack(fighter_2, screen)

        if round_end == False:
            if fighter_1.alive == False:
                score[1] += 1
                round_end = True
                round_end_time = pygame.time.get_ticks()
                print(score)
            elif fighter_2.alive == False:
                score[0] += 1
                round_end = True
                round_end_time = pygame.time.get_ticks()
                print(score)
        else:

            if pygame.time.get_ticks() - round_end_time > 3000:
                round_end = False
                new_game()

        if score[0] > 0 or score[1] > 0:
            font = pygame.font.Font(None, 64)
            text1 = font.render(f'VICTORY Player: {score.index(max(score))+1}', True, (150, 0, 0))
        else:
            font = pygame.font.Font(None, 0)
            text1 = font.render("123", True, (255, 0, 0))

        if intro_count <= 0:
            game_start = True
            font = pygame.font.Font(None, 0)
            text2 = font.render(f'{intro_count}', True, (0, 0, 0))
        else:
            if (pygame.time.get_ticks() - last_update) >= 1000:
                intro_count -= 1
                last_update = pygame.time.get_ticks()
                font = pygame.font.Font(None, 64)
                text2 = font.render(f'{intro_count}', True, (0, 0, 0))


        draw_bg()
        if game_start == True:
            fighter_1.move()
            fighter_2.move()
            fighter_1.render(screen)
            fighter_2.render(screen)
            fighter_1.update(fighter_2, screen)
            fighter_2.update(fighter_1, screen)
        healthbar(20, 20, fighter_1.health)
        healthbar(580, 20, fighter_2.health)
        screen.blit(text1, (300, 200))
        screen.blit(text2, (480, 100))
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main_menu()