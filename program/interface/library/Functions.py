import socket
import threading

Hosts = {}


class Scanner(threading.Thread):
    '''https://tutoriels.pecaudchristopher.com/tutoriels_windows/espace_python/Tutoriel_Creation_Scanner_IP_Python.php'''
    def __init__(self, addr: str):
        self.addr = addr
        threading.Thread.__init__(self)

    def run(self):
        self.lookup(self.addr)

    def lookup(self, addr:str):
        try:
            hostname, alias, _ = socket.gethostbyaddr(addr)
            global host
            host[address] = hostname

        except socket.herror:
            host[address] = None




    def scanner(self):
        for ping in range(1, 254):
            address = "192.168.1." + str(ping)
            socket.setdefaulttimeout(1)

            try:
                hostname, alias, addresslist = socket.gethostbyaddr(address)
            except socket.herror:
                hostname = None
                alias = None
                addresslist = address

            print(addresslist, '=>', hostname)
