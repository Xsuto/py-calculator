import pygame

from CalculatorLogic import CalculatorLogic
from GridLayout import GridLayout


class EventHandler():
    def __init__(self, layout: GridLayout, calculator_logic: CalculatorLogic, running: [bool]):
        self.__layout = layout
        self.__calculator_logic = calculator_logic
        self.__is_app_running = running

    def notify_calculator_logic(self, text: str or int):
        try:
            # We are doing this just to check if button text is a number if not it will throw exception
            int(text)
        except ValueError:
            print("error",text)
            self.__calculator_logic.notify(False, text)
            return

        self.__calculator_logic.notify(True, text)

    def get_key(self, event: pygame.event) -> str:
        is_shift_pressed = pygame.key.get_mods() & pygame.KMOD_SHIFT
        key = pygame.key.name(event.key)
        if is_shift_pressed:
            if key == "8":
                return "*"
            if key == "=":
                return "+"
            if key == "5":
                return "%"
        else:
            return key

    def mouse_down_event(self):
        x, y = pygame.mouse.get_pos()
        for component in self.__layout.get_components():
            if component.item.is_clicked(x, y):
                component.item.on_click()

    def mouse_up_event(self):
        for component in self.__layout.get_components():
            if component.item.is_activated():
                component.item.flip_is_activated()
                text = component.item.get_text()
                self.notify_calculator_logic(text)

    def mouse_move_event(self):
        x, y = pygame.mouse.get_pos()
        for component in self.__layout.get_components():
            if component.item.is_activated():
                if not component.item.is_clicked(x, y):
                    component.item.flip_is_activated()

    def on_keyup_event(self, event: pygame.event):
        key = self.get_key(event)
        for button in self.__layout.get_component_by_type("button"):
            if button.get_text().lower() == key:
                self.notify_calculator_logic(key)
                button.flip_is_activated()

    def on_keydown_event(self, event: pygame.event):
        key = self.get_key(event)
        for button in self.__layout.get_component_by_type("button"):
            if button.get_text().lower() == str(key):
                button.flip_is_activated()

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
            if event.type == pygame.KEYUP:
                self.on_keyup_event(event)
            if event.type == pygame.KEYDOWN:
                self.on_keydown_event(event)
