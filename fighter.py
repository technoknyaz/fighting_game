import pygame

vec = pygame.math.Vector2

walk_anim_right = [
    pygame.transform.scale(pygame.image.load("data/walk_right (1).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/walk_right (2).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/walk_right (3).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/walk_right (4).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/walk_right (5).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/walk_right (6).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/walk_right (7).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/walk_right (8).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/walk_right (1).png"), (200, 310)),
]
walk_anim_left = [
    pygame.transform.scale(pygame.image.load("data/walk_left (1).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/walk_left (2).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/walk_left (3).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/walk_left (4).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/walk_left (5).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/walk_left (6).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/walk_left (7).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/walk_left (8).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/walk_left (1).png"), (200, 310)),
]
attack_anim_right = [
    pygame.transform.scale(pygame.image.load("data/attack_right (2).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/attack_right (3).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/attack_right (4).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/attack_right (5).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/attack_right (1).png"), (200, 310)),
]
attack_anim_left = [
    pygame.transform.scale(pygame.image.load("data/attack_left (4).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/attack_left (5).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/attack_left (1).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/attack_left (2).png"), (200, 310)),
    pygame.transform.scale(pygame.image.load("data/attack_left (3).png"), (200, 310))
]
class Fighter():
    def __init__(self, x, y, player, image, direction):
        self.pos = vec(x, y)
        self.jump = False
        self.vel_y = 0
        self.direction = direction
        self.move_frame = 0
        self.attack_frame = 0
        self.attacking = False
        self.health = 100
        self.player = player
        self.alive = True

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (200, 310))


        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def move(self):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if self.alive == True:
            if self.player == 1:
                if key[pygame.K_a]:
                    dx = -SPEED
                if key[pygame.K_d]:
                    dx = SPEED
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True

                self.vel_y += GRAVITY
                dy += self.vel_y

                if self.pos.x + dx < 0:
                    dx = -self.pos.x
                if self.pos.x + dx > 800:
                    dx = 800 - self.pos.x
                if self.pos.y + dy > 600 - 310:
                    self.vel_y = 0
                    self.jump = False
                    dy = 600 - 310 - self.pos.y

                self.dx = dx
                self.rect.x += dx
                self.rect.y += dy
                self.pos.x += dx
                self.pos.y += dy

            if self.player == 2:
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True

                self.vel_y += GRAVITY
                dy += self.vel_y

                if self.pos.x + dx < 0:
                    dx = -self.pos.x
                if self.pos.x + dx > 800:
                    dx = 800 - self.pos.x
                if self.pos.y + dy > 600 - 310:
                    self.vel_y = 0
                    self.jump = False
                    dy = 600 - 310 - self.pos.y

                self.dx = dx
                self.pos.x += dx
                self.pos.y += dy
                self.rect.x += dx
                self.rect.y += dy


    def walk_anim(self):
        if self.move_frame > 8:
            self.move_frame = 0


        if self.jump == False:
            if self.dx > 0:
                self.image = walk_anim_right[self.move_frame]
                self.direction = "LEFT"
            elif self.dx < 0:
                self.image = walk_anim_left[self.move_frame]
                self.direction = "RIGHT"
            self.move_frame += 1

    def attack(self, target, surface):
        if self.attacking == True:
            if self.attack_frame > 4:
                self.attack_frame = 0
                self.attacking = False

            if self.direction == "LEFT":
                self.image = attack_anim_right[self.attack_frame]
            elif self.direction == 'RIGHT':
                self.image = attack_anim_left[self.attack_frame]
            self.attack_frame += 1
            if self.direction == 'RIGHT':
                attacking_rect = pygame.Rect(self.pos.x - 100, self.pos.y, 100, 310)
            elif self.direction == 'LEFT':
                attacking_rect = pygame.Rect(self.pos.x + 200, self.pos.y, 100, 310)
            # pygame.draw.rect(surface, (255, 255, 0), attacking_rect)
            if attacking_rect.colliderect(target.rect):
                target.health -= 1
                if target.health < 0:
                    target.alive = False
                    image = pygame.image.load("data/Dead-ezgif.com-crop.png")
                    target.image = pygame.transform.scale(image, (200, 310))
        else:
            pass

    def update(self, target, surface):
        self.attack(target, surface)
        self.walk_anim()
        self.move()

    def render(self, surface):
        # pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(self.image, self.pos)




