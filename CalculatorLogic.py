import settings
from GridLayout import GridLayout


class CalculatorLogic:

    def __init__(self, layout: GridLayout):
        self.__layout: GridLayout = layout
        self.__first_number: float = 0
        self.__first_number_dot = False
        self.__action: str = ""
        self.__second_number: float = 0
        self.__second_number_dot = False
        self.__just_compute_equal = False

    def on_number_action(self, number_as_str: str):

        if self.__action == "":
            value = str(self.__first_number)
            if len(str(value)) < settings.MAXIMAL_NUMBER_OF_DIGITS_IN_NUMBER:
                if self.__first_number_dot:
                    if value[len(value) - 1] == "0":
                        value = value[:len(value) - 1] + number_as_str
                    else:
                        value += number_as_str
                else:
                    value = str(int(float(value)))
                    if value == "0":
                        value = number_as_str
                    else:
                        value += number_as_str

                self.__first_number = float(value)
                self.update_textfield(value)
        else:
            value = str(self.__second_number)
            if len(str(value)) < settings.MAXIMAL_NUMBER_OF_DIGITS_IN_NUMBER:
                if self.__second_number_dot:
                    if value[len(value) - 1] == "0":
                        value = value[:len(value) - 1] + number_as_str
                    else:
                        value += number_as_str
                else:
                    value = str(int(float(value)))
                    if value == "0":
                        value = number_as_str
                    else:
                        value += number_as_str
                self.__second_number = float(value)
                self.update_textfield(value)

    def on_action_clear(self):
        if self.__action == "":
            self.__first_number = 0
            self.__first_number_dot = False
        else:
            self.__second_number = 0
            self.__second_number_dot = False
        self.update_textfield(0)

    def update_textfield(self, text: str):
        textfield = self.__layout.get_component_by_type("textfield")
        if len(textfield):
            textfield[0].set_text(text)

    # Formatted output for textfield
    # If number == 13.0  it will convert it to 13
    def formatted_output(self, x: float) -> str:
        if 1 > x > -1:
            return str(x) if x != 0 else 0
        return str(int(x) if x % int(x) == 0 else x)

    def equal(self):

        if self.__action == "+":
            self.__first_number = self.__first_number + self.__second_number
        elif self.__action == "-":
            self.__first_number = self.__first_number - self.__second_number
        elif self.__action == "*":
            self.__first_number = self.__first_number * self.__second_number
        elif self.__action == "/":
            try:
                self.__first_number = self.__first_number / self.__second_number
            except ZeroDivisionError:
                self.__first_number = 0
                self.__second_number = 0
                self.__action = ""
                self.__first_number_dot = False
                self.__second_number_dot = False
                self.update_textfield("Not a Number")
                return

        if len(str(self.__first_number)) > settings.MAXIMAL_NUMBER_OF_DIGITS_IN_NUMBER:
            self.__first_number = round(self.__first_number, settings.MAXIMAL_NUMBER_OF_DIGITS_IN_NUMBER)
        self.__second_number = 0
        self.__action = ""
        self.__first_number_dot = False
        self.__second_number_dot = False
        self.__just_compute_equal = True
        self.update_textfield(self.formatted_output(self.__first_number))

    def reverse_sign(self):
        if self.__action == "":
            self.__first_number = -self.__first_number
            self.update_textfield(self.formatted_output(self.__first_number))
        else:
            self.__second_number = -self.__second_number
            self.update_textfield(self.formatted_output(self.__second_number))

    def percentage(self):
        if self.__action == "":
            self.__first_number *= 0.01
            self.update_textfield(self.formatted_output(self.__first_number))
        else:
            self.__second_number *= 0.01
            self.update_textfield(self.formatted_output(self.__second_number))

    def dot(self):
        if self.__action == "":
            self.__first_number_dot = True
        else:
            self.__second_number_dot = True

    def notify(self, is_number_action: bool, text: str):
        if is_number_action:
            if self.__just_compute_equal:
                self.__first_number = 0
                self.__just_compute_equal = False
            self.on_number_action(text)
        else:
            self.__just_compute_equal = False
            if text.lower() == "c":
                self.on_action_clear()
            elif text == "=":
                self.equal()
            elif text == "+/-":
                self.reverse_sign()
            elif text == "%":
                self.percentage()
            elif text == ".":
                self.dot()
            else:
                self.__action = text
