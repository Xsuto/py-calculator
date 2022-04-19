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
        # If we just compute equal and we clicked on a number then the first_number should be overwritten
        # For example 4 + 5 = 9 -> click 1 -> first number should be 1 instead of 91
        self.__just_compute_equal = False

    def add_number_to(self, number_as_str: str, to: float, should_be_after_dot: bool):
        value = str(to)
        if len(value) - 1 < settings.MAXIMAL_NUMBER_OF_DIGITS_IN_NUMBER:
            if should_be_after_dot:
                dot = value.find(".")
                if dot > 0:
                    if value[dot + 1] == "0":
                        output = f"{value[0:dot]}.{number_as_str}"
                        self.update_textfield(output)
                        return float(output)
                    output = value + number_as_str
                    self.update_textfield(output)
                    return float(output)
                else:
                    output = f"{value}.{number_as_str}"
                    self.update_textfield(output)
                    return float(output)
            elif to == 0:
                output = float(number_as_str)
                self.update_textfield(self.formatted_output(output))
                return float(output)
            else:
                output = to * 10 + int(number_as_str)
                self.update_textfield(self.formatted_output(output))
                return output
        return to

    def update_textfield(self, text: str):
        textfield = self.__layout.get_component_by_type("textfield")
        if len(textfield):
            textfield[0].set_text(text)

    # Formatted output for textfield If number is bigger than Maximal_..._Number or already has 13.1313+e13 then,
    # function will return 13+e13 (for example) If number == 13.0  it will convert it to 13
    def formatted_output(self, x: float, should_have_dot: bool = False) -> str:
        value = str(x)
        if should_have_dot:
            return f"{round(x)}."
        if 1 > x > -1:
            return value if x != 0 else 0
        if int(x) / x == 1:
            return str(int(x))

        return str(x)

    def on_action_equal(self):
        print(f"Before action\nfirst: {self.__first_number}, second: {self.__second_number}, action: {self.__action}")
        # if we are adding or subtracting for example 1.1 + 2.2 we will get 3.30000005432111 because of round-off
        # error. We want to display 3.3, so we need to round number.
        # [::-1] will reverse string so 1.2345 -> 2345.1.find(".") -> 4
        first_number_decimal_numbers = str(self.__first_number)[::-1].find(".")
        second_number_decimal_numbers = str(self.__second_number)[::-1].find(".")
        round_to = first_number_decimal_numbers if first_number_decimal_numbers > second_number_decimal_numbers else second_number_decimal_numbers
        if self.__action == "+":
            self.__first_number = round(self.__first_number + self.__second_number, round_to)
        elif self.__action == "-":
            self.__first_number = round(self.__first_number - self.__second_number, round_to)
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

        print(f"After action\nfirst: {self.__first_number}, second: {self.__second_number}, action: {self.__action}")
        self.__second_number = 0
        self.__action = ""
        self.__first_number_dot = False
        self.__second_number_dot = False
        self.__just_compute_equal = True
        self.update_textfield(self.formatted_output(self.__first_number))

    def on_action_number(self, number_as_str: str):
        if self.__action == "":
            self.__first_number = self.add_number_to(number_as_str, self.__first_number, self.__first_number_dot)
        else:
            self.__second_number = self.add_number_to(number_as_str, self.__second_number, self.__second_number_dot)

    def on_action_clear(self):
        if self.__action == "":
            self.__first_number = 0
            self.__first_number_dot = False
        else:
            self.__second_number = 0
            self.__second_number_dot = False
        self.update_textfield(0)

    def on_action_reverse_sign(self):
        if self.__action == "":
            self.__first_number = -self.__first_number
            self.update_textfield(self.formatted_output(self.__first_number))
        else:
            self.__second_number = -self.__second_number
            self.update_textfield(self.formatted_output(self.__second_number))

    def on_action_percentage(self):
        if self.__action == "":
            self.__first_number *= 0.01
            self.update_textfield(self.formatted_output(self.__first_number))
        else:
            self.__second_number *= 0.01
            self.update_textfield(self.formatted_output(self.__second_number))

    def on_action_dot(self):
        if self.__action == "":
            self.__first_number_dot = True
            self.update_textfield(self.formatted_output(self.__first_number, self.__first_number_dot))
        else:
            self.__second_number_dot = True
            self.update_textfield(self.formatted_output(self.__second_number, self.__second_number_dot))

    # Thanks to this function EventHandler can communicate with us
    def notify(self, is_number_action: bool, value: str):
        if is_number_action:
            if self.__just_compute_equal:
                self.__first_number = 0
                self.__just_compute_equal = False
            self.on_action_number(value)
        else:
            # Dot action is special action that should reset first number if just_compute_equal
            if value == ".":
                if self.__just_compute_equal:
                    self.__just_compute_equal = False
                    self.__first_number = 0
                self.on_action_dot()
                return

            self.__just_compute_equal = False
            if value.lower() == "c":
                self.on_action_clear()
            elif value == "=":
                self.on_action_equal()
            elif value == "+/-":
                self.on_action_reverse_sign()
            elif value == "%":
                self.on_action_percentage()
            else:
                self.__action = value
