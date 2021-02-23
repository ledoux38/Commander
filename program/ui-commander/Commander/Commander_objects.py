from enum import Enum


class GPIOType(Enum):
    INPUT = 0
    OUTPUT = 1


class Carte:
    def __init__(self):
        pass


class GPIO:
    __slots__ = ('gpio_type', 'name', 'value')

    def __init__(self, gpio_type: GPIOType, name: str, value: bool):

        if type(gpio_type) is not GPIOType:
            raise TypeError(gpio_type)

        if type(name) is not str:
            raise TypeError(name)

        if type(value) is not bool:
            raise TypeError(value)

        self.gpio_type: GPIOType = gpio_type
        self.name: str = name
        self.value: bool = value


class Electronic_card:
    __slots__ = ('name', 'gpios')

    def __init__(self, name):
        if type(name) is not str:
            raise TypeError(name)

        self.gpios: [] = []
        self.name = name

    @property
    def gpios(self):
        return self.__gpios

    @gpios.setter
    def gpios(self, val: GPIO):
        if type(val) is not GPIO:
            raise TypeError(val)
