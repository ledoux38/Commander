import os
import platform
import ipaddress
import socket
from .Settings import *

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
        list_ip_ok: list = []
        address_converted_to_ip: Ip = Ip(addr)
        min: int = int(address_converted_to_ip.Get_value_by_index(3))
        if min > max:
            raise ValueError(str(min) + ">" + str(max))
        for num in range(min, max):
            address_converted_to_ip.Set_value_by_index(3, num)
            if Utils.Connection_to_IP(str(address_converted_to_ip), PORT):
                list_ip_ok.append(str(address_converted_to_ip))

        return list_ip_ok

    @staticmethod
    def Connection_to_IP(addr: str, port: int) -> bool:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((addr, port))
        s.close()
        if result == 0:
            return 1
        else:
            return 0


class Ip(object):
    __slots__ = '__ip'

    def __init__(self, ip: str):
        if type(ip) != str:
            raise TypeError(name)

        self.__ip: [str] = []

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
