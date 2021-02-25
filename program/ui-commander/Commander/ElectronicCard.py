from Commander import GPIO


class Electronic_card:
    __slots__ = ('name', 'gpio')

    def __init__(self, name):
        if type(name) is not str:
            raise TypeError(name)

        self.gpio: list = {}
        self.name = name

    def get_gpio(self, index: int) -> GPIO:
        print("get")
        return self.gpio[index]

    def set_gpio(self, index: int, val: GPIO):
        print("set")
        if type(val) is not GPIO:
            raise TypeError(val)

    def add_gpio(self, val: GPIO):
        print("add")
        if type(val) is not GPIO:
            raise TypeError(val)

        self.gpio.append(val)

    property(get_gpios, add_gpio)
