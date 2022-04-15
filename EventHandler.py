import pygame

from CalculatorLogic import CalculatorLogic
from GridLayout import GridLayout


class EventHandler():
    def __init__(self, layout: GridLayout, calculator_logic: CalculatorLogic, running: [bool]):
        self.__layout = layout
        self.__calculator_logic = calculator_logic
        self.__is_app_running = running

    def mouse_down_event(self):
        x, y = pygame.mouse.get_pos()
        for component in self.__layout.get_components():
            if component.item.is_clicked(x, y):
                component.item.on_click()

    def mouse_up_event(self):
        for component in self.__layout.get_components():
            if component.item.is_activated():
                component.item.flip_is_activated()

    def mouse_move_event(self):
        x, y = pygame.mouse.get_pos()
        for component in self.__layout.get_components():
            if component.item.is_activated():
                if not component.item.is_clicked(x, y):
                    component.item.flip_is_activated()

    def check_for_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__is_app_running[0] = False
            if event.type == pygame.MOUSEMOTION:
                self.mouse_move_event()
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_up_event()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down_event()
