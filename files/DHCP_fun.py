from scapy.all import *

class cDHCP:
    def __init__(self, dest_address, port_list):
        self.dest_address=dest_address
        self.port_list=port_list
        self.dest_port=67
        self.source_port=68
        self.ip_list = []
        self.dhcp_result=None
        self.DHCP_check()

    def dhcp_discover(self):
        dst_mac = "ff:ff:ff:ff:ff:ff"
        src_mac = get_if_hwaddr(conf.iface)
        spoofed_mac = RandMAC()
        options = [("message-type", "discover"),
                   ("max_dhcp_size",1500),
                   ("client_id", mac2str(spoofed_mac)),
                   ("lease_time",10000),
                   ("end","0")]
        transaction_id = random.randint(1, 900000000)
        dhcp_request = Ether(src=src_mac,dst=dst_mac)\
                        /IP(src="0.0.0.0",dst="255.255.255.255")\
                        /UDP(sport=self.source_port,dport=self.dest_port)\
                        /BOOTP(chaddr=[mac2str(spoofed_mac)],
                                       xid=transaction_id,
                                       flags=0xFFFFFF)\
                        /DHCP(options=options)
        sendp(dhcp_request, iface=conf.iface)

    def print_packet(self, packet):
        ip_layer = packet.getlayer(IP)

        self.ip_list.append(ip_layer.src)
        return self.ip_list

    def DHCP_check(self):
        self.dhcp_discover()
        sniff(filter="port 68", prn=self.print_packet, timeout=3)
        DHCP_service=False
        for i in self.ip_list:
            if str(i)==str(self.dest_address):
                DHCP_service=True
        self.ip_list.clear()
        DHCP = (self.dest_port in self.port_list)
        if (DHCP_service == True and DHCP == False):
            self.dhcp_result = "DHCP should be closed, but is open!"
        if (DHCP_service == False and DHCP == True):
            self.dhcp_result = "DHCP should be open, but is closed!"
        else:
            self.dhcp_result = "DHCP is good"


#------test
#port=[53,67]
#add='192.168.1.1'
#dhcp_instance=cDHCP(add,port)
#dhcp_result=dhcp_instance.dhcp_result
#print(dhcp_result)

