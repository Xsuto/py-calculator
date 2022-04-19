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
            # alternative keybind for equal operation
            if key == "return":
                return "="
            return key

    def get_alternative_key(self, event: pygame.event):
        key = pygame.key.name(event.key)
        if key == "8":
            return "*"
        if key == "=":
            return "+"
        if key == "5":
            return "%"
        if key == "return":
            return "="

    def mouse_down_event(self):
        x, y = pygame.mouse.get_pos()
        for component in self.__layout.get_components():
            if component.is_clicked(x, y):
                component.set_is_activated(True)

    def mouse_up_event(self):
        for component in self.__layout.get_components():
            if component.is_activated():
                print(component.get_text())
                component.set_is_activated(False)
                self.notify_calculator_logic(component.get_text())

    def mouse_move_event(self):
        x, y = pygame.mouse.get_pos()
        for component in self.__layout.get_components():
            if component.is_activated():
                if not component.is_clicked(x, y):
                    component.set_is_activated(False)

    def on_keyup_event(self, event: pygame.event):
        for button in self.__layout.get_component_by_type("button"):
            if (button.get_text().lower() == self.get_key(
                    event) or button.get_text().lower() == self.get_alternative_key(event)) and button.is_activated():
                button.set_is_activated(False)

    def on_keydown_event(self, event: pygame.event):
        key = self.get_key(event)
        for button in self.__layout.get_component_by_type("button"):
            if button.get_text().lower() == key:
                self.notify_calculator_logic(key)
                button.set_is_activated(True)

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
