import datetime
import sys
import check_input
import tcp_scanning
import udp_scanning

#Open file with data
input_file=sys.argv[1]
data = [line.strip() for line in open(input_file, "r")]

#Check input data
if len(data)!=6:
    print("Bad input file syntax!")
    exit(0)

check_input.check_input(data)

#Set Parameters
address=data[0]
TCP_port_list=list(map(int, data[1].split(',')))
UDP_port_list=list(map(int, data[2].split(',')))
first=int(data[3])
last=int(data[4])
sleep_time=int(data[5])

#Scanning Process

while True:
    #Create raport
    now=datetime.datetime.now()
    year=now.strftime("%Y")
    month=now.strftime("%m")
    day=now.strftime("%d")
    time=now.strftime("%H:%M:%S")

    raport="Scanning report "+now.strftime('%d/%m/%Y, %H:%M:%S')+"\n"

    #tcp_result=(raport+tcp_scanning.tcp_scan(address, TCP_port_list, first, last))
    #raport=tcp_result
    #print(raport)

    udp_scanning.udp_scan(address, UDP_port_list)




    import time
    time.sleep(sleep_time)

    today = ('{}-{}-{}').format(day, month, year)
    file_save_name = ("raport ip:{} date: {} ".format(address, today))
    print(file_save_name)
    # Write report to file
    with open(file_save_name, 'a') as file:
        file.write("elo" + "\n")


