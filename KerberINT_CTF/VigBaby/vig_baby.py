#!/usr/bin/python

import hashlib
import sys

from itertools import cycle

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_{}'

ciphertext = "TKlc_OLxUOhJMGbiVa0mhjHifvG6JiHDJZnhJ7ULikhxLra"

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

def decrypt(key, ciphertext):
    pairs = zip(ciphertext, cycle(key))
    result = ''

    for pair in pairs:
        (x,y)=pair
        #print(x,y)
        total = ALPHA.index(x) - ALPHA.index(y)
        result += ALPHA[total % len(ALPHA)]

    return result

def find_key(cipher,clear):
    key = ''
    for i in range(len(clear)):
        for j in ALPHA:
            key_tmp = key + j
            test_decrypt = decrypt(key_tmp, cipher)
            if (test_decrypt[i] == clear[i]):
                key += j
                break
    return key

print find_key(ciphertext, "CTF{")
