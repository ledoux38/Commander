from .Peripheral import GPIO


class Card:
    __slots__ = ('name', '__gpio')

    def __init__(self, name):
        if type(name) is not str:
            raise TypeError(name)

        self.__gpio: list = []
        self.name = name

    def get_gpio(self, index: int) -> GPIO:
        return self.__gpio[index]

    def get_all_gpio(self) -> []:
        return self.__gpio

    def set_gpio(self, index: int, val: GPIO):
        if type(val) is not GPIO:
            raise TypeError(val)
        self.__gpio[index] = val

    def add_gpio(self, val: GPIO):
        if type(val) is not GPIO:
            raise TypeError(val)

        self.__gpio.append(val)

    property(get_gpio, add_gpio)
