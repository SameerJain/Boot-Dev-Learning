class Unit:
    def __init__(self, name: str, pos_x: int, pos_y: int) -> None:
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1: int, y_1: int, x_2: int, y_2: int) -> bool:
        if (x_1 <= self.pos_x <= x_2) and (y_1 <= self.pos_y <= y_2):
            print(self.pos_x, self.pos_y)
            print(x_1, y_1, x_2, y_2)
            return True
        return False


class Dragon(Unit):
    def __init__(self, name: str, pos_x: int, pos_y: int, fire_range: int) -> None:
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x: int, y: int, units: list[Unit]) -> list[Unit]:
        result = []
        for unit in units:
            print(self.__fire_range)
            if unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            ):
                result.append(unit)
        return result
