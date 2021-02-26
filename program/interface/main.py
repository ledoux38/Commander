from program.interface.library.Functions import scanner

if __name__ == '__main__':
    addresses = []

    """ On définit une plage d'adresses IP à scanner """
    for ping in range(1, 254):
        addresses.append("192.168.0." + str(ping))

    threads = []

    """ On créée autant de threads qu'il y à d'adresses IP à scanner """
    netscanthreads = [NetscanThread(address) for address in addresses]
    for thread in netscanthreads :
        """ Chaque thread est démarré en même temps """
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

    """ On affiche le résultat qui affiche pour chaque machine connectée son nom d'hôte """
    for address, hostname in host.items():
        if (hostname != None):
            print(address, '=>', hostname)