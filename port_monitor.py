import socket
import datetime

#Open file with pattern ports
with open('port_list.txt', 'r+') as f:
    y=f.read()
    x=y.split(',')

#Parameters
port_list=list(map(int,x))
address='192.168.2.10'
open_ports=[]
first=20
last=25

#Ports scanning
for port in range(first,last):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result=s.connect_ex((address, port))
    if(result==0):
        print("port {} is open".format(port))
        open_ports.append(port)

#Create raport
now=datetime.datetime.now()
year=now.strftime("%Y")
month=now.strftime("%m")
day=now.strftime("%d")
time=now.strftime("%H:%M:%S")

raport="Scanning report "+now.strftime('%d/%m/%Y, %H:%M:%S')+"\n"


#Check ports
for i in open_ports:
    check=(i in port_list) #Check this open port should be open
    if(check==False): #if no
        problem=("Warning! Port {} should be closed!".format(i))
        print(problem)
        raport=(raport+problem+"\n")


print(raport)

#Write report to file
with open ('raport.txt', 'a') as file:
    file.write(raport+"\n")




#port_list=[20,21,22,23,53,80,443]
#print(port_list)
#with open('port_list.txt', 'w+') as f:
#    f.write(str(port_list))