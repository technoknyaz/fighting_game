import pygame

class Fighter():
    def __init__(self, x, y, player):
        self.rectangle = pygame.Rect((x, y, 80, 180))
        self.vy = 0
        self.flag_jump = False
        self.attack_flag = False
        self.attack_type = 0
        self.health = 100
        self.player = player


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
                if key[pygame.K_d]:
                    dx = SPEED
                if key[pygame.K_w] and self.flag_jump == False:
                    self.vy = -30
                    self.flag_jump = True
                if key[pygame.K_e] or key[pygame.K_q]:
                    if key[pygame.K_e]:
                        self.attack_type = 1
                    if key[pygame.K_q]:
                        self.attack_type = 2
                    self.attacking(surface, target)
                    self.attack_flag = False

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

    def attacking(self, surface, target):
        self.attack_flag = True
        if self.attack_type == 1:
            rectangle_attacking = pygame.Rect((self.rectangle.x, self.rectangle.y, 2 * self.rectangle.width, self.rectangle.height))
        elif self.attack_type == 2:
            rectangle_attacking = pygame.Rect((self.rectangle.x - (self.rectangle.width), self.rectangle.y, 2 * self.rectangle.width, self.rectangle.height))

        if rectangle_attacking.colliderect(target.rectangle):
            self.health -= 1



        pygame.draw.rect(surface, (255, 255, 0), rectangle_attacking)


    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rectangle)