import pygame

import settings
from Button import Button
from CalculatorLogic import CalculatorLogic
from EventHandler import EventHandler
from GridLayout import GridLayout
from TextField import TextField


def build_layout() -> GridLayout:
    layout = GridLayout(
        settings.WIDTH,
        settings.HEIGHT,
        settings.ROWS,
        settings.COLUMNS,
    )

    layout.add_component(
        TextField(
            text="0",
            background_color=(41, 40, 40),
            text_color=settings.TEXT_COLOR_PRIMARY,
        ),
        0,
        1,
        0,
        4,
    )
    y = 1

    layout.add_component(
        Button(text="C", background_color=settings.BTN_COLOR_SECONDARY),
        y,
        y + 1,
        0,
        1,
    )
    layout.add_component(
        Button(text="+/-", background_color=settings.BTN_COLOR_SECONDARY),
        y,
        y + 1,
        1,
        2,
    )
    layout.add_component(
        Button(text="%", background_color=settings.BTN_COLOR_SECONDARY),
        y,
        y + 1,
        2,
        3,
    )
    layout.add_component(
        Button(text="/", background_color=settings.BTN_COLOR_SPECIAL),
        y,
        y + 1,
        3,
        4,
    )
    y += 1

    layout.add_component(
        Button(text="7", background_color=settings.BTN_COLOR_PRIMARY),
        y,
        y + 1,
        0,
        1,
    )
    layout.add_component(
        Button(text="8", background_color=settings.BTN_COLOR_PRIMARY),
        y,
        y + 1,
        1,
        2,
    )
    layout.add_component(
        Button(text="9", background_color=settings.BTN_COLOR_PRIMARY),
        y,
        y + 1,
        2,
        3,
    )
    layout.add_component(
        Button(text="*", background_color=settings.BTN_COLOR_SPECIAL),
        y,
        y + 1,
        3,
        4,
    )
    y += 1

    layout.add_component(
        Button(text="4", background_color=settings.BTN_COLOR_PRIMARY),
        y,
        y + 1,
        0,
        1,
    )
    layout.add_component(
        Button(text="5", background_color=settings.BTN_COLOR_PRIMARY),
        y,
        y + 1,
        1,
        2,
    )
    layout.add_component(
        Button(text="6", background_color=settings.BTN_COLOR_PRIMARY),
        y,
        y + 1,
        2,
        3,
    )
    layout.add_component(
        Button(text="-", background_color=settings.BTN_COLOR_SPECIAL),
        y,
        y + 1,
        3,
        4,
    )
    y += 1

    layout.add_component(
        Button(text="1", background_color=settings.BTN_COLOR_PRIMARY),
        y,
        y + 1,
        0,
        1,
    )
    layout.add_component(
        Button(text="2", background_color=settings.BTN_COLOR_PRIMARY),
        y,
        y + 1,
        1,
        2,
    )
    layout.add_component(
        Button(text="3", background_color=settings.BTN_COLOR_PRIMARY),
        y,
        y + 1,
        2,
        3,
    )
    layout.add_component(
        Button(text="+", background_color=settings.BTN_COLOR_SPECIAL),
        y,
        y + 1,
        3,
        4,
    )
    y += 1
    layout.add_component(
        Button(text="0", background_color=settings.BTN_COLOR_PRIMARY),
        y,
        y + 1,
        0,
        2,
    )
    layout.add_component(
        Button(text=".", background_color=settings.BTN_COLOR_PRIMARY),
        y,
        y + 1,
        2,
        3,
    )
    layout.add_component(
        Button(text="=", background_color=settings.BTN_COLOR_SPECIAL),
        y,
        y + 1,
        3,
        4,
    )

    # Collision Tests
    # layout.addComponent(Button(text="+", background_color=settings.BTN_COLOR_SPECIAL), 0,1, 0, 1)
    # layout.addComponent(Button(text="+", background_color=settings.BTN_COLOR_SPECIAL), 3,4, 2, 4)
    # layout.addComponent(Button(text="+", background_color=settings.BTN_COLOR_SPECIAL), 1, 3, 2, 3)
    # layout.addComponent(Button(text="+", background_color=settings.BTN_COLOR_SPECIAL), 1,4, 0, 2)
    return layout


def draw_window(layout: GridLayout):
    layout.draw()
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    layout = build_layout()
    logic = CalculatorLogic(layout)
    event_handler = EventHandler(layout, logic)
    while True:
        # with clock.tick we are locking refresh rate to settings.FPS just to lower cpu usage
        clock.tick(settings.FPS)
        event_handler.check_for_event()
        draw_window(layout)


# Thanks to this Calculator won't run if we are not directly running main.py (python3 main.py)
if __name__ == "__main__":
    main()
