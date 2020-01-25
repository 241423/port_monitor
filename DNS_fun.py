import dns.resolver
from dns.exception import DNSException
def DNS_check(address, port_list):
    DNS_service = True
    my_resolver = dns.resolver.Resolver()
    my_resolver.nameservers = [address]  # ip address DNS server
    my_resolver.lifetime = 3  # time out
    my_resolver.timeout=3
    try:
        answer = my_resolver.query('google.com')
        raise  dns.exception.Timeout
    except dns.exception.Timeout:
        DNS_service = False
    except:
        DNS_service=True


    DNS=(53 in port_list)
    if(DNS_service==True and DNS==False):
        #print("DNS jest włączony a nie powinien")
        problem="DNS should be closed, but is open!"
        return problem
    elif(DNS_service==False and DNS==True):
        #print("DNS jest wyłączony a powinien byc wlaczony")
        problem = "DNS should be open, but is closed!"
        return problem
    else:
        return "DNS is good"


#porty=[53,68]
#adres='127.0.0.1'

#print(DNS_check(adres,porty))
