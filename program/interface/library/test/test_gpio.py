from unittest import TestCase

from program.interface.library.Peripheral import GPIO, GpioType


class TestGPIO(TestCase):

    def test_new_class_with_good_parameters(self):
        test_object: GPIO = GPIO(GpioType.INPUT, "test", True)
        self.assertEqual(test_object.get_type(), GpioType.INPUT)
        self.assertEqual(test_object.get_name(), "test")
        self.assertEqual(test_object.get_value(), True)

    def test_new_class_with_not_good_parameters(self):
        with self.assertRaises(TypeError):
            test_object: GPIO = GPIO(GpioType.INPUT, "test", "test")

    def test_new_method(self):
        test_object: GPIO = GPIO(GpioType.INPUT, "test", True)
        with self.assertRaises(AttributeError):
            test_object.test = "test"
