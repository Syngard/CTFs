import random
import sys
import time

#cur_time = str(time.time()).encode('ASCII')
cur_time = '1513719133.8728752'.encode('ASCII')
random.seed(cur_time)


#msg = input('Your message: ').encode('ASCII')
with open("top_secret",'rb') as msg:
    flag_time = msg.read()
    flag = flag_time[:len(flag_time)-19]
    
    #print "flag_time = "+flag_time
    #print "flag = "+flag
    
    key = [random.randrange(256) for _ in flag]
    print(key[:5])
    
    c = [chr(m ^ k) for (m,k) in zip(flag, key)]
   
    f = ""
    for i in c:
        f += i
    print(f)


'''
with open("decr_flag", "wb") as f:
    f.write(bytes(c))
'''
'''
with open("top_secret", "rb") as encr_flag:
    flag = str(encr_flag.read())[-19:]
    print flag
    time = [chr(ord(m)^k) for (m,k) in zip(flag, [0x88]*18)]
    print str(time)
'''
'''
with open("top_secret",'rb') as msg:
    encr_time = str(msg.read())[-19:]
    c = [chr(ord(m) ^ ord(k)) for (m,k) in zip(encr_time,  cur_time)]
    print c
'''
