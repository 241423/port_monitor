import dns.resolver

class cDNS:
    def __init__(self, dest_address, port_list):
        self.dest_address=dest_address
        self.port_list=port_list
        self.dest_port=53
        self.time_out = 3
        self.DNS_service=True
        self.DNS_port=(self.dest_port in port_list)
        self.DNS_result=None
        self.DNS_query()
        self.DNS_check()

    def DNS_query(self):
        my_resolver = dns.resolver.Resolver()
        my_resolver.nameservers = [self.dest_address]
        my_resolver.lifetime = 3
        try:
            my_resolver.query('google.com')
            my_resolver.put(False, timeout=self.time_out)
            raise  dns.exception.Timeout
        except dns.exception.Timeout:
            self.DNS_service = False
        except:
            self.DNS_service=True

    def DNS_check(self):
        if(self.DNS_service==True and self.DNS_port==False):
            self.DNS_result="DNS should be closed, but is open!"
        elif(self.DNS_service==False and self.DNS_port==True):
            self.DNS_result = "DNS should be open, but is closed!"
        else:
            self.DNS_result = "DNS is good"


#------test
#porty=[53,68]
#adres='127.0.0.1'
#dns_instance=cDNS(adres, porty)
#print(dns_instance.DNS_result)
