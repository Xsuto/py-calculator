from typing import Tuple

import pygame

import settings
from setup import WIN


class Component:
    # Python convention for public, protected, private
    # name <- public
    # _name <- protected
    # __name <- private
    def __init__(
        self,
        start_x: int,
        start_y: int,
        text: str,
        width: int,
        height: int,
        text_color: Tuple[int, int, int],
        background_color: Tuple[int, int, int],
        border_color: Tuple[int, int, int],
    ):
        self._x = start_x
        self._y = start_y
        self._text = text
        self._width = width
        self._height = height
        self._text_color = text_color
        self._background_color = background_color
        self._activated_background_color = (
            int(background_color[0] * 0.7),
            int(background_color[1] * 0.7),
            int(background_color[2] * 0.7),
        )
        self._current_background_color = background_color
        self._border_color = border_color
        self._is_activated = False
        self._rect = pygame.Rect(start_x, start_y, width, height)

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

    def set_text(self, text):
        self._text = str(text)

    # Virtual method that needs to be overwritten
    def get_type(self) -> str:
        raise NotImplementedError()

    def get_text(self) -> str:
        return self._text

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
        if settings.DEBUG_POSITION:
            print("Rect: ", self._rect)

    def is_clicked(self, x: int, y: int):
        if (
            self._x + settings.HITBOX_MARGIN
            <= x
            <= self._width + self._x - settings.HITBOX_MARGIN
        ):
            if (
                self._y + self._height - settings.HITBOX_MARGIN
                >= y
                >= self._y + settings.HITBOX_MARGIN
            ):
                if settings.DEBUG_POSITION:
                    print(
                        f"From is_clicked\nGot x: {x}"
                        f"\nMy x: {self._x - settings.HITBOX_MARGIN}"
                        f"\nMy absolute width:{self._width + self._x - settings.HITBOX_MARGIN}",
                    )
                return True
        return False

    def set_is_activated(self, is_activated: bool):
        self._is_activated = is_activated
        if self._is_activated:
            self._current_background_color = self._activated_background_color
        else:
            self._current_background_color = self._background_color

    # If variable is a bool we call getter for this variable is_foo
    def is_activated(self):
        return self._is_activated

    def render_border(self):
        pygame.draw.rect(WIN, self._border_color, self._rect, settings.BORDER_SIZE)

    def render_background(self):
        pygame.draw.rect(WIN, self._current_background_color, self._rect)

    # Virtual method that needs to be overwritten
    def render_text(self):
        raise NotImplementedError()

    def draw(self):
        self.render_background()
        self.render_border()
        self.render_text()
