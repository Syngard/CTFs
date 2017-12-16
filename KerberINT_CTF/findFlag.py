import socket
import time
import string

#ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_{}'
ALPHA = string.printable

HOST = 'localhost'
PORT = 3333

def tcp_client():
    client = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    client.connect(( HOST, PORT ))

    client.send("")
    print client.recv(4096)

    flag = 'CTF{'
    time.sleep(1)
    client.send(flag)

    print client.recv(4096)

    while (flag[-1] != '}'):
        for i in ALPHA:
            time.sleep(0.1)
            DATA = flag + i
            client.send(DATA)
            response = client.recv(4096)

            #print DATA + " // " + response
            if (testResponse(response)):
                flag += i
                print flag
                time.sleep(1)
                break
            else:
                print DATA

def testResponse(response):
    print response
    return ("Continue comme" in response)

if __name__ == '__main__':
    tcp_client()
