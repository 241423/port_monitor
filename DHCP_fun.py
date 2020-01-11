from scapy.all import *

#-----Create dhcp packet and send
def dhcp_discover():
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
                    /UDP(sport=68,dport=67)\
                    /BOOTP(chaddr=[mac2str(spoofed_mac)],
                                   xid=transaction_id,
                                   flags=0xFFFFFF)\
                    /DHCP(options=options)
    sendp(dhcp_request,
          iface=conf.iface)




def print_packet(packet):
    ip_layer = packet.getlayer(IP)

    ip_list.append(ip_layer.src)
    return ip_list



#-----main
ip_list = []
def DHCP_check(address, port_list):
    dhcp_discover()
    sniff(filter="port 68", prn=print_packet, timeout=2)
    DHCP_service=False
    for i in ip_list:
        if str(i)==str(address):
            DHCP_service=True
    DHCP = (68 in port_list)
    if (DHCP_service == True and DHCP == False):
        problem = "DNS should be closed, but is open!"
        return problem
    if (DHCP_service == False and DHCP == True):
        problem = "DNS should be open, but is closed!"
        return problem
    else:
        return "DHCP is good"


#porty=[53,67]
#adres='192.168.2.1'

#print(DHCP_check(adres,porty))
