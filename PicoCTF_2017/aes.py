#! /usr/bin/python

from Crypto import Random
from Crypto.Cipher import AES
import base64

BLOCK_SIZE=64

def decrypt(encrypted, passphrase):

    passphrase = base64.b64decode(passphrase)
    
    aes = AES.new(passphrase, AES.MODE_ECB)
    return aes.decrypt(base64.b64decode(encrypted))

print(decrypt("aZUMiYeh+dN3+P0YFY8zYSTxvVVrskO9sM1Gpb20hpMmhyRCyr2YPfuyOQLrRX2f","5NQdRr6sjjkFnHSAOvAVeg=="))
