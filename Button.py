import settings
from Component import Component
from setup import WIN, FONT


class Button(Component):
    def __init__(self, start_x: int = 0, start_y: int = 0, text="", width=settings.WIDTH, height=0,
                 text_color=settings.TEXT_COLOR_PRIMARY, background_color=settings.BTN_COLOR_PRIMARY,
                 border_color=settings.BORDER_COLOR_PRIMARY):
        super(Button, self).__init__(start_x, start_y, text, width, height, text_color, background_color, border_color)

    def get_type(self) -> str:
        return "button"

    def render_text(self):
        text = FONT.render(self._text, True, self._text_color, self._current_background_color)
        text_rect = text.get_rect()
        text_rect.centerx = self._x + (self._width // 2)
        text_rect.centery = self._y + (self._height // 2)
        WIN.blit(text, text_rect)

    def draw(self):
        self.render_background()
        self.render_border()
        self.render_text()
