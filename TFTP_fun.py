import tftpy

def TFTP_check(address, port_list):
    TFTP_service = True
    client = tftpy.TftpClient(address, 69)
    try:
        client.download('file.txt', '/home/file.txt', timeout=3)
        raise tftpy.TftpContexts
    except tftpy.TftpTimeout:
        TFTP_service=False
    except:
        TFTP_service=True

    TFTP=(69 in port_list)
    if(TFTP_service==True and TFTP==False):
        problem="TFTP should be closed, but is open!"
        return problem
    elif(TFTP_service==False and TFTP==True):
        problem = "TFTP should be open, but is closed!"
        return problem
    else:
        return "TFTP is good"



#porty=[53,67]
#adres='192.168.2.1'

#print(TFTP_check(adres,porty))