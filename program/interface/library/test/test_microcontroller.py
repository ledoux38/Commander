from unittest import TestCase
from library.Microcontroller import Card
from library.Peripheral import GPIO, GpioType


class Test_microcontroller(TestCase):

    def test_new_class_with_good_parameters(self):
        test_object: Card = Card("test")
        self.assertEqual(test_object.name, "test")
        self.assertEqual(len(test_object.get_all_gpio()), 0)

    def test_new_class_with_not_good_parameters(self):
        with self.assertRaises(TypeError):
            test_object: Card = Card(649798)

    def test_new_method(self):
        test_object: Card = Card("test")
        with self.assertRaises(AttributeError):
            test_object.test = "test"

    def test_set_gpio(self):
        test_object: Card = Card("test")
        test_object.add_gpio(GPIO(GpioType.INPUT, "test", True))
        test_object.set_gpio(0, GPIO(GpioType.INPUT, "test", False))
        self.assertEqual(len(test_object.get_all_gpio()), 1)
        self.assertEqual(test_object.get_gpio(0).get_value(), False)

    def test_get_gpio(self):
        test_object: Card = Card("test")
        val: int = 6566
        with self.assertRaises(AttributeError):
            test_object.__gpio.append(val)
