import pygame

class Fighter():
    def __init__(self, x, y):
        self.rectangle = pygame.Rect((x, y, 80, 180))
        self.vy = 0
        self.flag_jump = False

    def move(self):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED
        if key[pygame.K_w] and self.flag_jump == False:
            self.vy = -30
            self.flag_jump = True

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




    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rectangle)