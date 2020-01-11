

#------address
def check_IP():
    while(True):
        address=input("Enter target's input: ")
        pieces = address.split('.')
        if len(pieces) != 4:
            print("Invalid input")
            continue
        try:
            all(0 <= int(p) < 256 for p in pieces)

        except ValueError:
            print("Invalid input")
            continue
        return address

#------TCP ports
def TCP_ports():
    port_list=[]
    while(True):
        flag=False
        port_list=input("Enter TCP ports separating ',': ")
        try:
            port_list = list(map(int, port_list.split(',')))
        except:
            print("Invalid input, try again!")
            continue
        for i in port_list:
            if i<0 or i>65535:
                print("Invalid input, try again!")
                flag=True
        if flag==False:
            return port_list

#------ TCP ports range
def TCP_range():
    first=1
    last=65535
    while(True):
        first=input("Enter first port: ")
        try:
            int(first)
        except:
            print("Invalid input, try again!")
            continue
        if int(first)<1 or int(first)>65535:
            print("Invalid input, try again!")
            continue
        else:
            break
    while(True):
        last=input("Enter last port: ")
        try:
            int(last)
        except:
            print("Invalid input, try again!")
            continue
        if int(last)<1 or int(last)>65535:
            print("Invalid input, try again!")
            continue
        elif first>last:
            print("First port is higher than last port!")
        else:
            return first,last

#------UDP ports
def UDP_ports():
    port_list=[]
    flag_DNS=input("Is DNS open? Enter 'y' default no :")
    if flag_DNS=='y':
        port_list.append(53)
    flag_DHCP = input("Is DHCP open? Enter 'y' default no :")
    if flag_DHCP == 'y':
        port_list.append(67)
    flag_TFTP = input("Is TFTP open? Enter 'y' default no :")
    if flag_TFTP == 'y':
        port_list.append(69)


#------scanning frequency

def scan_frequency():
    while(True):
        time=input("Enter scanning frequency [seconds], min 30s : ")
        try:
            int(time)
        except:
            print("Invalid input, try again!")
            continue
        if int(time)<30:
            print("Invalid input, try again!")
            continue
        return time


#------main
IP_address=check_IP()
ports_TCP=TCP_ports()
range=TCP_range()
ports_UDP=UDP_ports()
time_f=scan_frequency()

print("Ip address: ",IP_address)
print("TCP ports: ",ports_TCP)
print("TCP first port: ",range[0])
print("TCP last port: ", range[1])
print("UDP ports: ", ports_UDP )
print("Scanning frequency: ",time_f)

save_flag=input("Do you want save it? Enter 'y': ")
if save_flag=='y':
    file_name=input("Enter filename: ")
with open(file_name, 'w+') as f:
    f.write(str(IP_address)+'\n')
    f.write(str(ports_TCP) + '\n')
    f.write(str(ports_UDP) + '\n')
    f.write(str(range[0]) + '\n')
    f.write(str(range[1]) + '\n')
    f.write(str(time_f) + '\n')





