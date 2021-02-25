from unittest import TestCase

from Commander.ElectronicCard import Electronic_card


class TestElectronicCard(TestCase):

    def test_new_class_with_good_parameters(self):
        test_object: Electronic_card = Electronic_card("test")
        self.assertEqual(test_object.name, "test")
        self.assertEqual(len(test_object.gpio), 0)

    def test_new_class_with_not_good_parameters(self):
        with self.assertRaises(TypeError):
            test_object: Electronic_card = Electronic_card(649798)

    def test_new_method(self):
        test_object: Electronic_card = Electronic_card("test")
        with self.assertRaises(AttributeError):
            test_object.test = "test"

    def test_set_gpio(self):
        test_object: Electronic_card = Electronic_card("test")
        test_object.add_gpio(GPIO(GPIOType.INPUT, "test", True))
        test_object.set_gpio(0, GPIO(GPIOType.INPUT, "test", False))
        self.assertEqual(len(test_object.gpio), 1)
        self.assertEqual(test_object.get_gpio(0), 1)

    def test_get_gpio(self):
        test_object: Electronic_card = Electronic_card("test")
        val: int = 6566
        with self.assertRaises(TypeError):
            test_object.gpio.append(val)
