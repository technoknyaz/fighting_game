import pygame

class Button:
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = pygame.image.load(hover_image_path)
        self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_hover = False

    def draw(self, surface):
        current_image = self.hover_image if self.is_hover else self.image
        surface.blit(current_image, self.rect.topleft)


        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def check_hover(self, pos_mouse):
        self.is_hover = self.rect.collidepoint(pos_mouse)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hover:
            pass




