import DNS_fun
import DHCP_fun
import TFTP_fun

#---------main
def udp_scan(address, port_list):
    scan_problems = 'UDP scan result:\n'

    DNS_result=DNS_fun.DNS_check(address,port_list)
    scan_problems=scan_problems+str(DNS_result)+'\n'

    DHCP_result = DHCP_fun.DHCP_check(address, port_list)
    scan_problems = scan_problems + str(DHCP_result) + '\n'

    #TFTP_result=TFTP_fun.TFTP_check(address, port_list)
    #scan_problems = scan_problems + str(TFTP_result)+'\n'

    print(scan_problems)

adres='127.0.0.1'
porty=[1,2]
udp_scan(adres,porty)


