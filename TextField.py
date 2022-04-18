import pygame.font

import settings
from Component import Component
from setup import WIN


class TextField(Component):
    def __init__(self, start_x: int = 0, start_y: int = 0, text="", width=settings.WIDTH, height=0,
                 text_color=settings.WHITE, background_color=settings.BLACK,
                 border_color=settings.BORDER_COLOR_PRIMARY):
        super(TextField, self).__init__(start_x, start_y, text, width, height, text_color, background_color,
                                        border_color)

    def set_text(self, text):
        self._text = str(text)

    def get_type(self) -> str:
        return "textfield"

    def set_is_activated(self, is_activated: bool):
        pass

    def render_text(self):
        # We are creating custom font because self._text might be long and text might overflow self._rect,
        # so in that case we just decrease font_size
        font_size = settings.FONT_SIZE
        custom_font = pygame.font.Font(pygame.font.get_default_font(), settings.FONT_SIZE)
        text = custom_font.render(self._text, True, self._text_color, self._background_color)
        text_rect = text.get_rect()
        while text_rect.width > self._width - settings.MARGIN:
            font_size -= 2
            if font_size == 0:
                print("Panic font_size == 0 this shouldn't happened")
                exit(1)
            custom_font = pygame.font.Font(pygame.font.get_default_font(), font_size)
            text = custom_font.render(self._text, True, self._text_color, self._background_color)
            text_rect = text.get_rect()
        text_rect.left = self._x + self._width - text_rect.right - settings.MARGIN
        text_rect.centery = self._height / 2 + self._y
        WIN.blit(text, text_rect)

    def draw(self):
        self.render_background()
        self.render_border()
        self.render_text()
