from unittest import TestCase
from program.interface.library.Common import Utils


class Test_common(TestCase):
    def test_check_ip_with_good_parameter(self):
        self.assertEqual(Utils.Check_ip_is_valid('192.168.1.22'), True)

    def test_check_ip_with_bad_parameter(self):
        self.assertEqual(Utils.Check_ip_is_valid('192.168.1.tototo'), False)

