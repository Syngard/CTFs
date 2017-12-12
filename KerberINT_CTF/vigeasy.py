#!/usr/bin/python
import hashlib
import sys

from itertools import product
from itertools import cycle

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_{}'

flag = "TKlc_OLxUOhJMGbiVa0mhjHifvG6JiHDJZnhJ7ULikhxLra"
clear = "CTF{"

def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    pairs = zip(plaintext, cycle(key))
    result = ''

    for pair in pairs:
        (x,y)=pair
        #print(x,y)
        total = ALPHA.index(x) + ALPHA.index(y)
        result += ALPHA[total % len(ALPHA)]

    return result

def decryption(key, ciphertext):
    pairs = zip(ciphertext, cycle(key))
    result = ''

    for pair in pairs:
        (x,y)=pair
        #print(x,y)
        total = ALPHA.index(x) - ALPHA.index(y)
        result += ALPHA[total % len(ALPHA)]

    return result

"""
key = ''
for j in range(len(clear)):
    test_key = key
    for i in ALPHA:
        test_key = key + i
        test_decrypt = decryption(test_key, flag)
        #print test_decrypt
        if (test_decrypt[j] == clear[j]):
            print test_key
            key = test_key
            break
"""

#key=sys.argv[1]
#plaintext=sys.argv[2]+key
#cipher=encrypt(key,plaintext)
#print(cipher)

for n in range(4,len(flag)):
    for i in product(ALPHA, repeat = n):
        key = ''.join(i)
        #print key

        decrypted = decryption(key, flag)
        if (clear in decrypted and '}'+key in decrypted):
            print key + " >> " + decrypted
