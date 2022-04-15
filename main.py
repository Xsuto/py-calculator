import pygame

import settings
from Button import Button
from CalculatorLogic import CalculatorLogic
from EventHandler import EventHandler
from GridLayout import GridLayout
from TextField import TextField


def build_layout() -> GridLayout:
    layout = GridLayout(settings.WIDTH, settings.HEIGHT, settings.ROWS, settings.COLUMNS)

    layout.addComponent(TextField(text="0", background_color=(41, 40, 40)), 0, 1, 0, 4)
    y = 1

    layout.addComponent(Button(text="C", background_color=settings.BTN_COLOR_SECONDARY), y, y + 1, 0, 1)
    layout.addComponent(Button(text="+/-", background_color=settings.BTN_COLOR_SECONDARY), y, y + 1, 1, 2)
    layout.addComponent(Button(text="%", background_color=settings.BTN_COLOR_SECONDARY), y, y + 1, 2, 3)
    layout.addComponent(Button(text="/", background_color=settings.BTN_COLOR_SPECIAL), y, y + 1, 3, 4)
    y += 1

    layout.addComponent(Button(text="7", background_color=settings.BTN_COLOR_PRIMARY), y, y + 1, 0, 1)
    layout.addComponent(Button(text="8", background_color=settings.BTN_COLOR_PRIMARY), y, y + 1, 1, 2)
    layout.addComponent(Button(text="9", background_color=settings.BTN_COLOR_PRIMARY), y, y + 1, 2, 3)
    layout.addComponent(Button(text="*", background_color=settings.BTN_COLOR_SPECIAL), y, y + 1, 3, 4)
    y += 1

    layout.addComponent(Button(text="4", background_color=settings.BTN_COLOR_PRIMARY), y, y + 1, 0, 1)
    layout.addComponent(Button(text="5", background_color=settings.BTN_COLOR_PRIMARY), y, y + 1, 1, 2)
    layout.addComponent(Button(text="6", background_color=settings.BTN_COLOR_PRIMARY), y, y + 1, 2, 3)
    layout.addComponent(Button(text="-", background_color=settings.BTN_COLOR_SPECIAL), y, y + 1, 3, 4)
    y += 1

    layout.addComponent(Button(text="1", background_color=settings.BTN_COLOR_PRIMARY), y, y + 1, 0, 1)
    layout.addComponent(Button(text="2", background_color=settings.BTN_COLOR_PRIMARY), y, y + 1, 1, 2)
    layout.addComponent(Button(text="3", background_color=settings.BTN_COLOR_PRIMARY), y, y + 1, 2, 3)
    layout.addComponent(Button(text="+", background_color=settings.BTN_COLOR_SPECIAL), y, y + 1, 3, 4)
    y += 1

    layout.addComponent(Button(text="0", background_color=settings.BTN_COLOR_PRIMARY), y, y + 1, 0, 2)
    layout.addComponent(Button(text=".", background_color=settings.BTN_COLOR_PRIMARY), y, y + 1, 2, 3)
    layout.addComponent(Button(text="=", background_color=settings.BTN_COLOR_SPECIAL), y, y + 1, 3, 4)

    return layout


def draw_window(layout: GridLayout):
    layout.draw()
    pygame.display.update()


def main():
    # We are putting bool into list because we want to force python into sharing this variable by reference with
    # EventHandler, so we can stop app from inside this class
    run = [True]
    clock = pygame.time.Clock()
    layout = build_layout()
    logic = CalculatorLogic()
    event_handler = EventHandler(layout, logic, run)
    while run[0]:
        clock.tick(settings.FPS)

        event_handler.check_for_event()
        draw_window(layout)


if __name__ == '__main__':
    main()