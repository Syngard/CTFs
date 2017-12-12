#! /usr/bin/python

import socket
import time

def verif_bit(letter, verif):
    count = 0
    for i in letter:
        if (i == '1'):
            count += 1
    return (count%2 == verif)

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.send(content)
    #s.shutdown(socket.SHUT_WR)
        
    data = s.recv(1024)
    data = data[-12:]
    #print data
    
    flag = ""

    while 1:
        letter = data[1:9]
        verif  = data[9]
        
        #print data

        if verif_bit(letter, int(verif)):
            flag+= chr(int(letter,2))
            #print "Right"
            s.send("1")
            #time.sleep(1)
            print flag
        else:
            #print "Wrong"
            s.send("0")
            #time.sleep(1)

        data = s.recv(1024)

    print "Connection closed."
    s.close()



netcat("misc.chal.csaw.io", 4239, "")

#print verif_bit("01010101",1)
#print verif_bit("01010101",0)
