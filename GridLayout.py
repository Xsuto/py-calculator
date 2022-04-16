from dataclasses import dataclass

import settings
from Component import Component


# dataclass is c like struct
@dataclass
class GridItem:
    component: Component
    grid_row_start: int
    grid_row_end: int
    grid_column_start: int
    grid_column_end: int


class GridLayout:
    def __init__(self, width: int, height: int, rows: int, columns: int):
        self.__items: [GridItem] = []
        self.__width = width
        self.__height = height
        self.__rows = rows
        self.__columns = columns

    def get_component_by_type(self, component_type: str) -> [Component]:
        output: [Component] = []
        for component in self.get_components():
            if component.get_type() == component_type:
                output.append(component)
        return output

    def get_components(self):
        return [item.component for item in self.__items]

    def addComponent(self, component: Component, grid_row_start: int = 0, grid_row_end: int = 0,
                     grid_column_start: int = 0,
                     grid_column_end: int = 0):
        if not self.check_for_collision(grid_row_start, grid_row_end, grid_column_start, grid_column_end):
            component.set_x(grid_column_start * (self.__width // self.__columns))
            component.set_y(grid_row_start * (self.__height // self.__rows))
            component.set_width(self.__width // self.__columns * (grid_column_end - grid_column_start))
            component.set_height(self.__height // self.__rows * (grid_row_end - grid_row_start))
            if settings.DEBUG_POSITION:
                print(f"component x,y:{component.get_x()},{component.get_y()}"
                      f"\ncomponent width: height: {component.get_width()},{component.get_height()}\n")
            self.__items.append(GridItem(component, grid_row_start, grid_row_end, grid_column_start, grid_column_end))

    def check_for_collision(self, grid_row_start: int, grid_row_end: int,
                            grid_column_start,
                            grid_column_end):
        for item in self.__items:
            if item.grid_row_start == grid_row_start and item.grid_row_end == grid_row_end:
                if item.grid_column_start == grid_column_start and item.grid_column_end == grid_column_end:
                    print(f"\nERROR: Components at "
                          f"\ngrid_row_start,grid_row_end:{grid_row_start},{grid_row_end}"
                          f"\ngrid_column_start: grid_column_end: {grid_column_start},{grid_column_end}\n"
                          f"Collided")
                    return True
        return False

    def draw(self):
        for component in self.get_components():
            component.draw()
