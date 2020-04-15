import socket

class cTCP:
    def __init__(self, address, port_list, first, last):
        self.address=address
        self.port_list=port_list
        self.first=first
        self.last=last
        self.open_ports=[]
        self.result = 'TCP scan result:\n'
        self.scaning()
        self.check()

    def scaning(self):
        for port in range(self.first, self.last):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((self.address, port))  # try connect
            if (result == 0):  # if connect is good add to list
                self.open_ports.append(port)

    def check(self):
        flag = True
        for i in self.open_ports:
            check = (i in self.port_list)
            if (check == False):  # if no
                self.result = self.result +("Warning! Port {} should be closed!".format(i))+"\n"
                flag = False  #detection flag
        if flag == True:
            self.result = self.result + "TCP is good\n"


#-------test
#adres="127.0.0.1"
#porty=[53,81]
#pierwszy=50
#ostatni=1000
#tcp_instance=cTCP(adres,porty,pierwszy,ostatni)
#print(tcp_instance.result)