import datetime
import sys
import socket
from files import tcp_scanning
from files import udp_scanning
import os

class cMAIN:
    def __init__(self, input_file):
        self.input_file=input_file
        self.data=[line.strip() for line in open(self.input_file, "r")]
        self.check_lines()
        self.check_data()
        self.address = self.data[0]
        self.TCP_port_list = list(map(int, self.data[1].split(',')))
        self.UDP_port_list = list(map(int, self.data[2].split(',')))
        self.first = int(self.data[3])
        self.last = int(self.data[4])
        self.sleep_time = int(self.data[5]) * 60

    def check_lines(self):
        if len(self.data) != 6:
            print("Bad input file syntax!")
            exit(0)

    def check_data(self):
        try:
            socket.inet_aton(self.data[0])
        except socket.error:
            print("Invalid input address!")
        try:
            list(map(int, self.data[1].split(',')))
        except:
            print("Ports are not intiger")
        try:
            list(map(int, self.data[2].split(',')))
        except:
            print("Ports are not intiger")
        try:
            int(self.data[3])
        except:
            print("First port is not intiger")
        try:
            int(self.data[4])
        except:
            print("Last port is not intiger")
        if int(self.data[3]) >= int(self.data[4]):
            print("Last port is lower than first one")
            exit(0)
        try:
            int(self.data[5])
        except:
            print("Loop time is not intiger")

    def scan_process(self):
        while True:
            now=datetime.datetime.now()
            year=now.strftime("%Y")
            month=now.strftime("%m")
            day=now.strftime("%d")
            time=now.strftime("%H:%M:%S")
            raport="Scanning report "+now.strftime('%d/%m/%Y, %H:%M:%S')+"\n"

            tcp_instance=tcp_scanning.cTCP(self.address,self.TCP_port_list,self.first,self.last)
            raport=(raport+tcp_instance.result)

            udp_instance=udp_scanning.cUDP(self.address,self.UDP_port_list)
            raport=(raport+udp_instance.result)
            print(raport)
            today = ('{}-{}-{}').format(day, month, year)
            file_name = ("raport ip:{} date: {} ".format(self.address, today))
            path=os.path.join('raports', file_name)
            with open(path, 'a') as file:
                file.write(raport + "\n")

            import time
            time.sleep(self.sleep_time)

def main():
    scanner_instance = cMAIN(sys.argv[1])
    scanner_instance.scan_process()

if __name__ == "__main__":
    main()

