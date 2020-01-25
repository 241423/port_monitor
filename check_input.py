import socket

def check_input(data):
    #check IP Address
    try:
        socket.inet_aton(data[0])
    except socket.error:
        print("Invalid input address!")

    #check tcp ports
    try:
        list(map(int, data[1].split(',')))
    except:
        print("Ports are not intiger")
    #check udp ports
    try:
        list(map(int, data[2].split(',')))
    except:
        print("Ports are not intiger")

    #check first port in range
    try:
        int(data[3])
    except:
        print("First port is not intiger")

    #check last port in range
    try:
        int(data[4])
    except:
        print("Last port is not intiger")

    #check port range
    if int(data[3])>=int(data[4]):
        print("Last port is lower than first one")
        exit(0)


    #check loop time
    try:
        int(data[5])
    except:
        print("Loop time is not intiger")



