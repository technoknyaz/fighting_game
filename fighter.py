import pygame

class Fighter():
    def __init__(self, x, y, player, player_image):
        self.image = pygame.transform.scale(pygame.image.load(player_image), (100,300))
        self.rectangle = pygame.Rect((x, y, 100, 300))
        self.vy = 0
        self.flag_jump = False
        self.attack_flag = False
        self.attack_type = 0
        self.health = 100
        self.player = player
        self.left = False
        self.right = False
        self.count = 0
        self.attack_anim_flag = False

        self.run_right = [
            pygame.transform.scale(pygame.image.load('data/run_1.png'), (100,300)),
            pygame.transform.scale(pygame.image.load('data/run_2.png'), (100,300)),
            pygame.transform.scale(pygame.image.load('data/run_3.png'), (100,300)),
            pygame.transform.scale(pygame.image.load('data/run_4.png'), (100,300)),
            pygame.transform.scale(pygame.image.load('data/run_5.png'), (100,300)),
            pygame.transform.scale(pygame.image.load('data/run_6.png'), (100,300)),
            pygame.transform.scale(pygame.image.load('data/run_7.png'), (100,300)),
            pygame.transform.scale(pygame.image.load('data/run_8.png'), (100,300))
        ]
        self.run_left = [
            pygame.transform.scale(pygame.image.load('data/run_left_1.png'), (100,300)),
            pygame.transform.scale(pygame.image.load('data/run_left_2.png'), (100,300)),
            pygame.transform.scale(pygame.image.load('data/run_left_3.png'), (100,300)),
            pygame.transform.scale(pygame.image.load('data/run_left_4.png'), (100,300)),
            pygame.transform.scale(pygame.image.load('data/run_left_5.png'), (100,300)),
            pygame.transform.scale(pygame.image.load('data/run_left_6.png'), (100,300)),
            pygame.transform.scale(pygame.image.load('data/run_left_7.png'), (100,300)),
            pygame.transform.scale(pygame.image.load('data/run_left_8.png'), (100,300))

        ]
        self.attack = [
            pygame.transform.scale(pygame.image.load('data/Attack_1.png'), (100, 300)),
            pygame.transform.scale(pygame.image.load('data/Attack_2.png'), (100, 300)),
            pygame.transform.scale(pygame.image.load('data/Attack_3.png'), (100, 300)),
            pygame.transform.scale(pygame.image.load('data/Attack_4.png'), (100, 300))
        ]

    def move(self, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        if self.player == 1:
            if self.attack_flag == False:
                if key[pygame.K_a]:
                    dx = -SPEED
                    self.left = True
                    self.right = False
                elif key[pygame.K_d]:
                    self.left = False
                    self.right = True
                    dx = SPEED
                else:
                    self.left = False
                    self.right = False
                    self.count = 0
                if key[pygame.K_w] and self.flag_jump == False:
                    self.vy = -30
                    self.flag_jump = True
                if key[pygame.K_e] or key[pygame.K_q]:
                    self.attack_anim_flag = True
                    if key[pygame.K_e]:
                        self.attack_type = 1
                    if key[pygame.K_q]:
                        self.attack_type = 2
                    self.attacking(surface, target)
                    self.attack_flag = False
                else:
                    self.attack_anim_flag = False


        if self.player == 2:
            if self.attack_flag == False:
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                if key[pygame.K_UP] and self.flag_jump == False:
                    self.vy = -30
                    self.flag_jump = True
                if key[pygame.K_n] or key[pygame.K_m]:
                    if key[pygame.K_m]:
                        self.attack_type = 1
                    if key[pygame.K_n]:
                        self.attack_type = 2
                    self.attacking(surface, target)
                    self.attack_flag = False


        self.vy += GRAVITY
        dy += self.vy

        if self.rectangle.left + dx < 0:
            dx = -self.rectangle.left
        if self.rectangle.right + dx > 1000:
            dx = 1000 - self.rectangle.right
        if self.rectangle.bottom + dy > 600:
            self.vy = 0
            self.flag_jump = False
            dy = 600 - self.rectangle.bottom

        self.rectangle.x += dx
        self.rectangle.y += dy

    def animation(self, surface):
        if self.count + 1 >= 60:
            self.count = 0
        if self.right == True and self.left == False:
            surface.blit(self.run_right[self.count // 8], (self.rectangle.x, self.rectangle.y))
            self.count += 1
        elif self.right == False and self.left == True:
            surface.blit(self.run_left[self.count // 8], (self.rectangle.x, self.rectangle.y))
            self.count += 1
        elif self.attack_anim_flag == True:
            surface.blit(self.attack[self.count // 4], (self.rectangle.x, self.rectangle.y))
            self.count += 1
        else:
            surface.blit(self.image, (self.rectangle.x, self.rectangle.y))


    def attacking(self, surface, target):
        self.attack_flag = True
        self.attack_anim_flag = True
        if self.attack_type == 1:
            rectangle_attacking = pygame.Rect((self.rectangle.x, self.rectangle.y, 2 * self.rectangle.width, self.rectangle.height))
        elif self.attack_type == 2:
            rectangle_attacking = pygame.Rect((self.rectangle.x - (self.rectangle.width), self.rectangle.y, 2 * self.rectangle.width, self.rectangle.height))

        if rectangle_attacking.colliderect(target.rectangle):
            self.health -= 1
