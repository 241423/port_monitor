# port monitor

This script can help you control open ports on devices in your network. Program controls TCP ports and DNS, DHCP and TFTP. <br />

Required libraries:
socket
sys
datetime
os
dns.resolver
scapy
tftpy

 Create config file with port_list_creator 
Structure of config file - localhost  <br />

127.0.0.1    -- device ip address   <br />
53, 80, 631     -- list of TCP ports which should be open  <br />
53, 68      -- list of UDP ports which should be open  <br />
1   -- first TCP port in list range  <br />
1024    -- last TCP port in list range   <br />
60  -- scan frequency in minutes <br />

Use below command to run the script. localhost is config file

sudo python3 port_monitor.py localhost 

 The script will return a result. Sample report you can see in reports directory

How it work:  <br />
In TCP scan the ports are being requested by socket module. When response equal 0, it means the port is open.  <br />
In DNS scan the script send request to resolve domain, if DNS response anything, it means the port is open. <br />
In DHCP scan the script prepare DHCP Discover frame and send it. Next sniffs the responses and analyze results. <br />
In TFTP scan the script try download a file, if TFTP response anything, it means the port is open. <br />


