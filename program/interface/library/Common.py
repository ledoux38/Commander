import os
import platform
import ipaddress
from ping3 import ping, verbose_ping


class Utils(object):
    @staticmethod
    def Check_ip_is_valid(ip: str) -> bool:
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

    @staticmethod
    def Scanner(addr: str, max: int) -> list:
        ip_returned: list = []
        ip: Ip = Ip(addr)
        min: int = int(ip.Get_value_by_index(3))
        if min > max:
            raise ValueError(str(min) + ">" + str(max))
        for num in range(min, max):
            ip.Set_value_by_index(3, num)
            response = ping(ip.__str__())
            if response is not None and response != False:
                ip_returned.append(ip.__str__())

        return ip_returned


class Ip(object):
    def __init__(self, ip: str):
        self.Set_ip(ip)

    def __str__(self) -> str:
        returned_val: str = ""
        for index, val in enumerate(self.__ip):
            if index > 0:
                returned_val += "." + val
            else:
                returned_val += val
        return returned_val

    def Get_ip(self) -> [str]:
        return self.__ip

    def Set_ip(self, new_ip: str):
        if Utils.Check_ip_is_valid(new_ip):
            self.__ip = new_ip.split(".")
        else:
            raise ValueError(new_ip)

    def Set_value_by_index(self, index: int, value: int):
        value = str(value)
        self.__ip[index] = value

    def Get_value_by_index(self, index: int) -> str:
        return self.__ip[index]

    property(Get_ip, Set_ip)
