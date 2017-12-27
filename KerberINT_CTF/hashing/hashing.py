#! /usr/bin/python

import hashlib

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

flag_sum = "612eb3c0d9879006cb2beef6fa3c8cd2"

for a in alphabets:
    for b in alphabets:
        for c in alphabets:
            for d in alphabets:
                for e in alphabets:
                    flag = "CTF{"+a+b+c+d+e+"}"
                    m = hashlib.md5(flag).hexdigest()
                    #print flag + " << " + m
                    if (str(m) == flag_sum):
                        print flag
