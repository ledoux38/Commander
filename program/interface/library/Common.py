import os
import platform


class Utils(object):
    @staticmethod
    def Scanner(base_addr: str, min: int, max: int) -> list:
        ip_returned: list = []
        base_adder_split: [] = base_addr.split('.')
        new_addr: str = base_adder_split[0] + '.' + base_adder_split[1] + '.' + base_adder_split[2] + '.'

        sys_os = platform.system()

        if (sys_os == "Windows"):
            cmd_ping = "ping -n 1 "
        elif (sys_os == "Linux"):
            cmd_ping = "ping -c 1 "
        else:
            cmd_ping = "ping -c 1 "

        for ip in range(min, max):
            addr = new_addr + str(ip)
            comm = cmd_ping + addr
            response = os.popen(comm)

            for line in response.readlines():
                if (line.count("ttl")):
                    ip_returned.append(addr)

        return ip_returned


if __name__ == '__main__':
    print(Utils.Scanner("182.168.1", 20, 25))
