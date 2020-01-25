import socket


def tcp_scan(address, port_list, first, last):
    open_ports=[]  #list with open ports
    #Ports scanning
    for port in range(first,last):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #create socket
        result=s.connect_ex((address, port))  #try connect
        if(result==0): #if connect is good add to list
            open_ports.append(port)
    scan_problems='TCP scan result:\n'
    #Check ports
    good_flag=True #to result information
    for i in open_ports:
        check=(i in port_list) #Check this open port should be open
        if(check==False): #if no
            problem=("Warning! Port {} should be closed!".format(i))
            good_flag=False
            scan_problems=(scan_problems+problem+"\n")
    if good_flag==True:
        scan_problems=scan_problems+"TCP is good\n"
    return scan_problems

#adres="127.0.0.1"
#porty=[53,81]
#pierwszy=50
#ostatni=100
#print(tcp_scan(adres,porty,pierwszy,ostatni))