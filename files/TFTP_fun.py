import tftpy

class cTFTP:
    def __init__(self, dest_address, port_list):
        self.dest_address=dest_address
        self.port_list=port_list
        self.dest_port=69
        self.file = 'file.txt'
        self.path = '/home/file.txt'
        self.time_out = 3
        self.TFTP_service = True
        self.TFTP_port=(self.dest_port in self.port_list)
        self.tftp_result=None
        self.TFTP_query()
        self.TFTP_check()

    def TFTP_query(self):
        client=tftpy.TftpClient(self.dest_address, self.dest_port)
        try:
            client.download('file.txt', '/home/file.txt', timeout=self.time_out)
            raise tftpy.TftpContexts
        except tftpy.TftpTimeout:
            self.TFTP_service=False
        except:
            self.TFTP_service=True

    def TFTP_check(self):
        if (self.TFTP_service == True and self.TFTP_port == False):
            self.TFTP_result = "TFTP should be closed, but is open!"
        elif (self.TFTP_service == False and self.TFTP_port == True):
            self.TFTP_result = "TFTP should be open, but is closed!"
        else:
            self.TFTP_result = "TFTP is good"



#---------test
#add='127.0.0.1'
#port=[1,2,3,4,5,68]
#tftp_instance=cTFTP(add, port)
#print(tftp_instance.TFTP_result)

