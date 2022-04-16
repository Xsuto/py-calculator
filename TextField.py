import settings
from Component import Component
from setup import WIN, FONT


class TextField(Component):
    def __init__(self, start_x: int = 0, start_y: int = 0, text="", width=settings.WIDTH, height=0,
                 text_color=settings.WHITE, background_color=settings.BLACK):
        super(TextField, self).__init__(start_x, start_y, text, width, height, text_color, background_color)

    def get_type(self) -> str:
        return "textfield"

    def render_text(self):
        text = FONT.render(self._text, True, self._text_color, self._background_color)
        text_rect = text.get_rect()
        text_rect.left = self._x + self._width - text_rect.right - settings.MARGIN
        text_rect.centery = self._height / 2 + self._y
        WIN.blit(text, text_rect)

    def draw(self):
        self.render_background()
        self.render_border()
        self.render_text()
