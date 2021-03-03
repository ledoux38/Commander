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
        if Utils.Check_ip_is_valid(addr):
            min: int = int(addr.split(".")[3])
            if min > max:
                raise ValueError(srt(min) + ">" + str(max))
            for num in range(min, max):
                ip: str = new_addr + str(num)
                response = ping(ip)
                if response is not None and response != False:
                    ip_returned.append(ip)
        else:
            raise ValueError(addr)

        return ip_returned
