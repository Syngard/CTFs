#!/usr/bin/python -u
import random,string

flag = "FLAG:"
encflag = "BNZQ:2m8807395d9os2156v70qu84sy1w2i6e"
random.seed("random")
decflag = ""
"""
for c in flag:
  if c.islower():
    #rotate number around alphabet a random amount
    encflag += chr((ord(c)-ord('a')+random.randrange(0,26))%26 + ord('a'))
  elif c.isupper():
    encflag += chr((ord(c)-ord('A')+random.randrange(0,26))%26 + ord('A'))
  elif c.isdigit():
    encflag += chr((ord(c)-ord('0')+random.randrange(0,10))%10 + ord('0'))
  else:
    encflag += c
print "Unguessably Randomized Flag: "+encflag
"""
for c in encflag:
  if c.islower():
    #rotate number around alphabet a random amount
    decflag += chr((ord(c)-ord('a')-random.randrange(0,26))%26 + ord('a'))
  elif c.isupper():
    decflag += chr((ord(c)-ord('A')-random.randrange(0,26))%26 + ord('A'))
  elif c.isdigit():
    decflag += chr((ord(c)-ord('0')-random.randrange(0,10))%10 + ord('0'))
  else:
    decflag += c
    

print decflag
