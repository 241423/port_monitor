import tftpy

def TFTP_check(address, port_list):
    TFTP_service = True
    client = tftpy.TftpClient('127.0.0.1', 69)
    try:
        x=client.download('test_tftp.txt', '/home/mati/test_tftp.txt', timeout=2)
    except OSError as err:
        print("OS error: {0}".format(err))
        print("elo")
    except:
        TFTP_service=False

    TFTP=(69 in port_list)
    if(TFTP_service==True and TFTP==False):
        problem="TFTP should be closed, but is open!"
        return problem
    elif(TFTP_service==False and TFTP==True):
        problem = "TFTP should be open, but is closed!"
        return problem
    else:
        return "TFTP is good"



porty=[53,67]
adres='192.168.2.1'

TFTP_check(adres,porty)