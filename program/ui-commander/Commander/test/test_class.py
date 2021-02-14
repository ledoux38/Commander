from unittest import TestCase

from Commander.Commander_objects import GPIO, GPIOType


class TestGPIO(TestCase):

    def test_new_class_with_good_parameters(self):
        test_object: GPIO = GPIO(GPIOType.INPUT, "test", True)
        self.assertEqual(test_object.gpio_type, GPIOType.INPUT)
        self.assertEqual(test_object.name, "test")
        self.assertEqual(test_object.value, True)

    def test_new_class_with_not_good_parameters(self):
        with self.assertRaises(TypeError):
            test_object: GPIO = GPIO("test", "test", "test")
