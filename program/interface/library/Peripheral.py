from enum import Enum


class GpioType(Enum):
    INPUT = 0
    OUTPUT = 1


class GPIO:
    __slots__ = ('__gpio_type', '__name', '__value')

    def __init__(self, gpio_type: GpioType, name: str, value: bool):

        if type(gpio_type) is not GpioType:
            raise TypeError(gpioType)

        if type(name) is not str:
            raise TypeError(name)

        if type(value) is not bool:
            raise TypeError(value)

        self.__gpio_type: gpioType = gpio_type
        self.__name: str = name
        self.__value: bool = value

    def get_type(self) -> GpioType:
        return self.__gpio_type

    def set_type(self, val: GpioType):
        if type(gpioType) is not GpioType:
            raise TypeError(gpioType)
        self.__gpio_type = val

    def get_name(self) -> str:
        return self.__name

    def set_name(self, val: str):
        if type(name) is not str:
            raise TypeError(name)
        self.__name = val

    def get_value(self) -> GpioType:
        return self.__value

    def set_value(self, val: bool):
        if type(value) is not bool:
            raise TypeError(value)
        self.__value = val

    property(get_type, set_type)
    property(get_name, set_name)
    property(set_value, get_value)
