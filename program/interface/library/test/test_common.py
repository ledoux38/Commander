from unittest import TestCase
from program.interface.library.Common import Utils, Ip


class Test_Utils(TestCase):
    def test_check_ip_with_good_parameter(self):
        self.assertEqual(Utils.Check_ip_is_valid('192.168.1.22'), True)

    def test_check_ip_with_bad_parameter_0(self):
        self.assertEqual(Utils.Check_ip_is_valid('192.168.1.tototo'), False)

    def test_check_ip_with_bad_parameter_1(self):
        self.assertEqual(Utils.Check_ip_is_valid('192.168.1.'), False)

    def test_Scanner(self):
        self.assertEqual(Utils.Scanner('192.168.1.20', 23), ['192.168.1.22'])



class Test_Ip(TestCase):
    def test_ip_object_with_good_parameter(self):
        val: Ip = Ip('192.168.1.22')
        self.assertEqual(val.Get_ip(), ['192', '168', '1', '22'])

    def test_check_ip_object_with_bad_parameter(self):
        with self.assertRaises(ValueError):
            val: Ip = Ip('192.168.1.tototo')

    def test_ip_object_str(self):
        val: Ip = Ip('192.168.1.22')
        self.assertEqual(val.__str__(), '192.168.1.22')

    def test_ip_object_set_val_by_index(self):
        val: Ip = Ip('192.168.1.22')
        val.Set_value_by_index(3, 20)
        self.assertEqual(val.Get_ip(), ['192', '168', '1', '20'])
