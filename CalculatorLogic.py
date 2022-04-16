import settings
from GridLayout import GridLayout
from TextField import TextField


class CalculatorLogic:

    def __init__(self, layout: GridLayout):
        self.__layout: GridLayout = layout
        self.__first_number: float = 0
        self.__action: str = ""
        self.__second_number: float = 0

    def on_number_action(self, key: str):
        if self.__action == "":
            value = str(self.__first_number)
            if len(str(value)) < settings.MAXIMAL_NUMBER_OF_DIGITS_IN_NUMBER:
                if value == "0":
                    value = key
                else:
                    value += key
                self.__first_number = int(value)
                self.update_textfield(value)
        else:
            value = str(self.__second_number)
            if len(str(value)) < settings.MAXIMAL_NUMBER_OF_DIGITS_IN_NUMBER:
                if value == "0":
                    value = key
                else:
                    value += key
                self.__second_number = int(value)
                self.update_textfield(value)

    def on_action_clear(self):
        if self.__action == "":
            self.__first_number = 0
        else:
            self.__second_number = 0
        self.update_textfield(0)

    def update_textfield(self, value: str):
        textfield = self.__layout.get_component_by_type("textfield")
        textfield[0].set_text(value)

    def notify(self, is_number_action: bool, text: str):
        if is_number_action:
            self.on_number_action(text)
        else:
            if text.lower() == "c":
                self.on_action_clear()

        print(f"action type: {is_number_action}, got value {text}")
