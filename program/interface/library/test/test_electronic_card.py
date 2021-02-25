from unittest import TestCase
from interface.library.ElectronicCard import Card
from interface.library.Peripheral import GPIO, GPIOType


class TestElectronicCard(TestCase):

    def test_new_class_with_good_parameters(self):
        test_object: Card = Card("test")
        self.assertEqual(test_object.name, "test")
        self.assertEqual(len(test_object.gpio), 0)

    def test_new_class_with_not_good_parameters(self):
        with self.assertRaises(TypeError):
            test_object: Card = Card(649798)

    def test_new_method(self):
        test_object: Card = Card("test")
        with self.assertRaises(AttributeError):
            test_object.test = "test"

    def test_set_gpio(self):
        test_object: Card = Card("test")
        test_object.add_gpio(GPIO(GPIOType.INPUT, "test", True))
        test_object.set_gpio(0, GPIO(GPIOType.INPUT, "test", False))
        self.assertEqual(len(test_object.gpio), 1)
        self.assertEqual(test_object.get_gpio(0).value, False)

    def test_get_gpio(self):
        test_object: Card = Card("test")
        val: int = 6566
        with self.assertRaises(TypeError):
            test_object.gpio.append(val)
            print(test_object.gpio)
