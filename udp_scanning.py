import DNS_fun
import DHCP_fun
import TFTP_fun

class cUDP:
    def __init__(self, address, port_list):
        self.address=address
        self.port_list=port_list
        self.result='UDP scan result:\n'
        self.dns_scan()
        self.dhcp_scan()
        self.tftp_scan()

    def dns_scan(self):
        dns_instance=DNS_fun.cDNS(self.address, self.port_list)
        dns_result=dns_instance.DNS_result+'\n'
        self.result= self.result+ dns_result

    def dhcp_scan(self):
        dhcp_instance=DHCP_fun.cDHCP(self.address, self.port_list)
        dhcp_result = dhcp_instance.dhcp_result+'\n'
        self.result = self.result + dhcp_result

    def tftp_scan(self):
        tftp_instance = TFTP_fun.cTFTP(self.address, self.port_list)
        tftp_result = tftp_instance.TFTP_result+'\n'+'\n'
        self.result = self.result + tftp_result


#----test
#adres='127.0.0.1'
#porty=[1,2]
#udp_instace=cUDP(adres,porty)
#print(udp_instace.result)

