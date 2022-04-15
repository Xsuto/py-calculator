from dataclasses import dataclass


@dataclass
class Calculation:
    first_number: float
    action: str
    second_number: float

class CalculatorLogic:

    def __init__(self):
        pass