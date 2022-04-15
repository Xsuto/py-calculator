import pygame

import settings
from setup import WIN


class Component:
    # Python convention for public, protected, private
    # name <- public
    # _name <- protected
    # __name <- private
    def __init__(self, start_x: int = 0, start_y: int = 0, text="", width=settings.WIDTH, height=0,
                 text_color=settings.TEXT_COLOR_PRIMARY,
                 background_color=settings.BLACK, border_color=settings.BLACK):
        self._x = start_x
        self._y = start_y
        self._text = text
        self._width = width
        self._height = height
        self._text_color = text_color
        self._background_color = background_color
        self._activated_background_color = (
            background_color[0] * 0.7, background_color[1] * 0.7, background_color[2] * 0.7)
        self._current_background_color = background_color
        self._border_color = border_color
        self._is_activated = False
        self._rect = pygame.Rect(start_x, start_y, width, height)

    # It isn't necessary to update_rect in every set_foo call, but it is better to be safe than sorry
    def set_x(self, x: int):
        self._x = x
        self.update_rect()

    def set_y(self, y: int):
        self._y = y
        self.update_rect()

    def set_width(self, width: int):
        self._width = width
        self.update_rect()

    def set_height(self, height: int):
        self._height = height
        self.update_rect()

    def get_type(self) -> str:
        return ""

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def update_rect(self):
        self._rect = pygame.Rect(self._x, self._y, self._width, self._height)
        if settings.DEBUG:
            print("Rect: ", self._rect)

    def is_clicked(self, x: int, y: int):
        if self._x + settings.HITBOX_MARGIN <= x <= self._width + self._x - settings.HITBOX_MARGIN:
            if self._y + self._height - settings.HITBOX_MARGIN >= y >= self._y + settings.HITBOX_MARGIN:
                if settings.DEBUG:
                    print("From is_clicked\nGot x: ", x, "\nMy x: ", self._x, "\nMy absolute width:",
                          self._width + self._x)
                return True
        return False

    def flip_is_activated(self):
        self._is_activated = not self._is_activated
        if self._is_activated:
            self._current_background_color = self._activated_background_color
        else:
            self._current_background_color = self._background_color

    def is_activated(self):
        return self._is_activated

    # Virtual function that needs to be overwritten
    def on_click(self):
        pass

    # Virtual function that needs to be overwritten
    def draw(self):
        pass

    def render_border(self):
        pygame.draw.rect(WIN, self._border_color, self._rect, 1)

    def render_background(self):
        pygame.draw.rect(WIN, self._current_background_color, self._rect)
