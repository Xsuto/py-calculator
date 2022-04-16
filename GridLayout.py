from dataclasses import dataclass

import settings
from Component import Component


# dataclass is c like struct
@dataclass
class GridItem:
    item: Component
    grid_row_start: int
    grid_row_end: int
    grid_column_start: int
    grid_column_end: int


class GridLayout:
    def __init__(self, width: int, height: int, rows: int, columns: int):
        self.__components: [GridItem] = []
        self.__width = width
        self.__height = height
        self.__rows = rows
        self.__columns = columns

    def get_component_by_type(self, component_type: str) -> [Component]:
        output: [Component] = []
        for component in self.__components:
            if component.item.get_type() == component_type:
                output.append(component.item)
        return output

    def get_components(self):
        return self.__components

    def addComponent(self, component: Component, grid_row_start: int = 0, grid_row_end: int = 0,
                     grid_column_start: int = 0,
                     grid_column_end: int = 0):
        component.set_x(grid_column_start * (self.__width // self.__columns))
        component.set_y(grid_row_start * (self.__height // self.__rows))
        component.set_width(self.__width // self.__columns * (grid_column_end - grid_column_start))
        component.set_height(self.__height // self.__rows * (grid_row_end - grid_row_start))
        if settings.DEBUG_POSITION:
            print(f"component x,y:{component.get_x()},{component.get_y()}"
                  f"\ncomponent width: height: {component.get_width()},{component.get_height()}\n")
        self.__components.append(GridItem(component, grid_row_start, grid_row_end, grid_column_start, grid_column_end))

    def draw(self):
        for component in self.__components:
            component.item.draw()
