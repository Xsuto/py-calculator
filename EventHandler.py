import pygame

from CalculatorLogic import CalculatorLogic
from GridLayout import GridLayout


class EventHandler:
    def __init__(
        self,
        layout: GridLayout,
        calculator_logic: CalculatorLogic,
    ):
        self.__layout = layout
        self.__calculator_logic = calculator_logic

    def notify_calculator_logic(self, text: str):
        try:
            # We are doing this just to check if button text is a number if not it will throw exception
            int(text)
        except ValueError:
            self.__calculator_logic.notify(False, text)
            return

        self.__calculator_logic.notify(True, text)

    def get_key(self, event: pygame.event) -> str:
        is_shift_pressed = pygame.key.get_mods() & pygame.KMOD_SHIFT
        if is_shift_pressed:
            return self.get_alternative_key(event)
        else:
            key = pygame.key.name(event.key)
            # alternative keybind for equal operation
            if key == "return":
                return "="
            # Numpad support. If we press key on numpad then pygame.key.name will return [key]
            # For example for numpad 0 return [0]. key[2] might be out of range we have to put it in try block
            try:
                if key[0] == "[" and key[2] == "]":
                    return key[1]
            except IndexError:
                pass
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
                component.set_is_activated(False)
                self.notify_calculator_logic(component.get_text())

    def mouse_move_event(self):
        x, y = pygame.mouse.get_pos()
        for component in self.__layout.get_components():
            if component.is_activated():
                if not component.is_clicked(x, y):
                    # If we pressed on button and then moved away cursor from it, we should deactivate this button.
                    component.set_is_activated(False)

    def on_keyup_event(self, event: pygame.event):
        for button in self.__layout.get_components_by_type("button"):
            # We are checking directly button text with alternative key because user might press shift and =
            # (activated +) and then releases shift then =, so in that case we should deactivate +
            if (
                button.get_text().lower() == self.get_key(event)
                or button.get_text().lower() == self.get_alternative_key(event)
            ) and button.is_activated():
                button.set_is_activated(False)

    def on_keydown_event(self, event: pygame.event):
        key = self.get_key(event)
        for button in self.__layout.get_components_by_type("button"):
            if button.get_text().lower() == key:
                self.notify_calculator_logic(key)
                button.set_is_activated(True)

    def check_for_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
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
